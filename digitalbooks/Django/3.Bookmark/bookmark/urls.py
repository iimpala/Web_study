from django.urls import path
from .views import *

urlpatterns = [
    # http://127.0.0.1/bookmark/ 이후의 주소
    path("", BookmarkListView.as_view(), name='list'),  # 클라스형 뷰는 .as_view()를 통해 함수형 뷰로 바꾸어서 작성함
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),  # <int:pk> : 글 번호 변수 <-- 컨버터(int, str, slug)
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]
