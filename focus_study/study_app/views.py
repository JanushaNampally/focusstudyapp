from django.shortcuts import render, redirect 

# Create your views here.
from .models import StudySession
from django.http import Http404 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login 
from datetime import date
from .models import Goal 


def start_study_session(request):
    if request.method == 'POST':
        course = request.POST['course']
        motivation = request.POST['motivation']
        session = StudySession(course=course, motivation=motivation)
        session.save()
        return redirect('session_started', session_id=session.id)
    
    return render(request, 'study_app/start_session.html')

def session_started(request, session_id):
    session = StudySession.objects.get(id=session_id)
    return render(request, 'study_app/session_started.html', {'session': session})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    
    

def track_streak(request):
    today = date.today()
    goal = Goal.objects.get(user=request.user)
    if goal.target_date == today:
        goal.streak += 1
        goal.save()
        
    return render(request, 'streak_target.html', {'goal': goal})