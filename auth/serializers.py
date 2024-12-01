from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser

class TokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user:CustomUser):
        token = super().get_token(user)

        token['username'] = user.username
        token['user_id'] = user.user_id
    

        return token