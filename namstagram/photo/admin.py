from django.contrib import admin

from .models import Photo

# 편리하게 하기 위해서 관리자 목록 화면을 바꾸었음
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','author','created','updated']
    raw_id_fields = ['author']
    list_filter = ['created','updated','author']
    search_fields = ['text','created']
    ordering = ['-updated','-created']

admin.site.register(Photo, PhotoAdmin)
