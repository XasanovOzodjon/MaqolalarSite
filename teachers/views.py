from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse, OpenApiExample
from .models import Teacher
from .serializers import TeacherSerializer


class TeacherListView(APIView):
    """
    Barcha o'qituvchilar ro'yxatini olish
    """
    
    @extend_schema(
        tags=['O\'qituvchilar'],
        summary="Barcha o'qituvchilar ro'yxati",
        description="""
        Tizimdagi barcha o'qituvchilar ro'yxatini qaytaradi.
        
        Har bir o'qituvchi haqida to'liq ma'lumot, shu jumladan 
        ularning maqolalari soni ham qaytariladi.
        """,
        responses={
            200: OpenApiResponse(
                response=TeacherSerializer(many=True),
                description='Muvaffaqiyatli. O\'qituvchilar ro\'yxati qaytarildi.',
                examples=[
                    OpenApiExample(
                        'O\'qituvchilar ro\'yxati',
                        value=[
                            {
                                'id': 1,
                                'fullname': 'Alisher Navoiy',
                                'subject': 'Matematika',
                                'image': '/media/teachers/alisher.jpg',
                                'address': 'Toshkent shahar',
                                'bio': 'Matematika fanlari doktori...',
                                'articles_count': 5
                            }
                        ]
                    )
                ]
            )
        }
    )
    def get(self, request):
        """Barcha o'qituvchilarni olish"""
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
class TeacherDetailView(APIView):
    """
    Bitta o'qituvchi tafsilotlarini olish
    """
    
    @extend_schema(
        tags=['O\'qituvchilar'],
        summary="O'qituvchi tafsilotlari",
        description="""
        Berilgan ID bo'yicha o'qituvchining to'liq ma'lumotlarini qaytaradi.
        
        Agar o'qituvchi topilmasa, 404 xato qaytariladi.
        """,
        responses={
            200: OpenApiResponse(
                response=TeacherSerializer,
                description='Muvaffaqiyatli. O\'qituvchi tafsilotlari qaytarildi.',
                examples=[
                    OpenApiExample(
                        'O\'qituvchi tafsiloti',
                        value={
                            'id': 1,
                            'fullname': 'Alisher Navoiy',
                            'subject': 'Matematika',
                            'image': '/media/teachers/alisher.jpg',
                            'address': 'Toshkent shahar, Yunusobod tumani',
                            'bio': 'Matematika fanlari doktori, 20 yillik tajribaga ega...',
                            'articles_count': 5
                        }
                    )
                ]
            ),
            404: OpenApiResponse(
                description='O\'qituvchi topilmadi'
            )
        }
    )
    def get(self, request, pk):
        """Bitta o'qituvchining tafsilotlarini olish"""
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return Response(
                {'error': 'O\'qituvchi topilmadi'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)