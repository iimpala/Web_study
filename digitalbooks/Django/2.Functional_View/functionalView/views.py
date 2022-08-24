# view : 기능, 페이지단위
# 화면이 나타나는 뷰 / 화면이 없는 뷰 => (템플릿의 유무)
# 화면이 있든 없든 주소 URL은 있어야 한다

# ==> 뷰 내용(함수, 클래스), URL이 있으면 동작함.(템플릿, 모델은 없어도 동작할 수 있음)

# 뷰의 코드 형식 : 함수형, 클래스형
# 함수형 : 매개변수 = request + a, 모양은 함수, 내가 원하는 대로 동작들을 설계하고 만들고 싶을 때
# 클래스형 : CRUD등 기존에 많이 사용하는 기능을 미리 클래스로 만들어두고 상속받아 사용
# 장고의 제네릭 뷰를 많이 사용함


# 함수형 view
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # 계산, db조회, 수정, 등록
    # 응답 메세지를 만들어서 변환
    html = "<html><body>Hello Django</body></html>"
    return HttpResponse(html)

def welcome(request):
    html = "<html><body>Welcome to Django</body></html>"
    return HttpResponse(html)

def template_test(request):
    # 기본 템플릿 폴더
    # 1. admin 앱
    # 2. 각 앱의 폴더에 있는 tamplates 폴더
    # 3. 사용자 설정 폴더 
    return render(request, 'index.html')

# 함수형 뷰 만들기, 템플릿 만들기, URL연결하기, 브라우저 접속하기