from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUser


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=50, unique=True, null=True)
    username_regex = RegexValidator(regex=r'^[\w.+-]*[a-zA-Z][\w.+-]*\Z',
                                    message="نام کاربری باید حداقل یک حرف داشته باشد و @ پذیرفته نمی شود")
    username = models.CharField(max_length=15, unique=True,
                                help_text=_(
                                    'هشدار نام کاربری باید بین 1 تا 15 حرف باشد و (فقط از حروف، اعداد و . / + / - / _ استفاده شود)'),
                                validators=[username_regex],
                                error_messages={'unique': _("کاربری با آن نام کاربری از قبل وجود دارد."), },
                                null=True, blank=True)
    is_verified = models.BooleanField(default=False, help_text='وضعیت تایید')
    if phone:

        USERNAME_FIELD = 'phone'
        REQUIRED_FIELDS = ['username', 'email']
    elif email:
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['username', 'phone']
    else:
        USERNAME_FIELD = 'username'
        REQUIRED_FIELDS = ['phone', 'email']
    objects = CustomUser()

    def __str__(self):
        return f'{self.email}-{self.phone}'
