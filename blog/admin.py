from django.contrib import admin
from .models import Post
#Register your models here.

admin.site.register(Post) #Регистрируем нашу модель ,что бы она была доступна на странице администратирования

