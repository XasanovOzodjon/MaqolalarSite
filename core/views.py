from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from articles.models import Article
from teachers.models import Teacher

class StatisticsView(APIView):
    """
    Tizim statistikasini olish
    """
    
    @extend_schema(
        tags=['Statistika'],
        summary="Tizim statistikasi",
        description="""
        Tizimdagi umumiy statistik ma'lumotlarni qaytaradi:
        - Jami maqolalar soni
        - Jami o'qituvchilar soni
        - Faol maqolalar soni
        """,
        responses={
            200: OpenApiResponse(
                description='Muvaffaqiyatli. Statistika ma\'lumotlari qaytarildi.',
                examples=[
                    OpenApiExample(
                        'Statistika',
                        value={
                            'total_articles': 25,
                            'total_teachers': 10,
                            'active_articles': 20
                        }
                    )
                ]
            )
        }
    )
    def get(self, request):
        """Tizim statistikasini olish"""
        data = {
            'total_articles': Article.objects.count(),
            'total_teachers': Teacher.objects.count(),
            'active_articles': Article.objects.filter(is_active=True).count(),
        }
        return Response(data, status=status.HTTP_200_OK)