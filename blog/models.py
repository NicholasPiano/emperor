#django
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

#local

#util

### MODELS ###
#high and mighty
class EmperorManager(BaseUserManager):
    def create_user(self, display_name, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            display_name=display_name,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, display_name, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            display_name=display_name,
            email=email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Emperor(AbstractBaseUser, PermissionsMixin):
    display_name = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    objects = EmperorManager()

    USERNAME_FIELD = 'email'
    DISPLAY_NAME_FIELD = 'display name'
    REQUIRED_FIELDS = ['display_name','date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __unicode__(self):
        return self.display_name

#meaty goodness
class Blog(models.Model):
    #connections
    emperor = models.ForeignKey(Emperor, related_name='blogs')

    #properties
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class Year(models.Model):
    #connections
    blog = models.ForeignKey(Blog, related_name='years')

    #properties
    index = models.IntegerField()

    def __unicode__(self):
        return self.index

class Month(models.Model):
    #connections
    year = models.ForeignKey(Year, related_name='months')

    #properties
    index = models.IntegerField()

    def __unicode__(self):
        return self.index

class Day(models.Model):
    #connections
    month = models.ForeignKey(Month, related_name='days')

    #properties
    index = models.IntegerField()

    def __unicode__(self):
        return self.index

class Post(models.Model):
    #connections
    blog = models.ForeignKey(Blog, related_name='posts')
    day = models.ForeignKey(Day, related_name='posts')

    #properties
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    index = models.IntegerField() #position in day

    def __unicode__(self):
        return self.title

class PageHit(models.Model):
    #connections
    post = models.ForeignKey(Post, related_name='hits')

    #properties
    date_time = models.DateTimeField(auto_now_add=True)
