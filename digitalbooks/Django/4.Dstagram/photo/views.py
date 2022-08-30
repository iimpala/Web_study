import imp
from django.shortcuts import render
from .models import Photo
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect


def photo_list(request):
    # 보여줄 사진 데이터
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})    
    # 첫번째 변수는 항상 request, 두번째 변수는 templates아래의 템플릿 파일의 경로, 세번째 변수는 context변수(html과 views.py의 변수를 매핑)

class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']  # 작성자(author), 작성시간(created) 자동
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id      # 작성자 매칭(외래키 : 필드명_id)

        if form.is_valid():
            # 데이터가 올바르다면 photo인스턴스를 저장
            form.instance.save()
            return redirect('/')
        
        else:
            return self.render_to_response({'form':form})   # 잘못입력했을 때 기존에 작성했던 form을 다시 보여줌

class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'
