from django.urls import path, re_path
from . import views

urlpatterns=[
    re_path(r'^$',views.home,name = 'home'),
    re_path(r'^email/$',views.email,name = 'email'),
    re_path(r'^create_profile_admin/$',views.create_profile_admin,name='create_profile_admin'),
]