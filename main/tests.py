from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Skills


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))
 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
 
        api_response = self.client.get(reverse("api:experience-list"))
        self.assertEqual(api_response.status_code, 200)
        data = api_response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], self.experience.title)
        self.assertEqual(data[0]["description"], self.experience.description)
        self.assertEqual(data[0]["category_display"], "Part-Time")
        self.assertTrue(data[0]["is_ongoing"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
 
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
 
        api_response = self.client.get(reverse("api:experience-list"))
        self.assertEqual(api_response.status_code, 200)
        self.assertEqual(api_response.json(), [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
 
        api_response = self.client.get(
            reverse("api:experience-detail", args=[self.experience.id])
        )
 
        self.assertFalse(self.experience.is_ongoing)
        self.assertEqual(api_response.status_code, 200)
        self.assertFalse(api_response.json()["is_ongoing"])
        self.assertIsNotNone(api_response.json()["ended_at"])

class SkillTest(TestCase):
    def setUp(self):
        self.skill = Skills.objects.create(
            name="Python",
            category="language",
        )

    def test_show_skills_page_uses_correct_template(self):
        response = self.client.get(reverse("main:show_skills"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skills.html")

    def test_skill_appears_when_data_exists(self):
        response = self.client.get(reverse("main:show_skills"))
        self.assertContains(response, "Python")
        self.assertContains(response, self.skill.get_category_display())

    def test_empty_skills_page(self):
        Skills.objects.all().delete()
        response = self.client.get(reverse("main:show_skills"))
        self.assertContains(response, "Belum ada data skill.")