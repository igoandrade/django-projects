from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    #return HttpResponse('OK')
    return render(request, 'authentication/home.html')


def signup(request):
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        pw1 = request.POST['pw1']
        pw2 = request.POST['pw2']

        myuser = User.objects.create_user(username, email, pw1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Conta criada com sucesso!")

        return redirect('signin')

    return render(request, 'authentication/signup.html')

def signin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Usuário logado com sucesso!")
            print(user.first_name)
            return render(request, 'authentication/home.html', {'user': user})
        else:
            messages.error(request, "Usuário ou senha incorretos!")
            return redirect('signin')


    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso!")
    return redirect('home')