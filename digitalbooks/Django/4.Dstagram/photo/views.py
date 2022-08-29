import imp
from django.shortcuts import render
from .models import Photo

def photo_list(request):
    # 보여줄 사진 데이터
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})    
    # 첫번째 변수는 항상 request, 두번째 변수는 templates아래의 템플릿 파일의 경로, 세번째 변수는 context변수(html과 views.py의 변수를 매핑)