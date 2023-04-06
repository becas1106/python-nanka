from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(label='ユーザーID')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput(), min_length=8)

# 複数指定できねえ
# class RegisterForm(forms.Form):
    # user = forms.CharField(label='ユーザーID', min_length=4, max_length=16)
    # password = forms.CharField(label='パスワード', widget=forms.PasswordInput(), min_length=8)
    # re_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput(), min_length=8)
    # last_name = forms.CharField(labe='名字', max_length=8)
    # first_name = forms.CharField(label='名前', max_length=8)