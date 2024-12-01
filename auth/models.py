import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class AuthManager(BaseUserManager):
    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        
        if other_fields.get('is_staff')  is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned is_superuser=True')
        
        super_user = self.create_user(email,username, password, **other_fields)
        
        return super_user
    
    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(_('The email must be provided'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        
        return user
    
class CustomUser(AbstractBaseUser):
    user_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    objects = AuthManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'username']
    
    class Meta:
        db_table = 'USERS'
        
    def __str__(self) -> str:
        return f'{self.username}'
