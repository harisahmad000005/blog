from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit 
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField( label='', max_length=50, widget=forms.TextInput(attrs={"class":"form-control  mb-3",'placeholder': 'Username'}))
    password = forms.CharField(label='',widget= forms.PasswordInput(attrs={"class":"form-control mb-3",'placeholder': 'Password'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login', css_class="btn btn-success btn-block mt-3"))
    

  
class RegisterForm(forms.ModelForm):
    username = forms.CharField( label='', max_length=50, widget=forms.TextInput(attrs={"class":"form-control  mb-3",'placeholder': 'Username'}))
    email = forms.EmailField( label='', max_length=50, widget=forms.EmailInput(attrs={"class":"form-control  mb-3",'placeholder': 'Email'}))
    password1 = forms.CharField(label='',widget= forms.PasswordInput(attrs={"class":"form-control mb-3",'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget= forms.PasswordInput(attrs={"class":"form-control ",'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ('email','username')
     
    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords Must Match ')
        return password2
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        user = User.objects.filter(email=email)
        if user:
            raise forms.ValidationError("Email Already Exist")
        return email
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register', css_class="btn btn-success btn-block mt-3"))
    


