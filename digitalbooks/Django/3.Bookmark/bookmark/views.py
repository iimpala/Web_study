from django.shortcuts import render

# CRUD : Create, Read, Update, Delete. 웹페이지의 기본 요소

# List
# 웹 페이지에 접속 = 페이지를 본다
# URL을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다 -> 응답
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark                # 어떤 모델에 대한 제네릭 뷰인지 지정

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']       # 어떤 필드를 변경할 것인지 지정 (modify view에서 필수항목) 
    success_url = reverse_lazy('list')  # 리디렉션 주소 지정. reverse_lazy : url을 만들어주는 함수 <--success url 방식
    template_name_suffix = '_create'    # html파일 이름

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
    