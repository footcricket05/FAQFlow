from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import FAQ
from .serializers import FAQSerializer


class FAQViewSet(ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        """Return FAQs based on requested language."""
        lang = request.GET.get('lang', 'en')
        faqs = self.get_queryset()

        data = [
            {
                "id": faq.id,
                "question": faq.get_translated_faq(lang)["question"],
                "answer": faq.get_translated_faq(lang)["answer"]
            }
            for faq in faqs
        ]

        return JsonResponse(
            data, safe=False,
            json_dumps_params={'ensure_ascii': False}
        )
