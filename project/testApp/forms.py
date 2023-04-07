from django import forms
from .models import User

class LoginForm(forms.Form):
    user = forms.CharField(label='ユーザーID')
    password = forms.CharField(label='パスワード', min_length=8)
    # password = forms.CharField(label='パスワード', widget=forms.PasswordInput(), min_length=8)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'password', 'first_name', 'last_name']
        labels={
            'user_id': 'ユーザーID',
            'password': 'パスワード',
            'first_name': '苗字',
            'last_name': '名前',
        }
        #TODO モデルにない行の表示方法とフォームの種類変更方法(パスワード隠したい)
        #TODO パスワード平文じゃなくハッシュで保存する方法