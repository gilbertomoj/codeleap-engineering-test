from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class PostRouteTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.default_response = ''
    def tearDown(self):
        pass

    def test_get_posts(self):
        """Test GET /posts"""
        response = self.client.get("/list")
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data, list)
        assert all("id" in post and "title" in post and "content" in post for post in response.data)

    def test_create_post(self):
        response = self.client.post("/create",
                                    {"title": "Test title", "content": "Test content", "username": "Test user1"})
        self.default_response = response
        assert response.status_code == status.HTTP_201_CREATED
        assert isinstance(response.data, dict)
        assert response.data["title"] == "Test title"

    def test_detail_post(self):
        create_response = self.client.post(
            "/create",
            {"title": "Detail title", "content": "Detail content", "username": "Test user2"},
        )
        response = self.client.get(f"/detail/{create_response.data['id']}")
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data, dict)
        assert response.data["title"] == "Detail title"

    def test_update_post(self):
        create_response = self.client.post(
            "/create",
            {"title": "Detail title", "content": "Detail content", "username": "Test user"},
        )
        response = self.client.patch(f"/update/{create_response.data['id']}",
                                    {"title": "Test title update", "content": "Test content update"})

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data, dict)
        assert response.data["title"] == "Test title update"
        assert response.data["content"] == "Test content update"

    def test_delete_post(self):
        create_response = self.client.post(
            "/create",
            {"title": "Detail title", "content": "Detail content", "username": "Test user"},
        )
        response = self.client.delete(f"/delete/{create_response.data['id']}")
        assert response.status_code == status.HTTP_204_NO_CONTENT