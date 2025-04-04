from main.models import CV
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class CVApiViewTest(APITestCase):
    fixtures = ["CVs"]

    def setUp(self):
        self.cv = CV(
            id=1,
            firstname="John",
            lastname="Doe",
            skills="Python, Django, PostgreSQL, React, AWS",
            projects="Project 1: CRM system for small businesses; Project 2: Task management system",
            bio="Experienced Fullstack developer with strong skills in Python and JavaScript.",
            contacts="email: john.doe@example.com, phone: +1234567890",
        )

        self.list_url = reverse("api/cv_list")
        self.detail_url = reverse("api/cv_detail", kwargs={"pk": self.cv.id})

    def test_get_cv_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 11)
        self.assertEqual(response.data[0]["firstname"], self.cv.firstname)

    def test_create_cv(self):
        data = {
            "firstname": "Alice",
            "lastname": "Smith",
            "skills": "React, TypeScript",
            "projects": "Portfolio, Dashboard",
            "bio": "Frontend developer",
            "contacts": "alice.smith@example.com",
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CV.objects.count(), 12)
        self.assertEqual(response.data["firstname"], "Alice")
        self.assertIn("id", response.data)

    def test_get_single_cv(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["firstname"], self.cv.firstname)

    def test_update_cv(self):
        new_name = "Johnny"
        updated_data = {
            "firstname": new_name,
            "lastname": "Doe",
            "skills": "Python, Django, FastAPI",
            "projects": "Updated Project",
            "bio": "Senior Developer",
            "contacts": "johnny.doe@example.com",
        }
        response = self.client.put(self.detail_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cv.refresh_from_db()
        self.assertEqual(self.cv.firstname, new_name)

    def test_delete_cv(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CV.objects.count(), 10)
