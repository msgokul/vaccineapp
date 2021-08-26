from django.contrib import messages, auth
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import PersonCreationForm
# Create your views here.
from .models import Taluk


def index(request):


    return render(request,'home.html')

def register (request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1 :
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"This Email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')

    return render (request,'register.html')

def login (request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials!!")
            return redirect('login')
    return render (request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect ('/')

def booking(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'booking.html', {'form': form})

def load_taluks(request):
    district_id = request.GET.get('district_id')
    taluks = Taluk.objects.filter(district_id=district_id).all()
    return render(request, 'options.html', {'taluks': taluks})

def profile(request):
    current_user = request.user
    use_id = current_user.id
    username = current_user.username
    first = current_user.first_name
    last = current_user.last_name
    email = current_user.email
    return render(request,'profile.html',{'use_id':use_id,'username':username,'first':first,'last':last,'email':email})

def result(request):
    current_user = request.user
    use_id = current_user.id
    return render(request,'result.html',{'use_id':use_id})