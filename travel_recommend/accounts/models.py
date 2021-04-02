from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.

# user id 와 별개로 nickname = id, name = name, 디비 자동으로 관리를 위해 pk(user_no)/ user_id
# *형식
# user_no/
# #username(id)/pw/pw2/firsname, lastname/jumin/gen/
# # occupation / 
