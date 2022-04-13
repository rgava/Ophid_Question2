from django.db import models
from django.urls import reverse

# Create your models here.
class PagesModel(models.Model):
    name=models.TextField()
    author=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    body=models.TextField(max_length=150,default='',blank=False)
    is_this_male=models.BooleanField(default=False)

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')