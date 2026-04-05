from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse, OpenApiExample
from .models import Article
from .serializers import ArticleSerializer

class ArticleListView(APIView):
    """
    Barcha maqolalar ro'yxatini olish
    """
    
    @extend_schema(
        tags=['Maqolalar'],
        summary="Barcha maqolalar ro'yxati",
        description="""
        Tizimdagi barcha maqolalar ro'yxatini qaytaradi.
        
        Maqolalar nashr etilgan sana bo'yicha saralangan holda qaytariladi.
        """,
        responses={
            200: OpenApiResponse(
                response=ArticleSerializer(many=True),
                description='Muvaffaqiyatli. Maqolalar ro\'yxati qaytarildi.',
                examples=[
                    OpenApiExample(
                        'Maqolalar ro\'yxati',
                        value=[
                            {
                                'id': 1,
                                'title': 'Matematika fanidan tadqiqot',
                                'description': 'Bu maqolada matematika...',
                                'author': 1,
                                'author_name': 'Alisher Navoiy',
                                'published_date': '2026-03-15T12:00:00Z',
                                'is_active': True
                            }
                        ]
                    )
                ]
            )
        }
    )
    def get(self, request):
        """Barcha maqolalarni olish"""
        articles = Article.objects.all().order_by('-published_date')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    

class ArticleDetailView(APIView):
    """
    Bitta maqola tafsilotlarini olish
    """
    
    @extend_schema(
        tags=['Maqolalar'],
        summary="Maqola tafsilotlari",
        description="""
        Berilgan ID bo'yicha maqolaning to'liq ma'lumotlarini qaytaradi.
        
        Agar maqola topilmasa, 404 xato qaytariladi.
        """,
        responses={
            200: OpenApiResponse(
                response=ArticleSerializer,
                description='Muvaffaqiyatli. Maqola tafsilotlari qaytarildi.',
                examples=[
                    OpenApiExample(
                        'Maqola tafsiloti',
                        value={
                            'id': 1,
                            'title': 'Matematika fanidan tadqiqot',
                            'description': 'Bu maqolada matematika sohasidagi yangi tadqiqotlar keltirilgan...',
                            'literature': 'Adabiyotlar ro\'yxati...',
                            'pdf': '/media/articles/pdfs/maqola.pdf',
                            'image': '/media/articles/images/cover.jpg',
                            'author': 1,
                            'author_name': 'Alisher Navoiy',
                            'is_active': True,
                            'published_date': '2026-03-15T12:00:00Z'
                        }
                    )
                ]
            ),
            404: OpenApiResponse(
                description='Maqola topilmadi'
            )
        }
    )
    def get(self, request, pk):
        """Bitta maqolaning tafsilotlarini olish"""
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response(
                {'error': 'Maqola topilmadi'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    


