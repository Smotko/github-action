from django.test import SimpleTestCase, TestCase, override_settings
from django.contrib.auth.models import User

class DbTests(TestCase):
    def test_connection(self):
        User.objects.all()
