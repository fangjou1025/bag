from django import forms
from django.contrib.auth.models import User
from account.models import UserProfile


class UserForm(forms.ModelForm):
    username = forms.CharField(label='會員帳號')
    password = forms.CharField(widget=forms.PasswordInput(), label='會員密碼')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='確認密碼')
    
    class Meta:
        model = User
        fields = ('username', 'password')
        
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password!=password2:
            raise forms.ValidationError('密碼不相符')
        return password2


class UserProfileForm(forms.ModelForm):
    fullName = forms.CharField(max_length=128, label='會員姓名')
    website = forms.CharField(max_length=128, label='個人網址')
    address = forms.CharField(max_length=128, label='住址')
    
    class Meta:
        model = UserProfile
        fields = ('fullName', 'website', 'address')