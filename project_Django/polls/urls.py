from django.urls import path
from . import views
from .views import register_view, QuestionListView
from django.urls import path
from . import views



app_name = 'polls'
urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('register/', register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/questions/', QuestionListView.as_view(), name='questions-api'),
]