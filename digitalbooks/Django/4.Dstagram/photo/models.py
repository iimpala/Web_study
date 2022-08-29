from distutils.command.upload import upload
import imp
from django.db import models
from django.urls import reverse


from django.contrib.auth.models import User

# 외래키(ForeignKey) : User테이블에서 해당 유저를 찾을 수 있는 주키        <- 내 친구가 가지고 있는 우리집 열쇠
# 주키(PrimartKey) : (User테이블) 1 admin x x x x x                     <- 내가 가지고있는 우리집 열쇠

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')  # on_delete : 작성자계정이 삭제되면 어떻게할거임? // related_name : user에서 photo를 참조하는 이름
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png') # upload_to : 사진을 업로드 할 경로
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)   # auto_now_add : db에 데이터가 등록될 때 현재시간을 등록
    updated = models.DateTimeField(auto_now=True)       # auto_now : db에 데이터가 등록되거나 수정될 때 현재시간을 등록

    class Meta:                     # 옵션을 설정하는 클래스
        ordering = ['-updated']    # updated 필드를 기준으로 정렬(- : 내림차순)

    def __str__(self):              # 관리자 페이지에서 인스턴스의 정보를 보일 때 출력될 내용
        return self.author.username + ' ' + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_datail', args=[self.id])