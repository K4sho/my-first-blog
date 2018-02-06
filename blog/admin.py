from django.contrib import admin
from .models import Post,Comment
#Register your models here.

admin.site.register(Post) #Регистрируем нашу модель ,что бы она была доступна на странице администратирования
admin.site.register(Comment)

