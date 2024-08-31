from django.urls import path,include
from .views import *
urlpatterns=[

    path("accounts/",include('django.contrib.auth.urls')),
    path("",FirstPage,name="first_page"),
    path("signup/",SignUpView.as_view(),name="signup")

]