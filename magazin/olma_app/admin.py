from django.contrib import admin
from django.db import models
from django_summernote.widgets import SummernoteWidget

from olma_app.models import Category, Product


# class Admin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.TextField: {'widget': SummernoteWidget},
    # }
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)

