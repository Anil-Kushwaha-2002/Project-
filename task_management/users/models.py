# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     mobile = models.CharField(max_length=15, unique=True)

#     def __str__(self):
#         return self.username


from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'  # Allows Django to recognize this as the custom user model
