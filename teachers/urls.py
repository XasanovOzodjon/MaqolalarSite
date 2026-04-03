from .views import TeacherListView, TeacherDetailView
from django.urls import path

urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
]