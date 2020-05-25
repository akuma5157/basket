"""
Do not modify this file. It is generated from the Swagger specification.
Create fixtures file by running "./manage.py dumpdata core auth -o core/fixtures/core.json"


"""
import logging
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, tag
from django.contrib.sessions.middleware import SessionMiddleware

from . import views

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def add_session_to_request(request):
    """Annotate a request object with a session"""
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()


class CoreTestSeed(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        # self.user = User.objects.get(username="ajay")

    @tag('get', 'getTime')
    def Test_getTime(self):
        # Create an instance of a GET request.
        vars = dict()
        request = self.factory.get('time/', vars)
        add_session_to_request(request)

        # Checking for anonymous user
        # simulating a non-logged-in request
        request.user = AnonymousUser()

        # Test Time.as_view() as if it were deployed at time/
        response = views.Time.as_view()(request, )
        # self.assertEqual(response.status_code, 401)

        ## simulating a logged in user
        # request.user = self.user

        ## Test Time.as_view() as if it were deployed at time/
        # response = views.Time.as_view()(request, )
        print(response.content)
        self.assertEqual(response.status_code, 200)
