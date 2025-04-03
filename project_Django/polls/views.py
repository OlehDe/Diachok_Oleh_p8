from django.shortcuts import render
from .models import Question

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
# Create your views here.

# from django.shortcuts import render
# from .models import Question  # Переконайтеся, що модель імпортована

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
            return redirect('http://127.0.0.1:8000/polls/')  # Змініть 'home' на вашу домашню сторінку
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {"form": form})
