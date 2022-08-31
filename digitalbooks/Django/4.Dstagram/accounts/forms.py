from django.contrib.auth.models import User
from django import forms

# 폼 : 폼 태그 -> HTML의 태그 -> 프론트에서 사용자의 입력을 받는 인터페이스
# 장고의 폼 : HTML의 폼 역할, 데이터베이스에 저장할 내용의 형식, 제약조건

class RegisterForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    # clean_필드명 : 해당 필드에 대한 validation
    def clean_password2(self):
        cd = self.cleaned_data                                      # 안전한 데이터
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwoed not matched!')
        
        return cd['password2']                                      # 관례적으로 해당 필드의 데이터를 리턴