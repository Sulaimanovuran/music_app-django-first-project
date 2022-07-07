from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title2 = models.SlugField(primary_key=True)

    def __str__(self):
        return self.title2


class Music(models.Model):
    COUNTRY = (
        ('KG', 'Кыргызстан'),
        ('KZ', 'Казахстан')
    )
    author = models.ManyToManyField(User)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= 'music')
    duration = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    country = models.CharField(max_length=30, choices=COUNTRY)

    def __str__(self):
        return f'{self.title} =) {self.category}'