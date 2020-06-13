from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

from django.contrib.auth import get_user_model
class MyUserManager(BaseUserManager):
    def create_user(self,email,username,mobile,first_name,last_name,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not mobile:
            raise ValueError("Mobile number is required!")
        elif len(mobile) != 10:
             raise ValueError("Mobile number is not valid!")
        # email = self.normalize_email(email)
        user = self.model(email=self.normalize_email(email),username=username, mobile=mobile,first_name=first_name,last_name=last_name)
        # user=self.create_user(email,mobile=mobile,first_name=first_name,last_name=last_name,password=password,)
        user.set_password(password)
        user.save(using=self._db)
        #user.save()
        return user

    def create_superuser(self,email,username, mobile, first_name,last_name, password):
        if not email:
            raise ValueError('Users must have an email address')
        if not mobile:
            raise ValueError("Mobile number is required!")
        elif len(mobile) != 10:
            raise ValueError("Mobile number is not valid!")

        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            mobile= mobile,
            first_name=first_name,
            last_name=last_name,
            password = password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
       # user.save()
        return user


class MyUserAccount(AbstractBaseUser):
    # username=models.OneToOneField(settings.AUTH_USER_MODEL)
    username = models.CharField('username', max_length=40)
    email = models.EmailField(verbose_name='email_Id', max_length=60, unique=True)

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    mobile = models.CharField(verbose_name="mobile number", max_length=12, unique=True)
    first_name = models.CharField(verbose_name="first name", max_length=50)
    last_name = models.CharField(verbose_name="last name", max_length=50,blank=True)
    is_active = models.BooleanField('active', default=True)
    is_superuser = models.BooleanField("administrator", default=False)
    is_staff = models.BooleanField("staff_user", default=False)
    is_admin = models.BooleanField("staff_user", default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile','first_name','last_name']

    def __str__(self):
        # return str(self.email)
        return self.email
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return self.is_admin
        # return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
