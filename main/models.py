from django.db import models
from django.utils import timezone  

# Create your models here.
class AbstractCard(models.Model):
    name = models.CharField(max_length=450)
    text = models.TextField()
    img = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True    


    def __str__(self):
        return self.name


class Banner(AbstractCard):
    img = models.ImageField(upload_to='banner/')

class OurTeam(AbstractCard):
    img = models.ImageField(upload_to='ourteam/')
    profession = models.CharField(max_length=200)

class CommonCraftCard(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='craftsmanship/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True    

    def __str__(self):
        return self.title

class Craftsmanship(CommonCraftCard):
    pass


class Craftsmanshiplist(CommonCraftCard):
    pass  

class SocialMediaLink(models.Model):
    name = models.CharField(max_length=150)
    url = models.URLField()
    icon = models.ImageField(upload_to='social_media_icons/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name