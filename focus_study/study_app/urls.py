from django.urls import path 
from . import views 

urlpatterns = [
    path('start/', views.start_study_session, name='start_session'),
    path('session/<int:session_id>/', views.session_started, name='session_started'),
]