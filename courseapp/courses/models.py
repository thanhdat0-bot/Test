from django.db import models
from django.contrib.auth.models import AbstractUser
from unicodedata import category


# Create your models here.
class User(AbstractUser):
    pass

class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=100,unique=True)

class Course(BaseModel):
    subject =models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/%Y/%m')
    category = models.ForeignKey(Category,on_delete=models.PROTECT)

class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/%Y/%m')
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('subject','course')

    def __str__(self):
        return self.subject

class tag(BaseModel):
    name =models.TextField(max_length=255,unique=True)

    def __str__(self):
        return self.name