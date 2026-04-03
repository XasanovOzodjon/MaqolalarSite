from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer

class ArticleListView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    

class ArticleDetailView(APIView):
    def get(self, request, pk):
        try:
            article = Article.objects.get(pk=pk).order_by('-published_date')
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    


