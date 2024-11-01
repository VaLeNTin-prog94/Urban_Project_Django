from django.contrib import admin
from .models import *

admin.site.register(Post)


# from .models import Category,News
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display=('name',)
#     search_fields = ('name',)
#
# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('title','category','created_at','is_published')
#     list_filter = ('category','is_published')
#     search_fields = ('title','content')
#     list_per_page = 10
#
#     fieldsets = (
#         (None,{
#             'fields':('title','content','category')
#         }),
#         ('Дополнительные настройки',{
#         'fields':('is_published','created_at','update_at')
#         }),
#     )
#     readonly_fields=('created_at','update_at')