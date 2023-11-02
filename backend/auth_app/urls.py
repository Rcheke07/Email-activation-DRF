from django.urls import path
from .views import *


urlpatterns=[
    path('activate/<str:uidb64>/<str:token>/',Account_activation_API.as_view(),name='activate'),
    path('login/',LoginAPIview.as_view(),name='login_url'),
    path('logout/',logoutf,name='logout_url')
]

