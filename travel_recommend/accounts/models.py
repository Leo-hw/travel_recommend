from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User, UserManager
from django.db import models
from pytz import timezone
from datetime import datetime
# Create your models here.

# user id 와 별개로 nickname = id, name = name, 디비 자동으로 관리를 위해 pk(user_no)/ user_id
# *형식
# user_no/
# #username(id)/pw/pw2/firsname, lastname/jumin/gen/
# # # occupation / 
# class Tuser(AbstractBaseUser, PermissionsMixin):
#     objects = UserManager()

#     email = models.EmailField(verbose_name = "email id", max_length = 64, unique = True)
#     username = models.CharField(max_length=30)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     date_joined = models.DateTimeField(('date joined'), default=datetime.now)

#     EMAIL_FIELD = 'email'
#     USERNAME_FIELD = 'email'

#     def __str__(self):
#         return self.username

#     def get_short_name(self):
#         return self.email

    
# class UserManager(BaseUserManager):
#     use_in_migrations = True 

#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('이메일이 없습니다.')

#         eamil = self.normalize_email(email)
#         user = self.model(email = email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     # 일반 유저 생성
#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)


#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('관리자는 is_staff가 True여야함')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('관리자는 is_superuser가 True여야함')

#         return self._create_user(email, password, **extra_fields)

class Tuser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    user_name = models.CharField(max_length=10, blank=True, null=True)
    user_pwd = models.CharField(max_length=10, blank=True, null=True)
    occupation = models.IntegerField(max_length=50, blank=False, null=False)
    class Meta:
        managed = False
        db_table = 'tuser'

# for connect occupations table
# db 에 따로 occupations table 을 만들어야 하나??
occupations_choices = {
    "1":"others",

}
# class Occupations(models.Model):
#     occupation = models.CharField(max_length=50, choices=occupations_choices, default='1')

class Occupations(models.Model):
    occ = models.CharField(max_length=50, choices=occupations_choices)
    occ_no = models.ForeignKey('Tuser', related_name='tuser', on_delete=models.CASCADE, db_column='occ_no')