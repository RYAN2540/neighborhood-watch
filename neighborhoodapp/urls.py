from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sendemail/', views.send_email, name='send-email'),
    path('create-admin/', views.create_admin, name='create-admin'),
    path('create-hood/', views.create_hood, name='create-hood'),
    path('update-hood/', views.update_hood, name='update-hood'),
    path('admin-profile/', views.admin_profile, name='admin-profile'),
    path('user-profile/', views.user_profile, name='user-profile'),
    path('add-occupant/', views.add_resident, name='add-occupant'),
    path('delete-hood/', views.delete_hood, name='delete-hood'),
    path('add-amenity/', views.add_amenity, name='add-amenity'),
    path('add-business/', views.add_business, name='add-business'),
    path('delete-occupant-profile/',
         views.delete_resident_profile, name='delete-occupant-profile'),
    path('change-password/', views.change_password,
         name='change-password'),
    path('make-post/', views.make_post, name='make-post'),
    path('occupants-list/', views.residents_list, name='occupants-list'),
    re_path(r'^delete-occupant/(\d+)/$',
            views.delete_resident, name='delete-occupant'),
    path('changeprofilephoto/', views.change_profile_photo,
         name='change-profile-photo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
