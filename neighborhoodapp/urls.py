from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    re_path(r'^$',views.index,name = 'index'),  
    re_path(r'^sendemail/$',views.send_email,name = 'send-email'),
    re_path(r'^create-admin/$',views.create_admin,name = 'create-admin'),
    re_path(r'^create-hood/$',views.create_hood,name = 'create-hood'),
    re_path(r'^update-hood/$',views.update_hood,name = 'update-hood'),
    re_path(r'^admin-profile/$',views.admin_profile,name = 'admin-profile'),
    re_path(r'^user-profile/$',views.user_profile,name = 'user-profile'),
    re_path(r'^add-occupant/$',views.add_resident,name = 'add-occupant'),
    re_path(r'^delete-hood/$',views.delete_hood,name = 'delete-hood'),
    re_path(r'^add-amenity/$',views.add_amenity,name = 'add-amenity'),
    re_path(r'^add-business/$',views.add_business,name = 'add-business'),
    re_path(r'^delete-occupant-profile/$',views.delete_resident_profile,name = 'delete-occupant-profile'),
    re_path(r'^change-password/$',views.change_password,name = 'change-password'),
    re_path(r'^make-post/$',views.make_post,name = 'make-post'),
    re_path(r'^occupants-list/$',views.residents_list,name = 'occupants-list'),
    re_path(r'^delete-occupant/(\d+)',views.delete_resident,name = 'delete-occupant'),
    re_path(r'^changeprofilephoto/$',views.change_profile_photo,name = 'change-profile-photo'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)