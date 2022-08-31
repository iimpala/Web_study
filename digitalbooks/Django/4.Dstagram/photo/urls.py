from django.urls import path
# from django.views.generic.detail import DetailView      # 제네릭 뷰는 urls.py에서 바로 사용가능함
from .views import *
from .models import Photo

app_name = 'photo'  # namespace

urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('detail/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),  # 제네릭 뷰 사용
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
]
