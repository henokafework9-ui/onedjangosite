from django.contrib import admin

# Register your models here.
from .models import Message , Login


admin.site.register(Login)
admin.site.register(Message)