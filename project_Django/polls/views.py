from django.shortcuts import render
from .models import Question

# Create your views here.

# from django.shortcuts import render
# from .models import Question  # Переконайтеся, що модель імпортована

def question_list(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'question_list.html', context)
