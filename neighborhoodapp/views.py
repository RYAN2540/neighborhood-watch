import folium
import random
import string
from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .models import Neighbourhood, Admin, Occupant, Business, Amenity, Post
from django.contrib.auth.decorators import login_required
from .email import send_signup_email_admin, send_signup_email_resident
from .forms import AdminProfileForm, NeighbourhoodForm, AddResidentForm, PostForm, BusinessForm, AmenityForm, ChangePasswordForm
from django.contrib.auth import authenticate
from django.contrib import messages

@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    admin= None
    try:
        admin = Admin.objects.get(user = current_user)
    except Admin.DoesNotExist:
        pass

    occupant = None
    try:
        occupant = Occupant.objects.get(user = current_user)
    except Occupant.DoesNotExist:
        pass

    if admin:
        return redirect(admin)
    elif occupant:
        return redirect(user_profile)
    else:
        raise Http404

@login_required(login_url='/accounts/login/')
def send_email(request):
    current_user = request.user
    email = current_user.email
    name = current_user.username
    send_signup_email_admin(name, email)
    return redirect(create_admin)


@login_required(login_url='/accounts/login/')
def create_admin(request):
    current_user = request.user
    if request.method == 'POST':
        form = AdminProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect(create_hood)

    else:
        form = AdminProfileForm()

    title = "Admin profile "
    return render(request, 'create-admin.html', {"form": form, "title": title})


@login_required(login_url='/accounts/login/')
def create_hood(request):
    current_user = request.user
    try:
        admin = Admin.objects.get(user = current_user)
    except Admin.DoesNotExist:
        raise Http404()

    my_hood = None
    try:
        my_hood = Neighbourhood.objects.get(admin = admin)
    except Neighbourhood.DoesNotExist:
        pass

    if my_hood:
        return redirect(my_admin)

    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = admin
            hood.save()
        return redirect(my_admin)

    else:
        form = NeighbourhoodForm()

    title = "Create Hood"
    return render(request, 'create_hood.html', {"form": form, "title": title})


@login_required(login_url='/accounts/login/')
def my_admin(request):
    current_user = request.user
    try:
        admin = admin.objects.get(this_user = current_user)
    except admin.DoesNotExist:
        raise Http404()

    my_hood =None
    try:
        my_hood = Neighbourhood.objects.get(admin = admin)
    except Neighbourhood.DoesNotExist:
        raise Http404()

    if my_hood:
        longitude = my_hood.location[0]
        latitude = my_hood.location[1]


    m = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker([latitude,longitude],
                    popup='<h5>My neighbourhood.</h5>',
                    tooltip=f'{my_hood.hood_name}',
                    icon=folium.Icon(icon='glyphicon-home', color='blue')).add_to(m),
    folium.CircleMarker(
        location=[latitude, longitude],
        radius=50,
        popup=f'{my_hood.hood_name}',
        color='#428bca',
        fill=True,
        fill_color='#428bca'
    ).add_to(m),

    map_page = m._repr_html_()    

    title = admin.this_user.username
    return render(request, 'my-admin-profile.html', {"profile": admin, "title": title, "hood": my_hood, "map_page":map_page})


@login_required(login_url='/accounts/login/')
def add_resident(request):
    current_user = request.user
    try:
        admin = admin.objects.get(this_user = current_user)
    except admin.DoesNotExist:
        raise Http404()

    try:
        my_hood = Neighbourhood.objects.get(admin = admin)
    except Neighbourhood.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        form = AddResidentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            this_resident =User.objects.create_user(username, email, password)
            resident_profile = Resident_Profile(full_name=name, this_user=this_resident, username=username, hood=my_hood)
            resident_profile.save()
            my_hood.occupants_count = len(Resident_Profile.objects.filter(hood = my_hood))
            send_signup_email_resident(name, username, password,admin.full_name, my_hood.hood_name, email)

        return redirect(my_admin)

    else:
        form = AddResidentForm()

    title = "Add resident"
    return render(request, 'add-resident.html', {"form": form, "title": title})


@login_required(login_url='/accounts/login/')
def update_hood(request):
    current_user = request.user
    try:
        admin = admin.objects.get(this_user = current_user)
    except admin.DoesNotExist:
        raise Http404()

    try:
        my_hood = Neighbourhood.objects.get(admin = admin)
    except Neighbourhood.DoesNotExist:
        pass

    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST)
        if form.is_valid():
            my_hood.hood_name = form.cleaned_data['hood_name']
            my_hood.location = form.cleaned_data['location']
            my_hood.save()
        return redirect(my_admin)

    else:
        form = NeighbourhoodForm()

    title = "Update Hood"
    return render(request, 'update-hood.html', {"form": form, "title": title})



@login_required(login_url='/accounts/login/')
def delete_hood(request):
    current_user = request.user
    try:
        admin = admin.objects.get(this_user = current_user)
    except admin.DoesNotExist:
        raise Http404()

    try:
        my_hood = Neighbourhood.objects.get(admin = admin)
    except Neighbourhood.DoesNotExist:
        pass

    admin.delete()
    current_user.delete()

    return redirect(home)
