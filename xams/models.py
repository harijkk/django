import sys
from django.db import models
from django import forms
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class xam(models.Model):
    name=models.CharField(max_length=100,null=True)
    place=models.CharField(max_length=100)
    adhar=models.CharField(max_length=12)
    gender=models.CharField(max_length=3,name="gender")
    religion=models.CharField(max_length=10)
    bd=models.DateField(max_length=100)
    mail=models.EmailField(max_length=100)
    pic=models.ImageField(upload_to='profiles')
    def __str__(self):
        return self.name    
    def save(self, *args, **kwargs):
        self.pic= self.compressImage(self.pic)
        super(xam, self).save(*args, **kwargs)
    def compressImage(self,pic):
        imageTemproary = Image.open(pic)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (200,230) ) 
        imageTemproaryResized.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        pic = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % pic.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return pic
# Create your models here.
