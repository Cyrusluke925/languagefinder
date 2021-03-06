# Create your views here.
from django.shortcuts import render, redirect
from languagefinder.forms import UserForm, ProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import User, Marker

# Create your views here.

def home(request):
    return render(request, 'languagefinder/home.html')


def sendJsonMarkers(request):
    markers = list(Marker.objects.all().values('user', 'title', 'latitude', 'longitude', 'symbol'))
    return JsonResponse({'markers': markers})



def hello(request):
    print('hELLOOOOOOOO')
    return render(request, 'languagefinder/addtomap.html')



@login_required
def user_logout(request):
    logout(request)
    return redirect('home')
    


def addtomap(request):
    print('HELLOOOOOOOOOOO')
    return render(request, 'languagefinder/login.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form= UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            login(request, user)
            return redirect('home')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'languagefinder/register.html', {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse('Your account is inactive')
        else:
            return HttpResponse("Invalid login credentials")
    else:
        
        return render(request, 'languagefinder/login.html', {})




@login_required
@csrf_exempt
def new_language(request):
    print('enters new language function')
    if request.method == "POST":
        # if form.is_valid:
        #   post = form.save(commit=False)
        print(request.user)
        print('THIS IS THE DATA THAT IS SENT OVER')
        # print(request.body)
        title = request.POST.get('title')
        latitude = request.POST.get('latitude')
        symbol = request.POST.get('symbol')
        longitude = request.POST.get('longitude')
        print(request.POST.get('name'))
        marker = Marker(title = title, latitude = latitude, longitude = longitude, symbol = symbol, user = request.user)
        marker.save()
        markers = list(Marker.objects.all().values('title', 'latitude', 'longitude', 'symbol', 'user'))

        return JsonResponse({'markers': markers})


@login_required
def view_profile(request):
    markers = Marker.objects.all()
    markers_list = []
    for marker in markers:
        if marker.user == request.user:
            markers_list.append(marker)
    user = request.user

    return render(request, 'languagefinder/profile.html', {'user': user, 'markers_list': markers_list})


