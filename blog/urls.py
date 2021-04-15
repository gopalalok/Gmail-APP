from django.urls import path
from users import views
from . import views as bv

urlpatterns = [
    
    path('about/', bv.about, name='blog-about'),
]