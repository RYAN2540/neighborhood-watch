from django.urls import path, re_path
from . import views

urlpatterns=[
    re_path(r'^$',views.home,name = 'home'),
    re_path(r'^email/$',views.email,name = 'email'),
    re_path(r'^create-profile-admin/$',views.create_profile_admin,name = 'create-profile-admin'),
    re_path(r'^create-hood/$',views.create_hood,name = 'create-hood'),
    re_path(r'^update-hood/$',views.update_hood,name = 'update-hood'),
    re_path(r'^my-admin-profile/$',views.my_admin_profile,name = 'my-admin-profile'),
    re_path(r'^add-resident/$',views.add_resident,name = 'add-resident'),
]