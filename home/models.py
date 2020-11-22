from django.db import models

# Classe Home
class Home(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.CharField(max_length=4000)

# Classe News Category
class NewsCategory(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.CharField(max_length=2000, blank=True)
    menu_position = models.IntegerField()

# Classe News
class News(models.Model):
    STATUS = (
        ('0', 'Draft'),
        ('1', 'Active'),
        ('2', 'Inactive'),
    )
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    abstract = models.CharField(max_length=4000, null=True, blank=True)
    text = models.TextField(null=False)
    lastsaved_date = models.DateField()
    release_date = models.DateField(null=True, blank=True)
    expire_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS)

    
