"""
Do not modify this file. It is generated from the Swagger specification.

"""
import importlib
import logging
import json
from django.core.serializers.json import DjangoJSONEncoder
from jsonschema import ValidationError

from django.conf import settings
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import os

import {{ module }}.schemas as schemas
import {{ module }}.utils as utils

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logging.getLogger('keyring').setLevel(logging.CRITICAL)
logging.getLogger('msrestazure').setLevel(logging.CRITICAL)
logging.getLogger('requests_oauthlib').setLevel(logging.CRITICAL)
logging.getLogger('boto').setLevel(logging.CRITICAL)
logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('botocore').setLevel(logging.CRITICAL)
logging.getLogger('s3transfer').setLevel(logging.CRITICAL)
logging.getLogger('urllib3').setLevel(logging.CRITICAL)


try:
    VALIDATE_RESPONSES = settings.SWAGGER_API_VALIDATE_RESPONSES
except AttributeError:
    VALIDATE_RESPONSES = False
logger.info("Swagger API response validation is {}".format(
    "on" if VALIDATE_RESPONSES else "off"
))

# Set up the stub class. If it is not explicitly configured in the settings.py
# file of the project, we default to a mocked class.
try:
    stub_class_path = settings.STUBS_CLASS
except AttributeError:
    stub_class_path = "{{ module }}.stubs.MockedStubClass"

module_name, class_name = stub_class_path.rsplit(".", 1)
Module = importlib.import_module(module_name)
Stubs = getattr(Module, class_name)


def maybe_validate_result(result_string, schema):
    if VALIDATE_RESPONSES:
        try:
            utils.validate(json.loads(result_string, encoding="utf8"), schema)
        except ValidationError as e:
            logger.error(e.message)


{% for class_name, verbs in classes|dictsort(true) %}
@method_decorator(csrf_exempt, name="dispatch")
  {% for verb, info in verbs|dictsort(true) %}
    {% if info.secure %}
@method_decorator(utils.login_required_no_redirect, name="{{ verb }}")
    {% endif %}
  {% endfor %}
class {{ class_name }}(View):

{% for verb, info in verbs|dictsort(true) %}
    {{ verb|upper }}_RESPONSE_SCHEMA = {{ info.response_schema }}
{% endfor %}
{% for verb, info in verbs|dictsort(true) if info.body %}
    {{ verb|upper }}_BODY_SCHEMA = {{ info.body.schema }}
{% endfor %}

{% for verb, info in verbs|dictsort(true) %}
    def {{ verb }}(self, request, {% for ra in info.required_args if ra.in == "path" %}{{ ra.name }}, {% endfor %}*args, **kwargs):
        """
        :param self: A {{ class_name }} instance
        :param request: An HttpRequest
        {% for ra in info.required_args if ra.in == "path" %}
        :param {{ ra.name }}: {{ ra.type }} {{ ra.description }}
        {% endfor %}
        """
  {% if info.body %}
        body = utils.body_to_dict(request.body, self.{{ verb|upper}}_BODY_SCHEMA)
        if not body:
            return HttpResponseBadRequest("Body required")

  {% endif %}
        try:
    {% for ra in info.required_args if ra.in == "query" %}
            if "{{ ra.name }}" not in request.GET:
                return HttpResponseBadRequest("{{ ra.name }} required")

      {% if ra.type == "array" %}
        {% if ra.collectionFormat == "multi" %}
            {{ ra.name }} = request.GET.getlist("{{ ra.name }}", None)
        {% else %}
            {{ ra.name }} = request.GET.get("{{ ra.name }}", None)
            if {{ ra.name }} is not None:
                {{ ra|parse_array }}
          {% if ra["items"].type == "integer" %}
                if {{ ra.name }}:
                    {{ ra.name }} = [int(e) for e in {{ ra.name }}]
          {% endif %}
        {% endif %}
      {% else %}
            {{ ra.name }} = request.GET.get("{{ ra.name }}")
      {% endif %}

      {% if ra.type == "boolean" %}
            {{ ra.name }} = ({{ ra.name }}.lower() == "true")
      {% elif ra.type == "integer" %}
            {{ ra.name }} = int({{ ra.name }})
      {% endif %}
            schema = {{ ra|clean_schema }}
            utils.validate({{ ra.name }}, schema)
    {% endfor %}
    {% for oa in info.optional_args if oa.in == "query" %}
            # {{ oa.name }} (optional): {{ oa.type }} {{ oa.description }}
      {% if oa.type == "array" %}
        {% if oa.collectionFormat == "multi" %}
            {{ oa.name }} = request.GET.getlist("{{ oa.name }}", None)
        {% else %}
            {{ oa.name }} = request.GET.get("{{ oa.name }}", None)
            if {{ oa.name }} is not None:
                {{ oa|parse_array }}
          {% if oa["items"].type == "integer" %}
                if {{ oa.name }}:
                    {{ oa.name }} = [int(e) for e in {{ oa.name }}]
          {% endif %}
        {% endif %}
      {% else %}
            {{ oa.name }} = request.GET.get("{{ oa.name }}", None)
      {% endif %}
            if {{ oa.name }} is not None:
      {% if oa.type == "boolean" %}
                {{ oa.name }} = ({{ oa.name }}.lower() == "true")
      {% elif oa.type == "integer" %}
                {{ oa.name }} = int({{ oa.name }})
      {% endif %}
                schema = {{ oa|clean_schema }}
                utils.validate({{ oa.name }}, schema)
    {% endfor %}
    {% if info.form_data %}
            form_data = {}
      {% for data in info.form_data %}
        {% if data.type == "file" %}
          {% if data.collectionFormat == "multi" %}
            {{ data.name }} = request.FILES.getlist("{{ data.name }}", None)
          {% else %}
            {{ data.name }} = request.FILES.get("{{ data.name }}", None)
          {% endif %}
        {% else %}
          {% if data.collectionFormat == "multi" %}
            {{ data.name }} = request.POST.getlist("{{ data.name }}", None)
          {% else %}
            {{ data.name }} = request.POST.get("{{ data.name }}", None)
          {% endif %}
        {% endif %}
        {% if data.required %}
            if not {{ data.name }}:
                return HttpResponseBadRequest("Formdata field '{{ data.name }}' required.")
        {% endif %}
            form_data["{{ data.name }}"] = {{ data.name }}
      {% endfor %}
    {% endif %}
            logger.debug("Calling {{ info.operation }}()")
            result = Stubs.{{ info.operation }}(request, {% if info.body %}body, {% endif %}{% if info.form_data %}form_data, {% endif %}
                {% for ra in info.required_args %}{{ ra.name }}, {% endfor %}
                {% for oa in info.optional_args if oa.in == "query" %}{{ oa.name }}, {% endfor %})
            logger.debug("Returned Result: {}".format(json.dumps(result, cls=DjangoJSONEncoder)))
            if type(result) is tuple:
                result, headers, status = result
            else:
                headers = {}
                status = 200

            # The result may contain fields with date or datetime values that will not
            # pass JSON validation. We first create the response, and then maybe validate
            # the response content against the schema.
            response = JsonResponse(result, status=status, safe=False)

            maybe_validate_result(response.content, self.{{ verb|upper }}_RESPONSE_SCHEMA)

            for key, val in headers.items():
                response[key] = val
            return response
        except PermissionDenied as pd:
            logger.exception("403")
            return HttpResponseForbidden("Permission Denied: {}".format(str(pd)))
        except ObjectDoesNotExist as dne:
            logger.exception("404")
            return HttpResponseNotFound("Not Found: {}".format(str(dne)))
        except ValidationError as ve:
            logger.exception("400")
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            logger.exception("400")
            return HttpResponseBadRequest("Parameter validation failed: {}".format(ve))
        except Exception as e:
            logger.exception("500")
            return JsonResponse(str(e), status=500, safe=False)

    {% if not loop.last %}
    {% endif %}
  {% endfor %}


{% endfor %}
class __SWAGGER_SPEC__(View):

    def get(self, request, *args, **kwargs):
        with open(os.path.join("swagger_specification.json"), "r") as f:
         spec = json.loads(f.read ())
        # Mod spec to point to demo application
        spec["basePath"] = "/"
        spec["host"] = "localhost:8000"
        # Add basic auth as a security definition
        security_definitions = spec.get("securityDefinitions", {})
        security_definitions["basic_auth"] = {"type": "basic"}
        spec["securityDefinitions"] = security_definitions
        return JsonResponse(spec)