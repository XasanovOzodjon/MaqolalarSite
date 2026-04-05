from .models import Teacher
from rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):
    """
    O'qituvchi ma'lumotlarini serializatsiya qilish uchun serializer
    """
    articles_count = serializers.SerializerMethodField(
        help_text="O'qituvchining jami maqolalari soni"
    )
    
    class Meta:
        model = Teacher
        fields = ['id', 'fullname', 'subject', 'image', 'address', 'bio', 'articles_count']
        extra_kwargs = {
            'fullname': {
                'help_text': "O'qituvchining to'liq ismi (maksimal 100 belgi)",
                'required': True
            },
            'subject': {
                'help_text': 'O\'qituvchi o\'qitadigan fan (maksimal 100 belgi)',
                'required': True
            },
            'image': {
                'help_text': "O'qituvchining rasmi (ixtiyoriy)",
                'required': False
            },
            'address': {
                'help_text': "O'qituvchining manzili (ixtiyoriy)",
                'required': False
            },
            'bio': {
                'help_text': "O'qituvchi haqida qisqacha ma'lumot (ixtiyoriy)",
                'required': False
            }
        }
    
    def get_articles_count(self, obj):
        """O'qituvchining maqolalari sonini qaytaradi"""
        return obj.article_set.count()
        