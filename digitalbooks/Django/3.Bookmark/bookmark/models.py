from django.db import models
from django.urls import reverse                     # 모델에서는 reverse, 뷰에서는 reverse_lazy

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)    # 데이터의 필드(종류)를 명시
    url = models.URLField('Site URL')
    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컬럼 종류
    # 2. 제약 사항(몇글자까지)
    # 3. Form의 종류
    # 4. Form에서의 제약사항


    # 매직메서드(__<method name>__형식, 용도가 정해진 메서드)
    # __str__ : 출력형식을 지정하는 메서드
    def __str__(self):
        return "이름 : "+self.site_name+" 주소 : "+self.url

    # 리디렉션 주소 지정(get_absolute_url 방식)
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


# 모델을 만들었다 => 데이터베이스에 어떤  데이터들을 어떤 형태로 넣을지 결정함
# makemigrations : 모델의 변경사항을 추적해서 기록
# -> migration => 데이터베이스에 모델의 내용을 반영(테이블 생성)

# => python manage.py makemigrations bookmark
#   -> python manage.py migrate bookmark
#   -> python manage.py migrate --run-syncdb : 초기 서버 구동시 데이터베이스 생성(<- no such table 에러)