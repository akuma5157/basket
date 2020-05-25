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

import core.schemas as schemas
import core.utils as utils

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
    stub_class_path = "core.stubs.MockedStubClass"

module_name, class_name = stub_class_path.rsplit(".", 1)
Module = importlib.import_module(module_name)
Stubs = getattr(Module, class_name)


def maybe_validate_result(result_string, schema):
    if VALIDATE_RESPONSES:
        try:
            utils.validate(json.loads(result_string, encoding="utf8"), schema)
        except ValidationError as e:
            logger.error(e.message)


@method_decorator(csrf_exempt, name="dispatch")
class Time(View):

    GET_RESPONSE_SCHEMA = schemas.Time

    def get(self, request, *args, **kwargs):
        """
        :param self: A Time instance
        :param request: An HttpRequest
        """
        try:
            logger.debug("Calling getTime()")
            result = Stubs.getTime(request, )
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

            maybe_validate_result(response.content, self.GET_RESPONSE_SCHEMA)

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