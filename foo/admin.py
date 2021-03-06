from django.contrib import admin
from .models import Foo


@admin.register(Foo)
class FooAdmin(admin.ModelAdmin):
    list_display = ['id', 'foo', 'user']