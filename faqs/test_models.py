from django.test import TestCase
from .models import FAQ


class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework."
    )

    def test_faq_creation(self):
        """Test if FAQ is created successfully."""
        self.assertEqual(
            self.faq.question, "What is Django?"
        )
        self.assertEqual(
            self.faq.answer, "Django is a Python web framework."
        )

    def test_faq_translation(self):
        """Test if translations are generated."""
        self.assertIsNotNone(self.faq.question_hi)
        self.assertIsNotNone(self.faq.question_bn)
