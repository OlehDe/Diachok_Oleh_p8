from django.shortcuts import render
from .models import Question

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, UserLoginForm

# Create your views here.

def question_list(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'question_list.html', context)




def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('http://127.0.0.1:8000/polls/')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('http://127.0.0.1:8000/polls/')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
