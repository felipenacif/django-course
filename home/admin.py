from django.contrib import admin
from .models import News
from .models import NewsCategory
from .models import Home

# Register your models here.
admin.site.register(News)
admin.site.register(NewsCategory)
admin.site.register(Home)