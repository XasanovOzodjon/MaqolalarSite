from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from articles.models import Article
from teachers.models import Teacher

class StatisticsView(APIView):
    def get(self, request):
        
        data = {
            'total_articles': Article.objects.count(),
            'total_teachers': Teacher.objects.count(),
        }
        return Response(data, status=status.HTTP_200_OK)