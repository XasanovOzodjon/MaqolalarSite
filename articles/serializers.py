from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """
    Maqola ma'lumotlarini serializatsiya qilish uchun serializer
    """
    author_name = serializers.CharField(source='author.fullname', read_only=True, 
                                       help_text="Maqola muallifining to'liq ismi")
    
    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'literature', 'pdf', 'image', 
                  'author', 'author_name', 'is_active', 'published_date']
        extra_kwargs = {
            'title': {
                'help_text': 'Maqola sarlavhasi (maksimal 255 belgi)',
                'required': True
            },
            'description': {
                'help_text': 'Maqolaning qisqacha tavsifi',
                'required': False
            },
            'literature': {
                'help_text': 'Foydalanilgan adabiyotlar ro\'yxati',
                'required': False
            },
            'pdf': {
                'help_text': 'Maqolaning PDF formati (ixtiyoriy)',
                'required': False
            },
            'image': {
                'help_text': 'Maqolaning muqova rasmi (ixtiyoriy)',
                'required': False
            },
            'author': {
                'help_text': 'Maqola muallifi (o\'qituvchi ID si)',
                'required': True
            },
            'is_active': {
                'help_text': 'Maqola faolmi? (standart: true)',
                'required': False
            },
            'published_date': {
                'help_text': 'Maqola nashr etilgan sana (avtomatik)',
                'read_only': True
            }
        }