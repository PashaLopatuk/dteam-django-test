from django.test import TestCase

from main.models import RequestLog

# Create your tests here.


class TestCVView(TestCase):
    fixtures = ["CVs"]

    def test_index(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_cv_info(self):
        cv_expected_content = {
            "id": 1,
            "firstname": "John",
        }

        response = self.client.get(f"/cv/{cv_expected_content['id']}")

        self.assertEqual(response.status_code, 200)
        self.assertIn(cv_expected_content["firstname"], response.content.decode())


class TestRequestLoging(TestCase):
    def test_request_logs_in_db(self):
        logs = RequestLog.objects.all()
        
        self.assertEqual(len(logs), 0)
        
        self.client.get('/')
        
        log: RequestLog = RequestLog.objects.get()
        
        self.assertEqual(log.http_method, "GET")
