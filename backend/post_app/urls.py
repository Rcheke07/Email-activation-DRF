from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('data/',EmployeeAPI.as_view()),
    path('data/<int:pk>',EmployeeDETAPI.as_view())
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)