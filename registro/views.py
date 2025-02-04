from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.

def FirstPage(request):

    return render(request,"first_page.html")

class SignUpView(CreateView):
    form_class= UserCreationForm
    success_url=reverse_lazy("login")
    template_name="registration/signup.html"
