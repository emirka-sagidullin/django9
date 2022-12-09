from django import forms


class Registration(forms.Form):
    name = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"class":"name", "placeholder":"Имя"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"email", "placeholder":"javapon@gmail.com"}), required=False)
    password = forms.CharField(widget=forms.TextInput(attrs={"class":"password", "placeholder":"Пароль"}))

class Entry(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"name", "placeholder":"javapon@gmail.com"}))
    password = forms.CharField(widget=forms.TextInput(attrs={"class":"name", "placeholder":"Пароль"}))