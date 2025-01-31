from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from deep_translator import GoogleTranslator  # Better than googletrans


LANGUAGES = {'hi': 'Hindi', 'bn': 'Bengali', 'en': 'English'}


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)

    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def translate_text(self, text, dest_language):
        """Translate text using Deep Translator and cache results."""
        cache_key = f"translation_{self.id}_{dest_language}"
        cached_translation = cache.get(cache_key)

        if cached_translation:
            return cached_translation

        translated_text = GoogleTranslator(
            source='auto',
            target=dest_language
        ).translate(text)

        translated_text = translated_text.encode('utf-8').decode('utf-8')

        cache.set(
            cache_key,
            translated_text,
            timeout=86400
        )

        return translated_text

    def get_translated_faq(self, lang):
        """Return translated FAQ if available, else default to English."""
        if lang in LANGUAGES:
            return {
                "question": getattr(self, f'question_{lang}', self.question),
                "answer": getattr(self, f'answer_{lang}', self.answer),
            }
        return {"question": self.question, "answer": self.answer}

    def save(self, *args, **kwargs):
        """Auto-translate FAQ content before saving."""
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, 'hi')
        if not self.answer_hi:
            self.answer_hi = self.translate_text(self.answer, 'hi')

        if not self.question_bn:
            self.question_bn = self.translate_text(self.question, 'bn')
        if not self.answer_bn:
            self.answer_bn = self.translate_text(self.answer, 'bn')

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
