from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
	name = models.CharField(max_length=50, unique=True)
	email = models.EmailField(max_length = 100)
	balance = models.DecimalField ( max_digits =5, decimal_places =2, default=0)
	freeze_balance = models.DecimalField ( max_digits =5, decimal_places =2, default=0)
	body = models.TextField(blank=True, null=True, db_index=True)
	date_pub = models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD = 'name'
	EMAIL_FIELD = 'email'
	REQUIRED_FIELDS = ['email']
