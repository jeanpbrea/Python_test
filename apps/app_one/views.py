from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .models import User
from .models import Poke
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'app_one/index.html')
    
def pokes_show(request):
    context = {
        'all_pokers' : User.objects.all(),
        # 'pokeu' : 
    }
    return render(request, 'app_one/pokes.html', context)

def register(request):
    result = User.objects.reg_validator(request.POST)
    if 'errors' in result:
         for key, value in result['errors'].items():
             messages.error(request, value)
    else: messages.success(request, 'Congratulations you have Registerd!')
    return redirect('/')

def login(request):
      if request.method == "POST":
        users_with_same_email = User.objects.filter(email = request.POST['email'])
        if len(users_with_same_email) > 0:
            print('user with this email exsists')
            the_user = users_with_same_email.first()
            if bcrypt.checkpw(request.POST['password'].encode('utf-8'), the_user.password.encode('utf-8')):
                request.session['user_id'] = the_user.id
                request.session['name'] = the_user.name
                messages.success(request, 'you have logged out,{}!'.format(request.session['name']))
                return redirect('/pokes/')
            else:
                print('passwords do not match')
                messages.error(request, 'Your password is incorrect!')
                return redirect('/')
        else:
            messages.error(request, 'Please type in your login information')
            return redirect('/')
def poke(request):
    User.poker.add(poker = request.POST['user_name']),

    

    return redirect('/pokes/')

def logout_view(request):
    logout(request)
    return redirect('/')
    