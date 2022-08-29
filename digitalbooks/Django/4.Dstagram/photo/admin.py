from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']   # 출력내용
    raw_id_fields = ['author']                              # 직접입력
    list_filter = ['created', 'updated', 'author']          # 필터링 메뉴(보통 시간 or 기간 기준)
    search_fields = ['text', 'created', 'author__username'] # 탐색범위(str형식으로 탐색 => author은 외부키 객체이므로 author__username으로 해야함)
    ordering = ['-updated', '-created']                     # 정렬순서

admin.site.register(Photo, PhotoAdmin)
