from datetime import timezone

from django.test import TestCase
from django.urls import reverse

from workspace.models import Task, Tag


class SwitchStatusTests(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name='test')
        self.task = Task.objects.create(
            content="test",
            status=False
        )
        self.task.tags.add(self.tag)

    def test_switch_status(self):
        url = reverse("workspace:switch-status", args=[self.task.id])
        response = self.client.get(url)

        self.task.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.task.status)
