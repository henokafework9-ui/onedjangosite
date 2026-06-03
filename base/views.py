from django.shortcuts import render , redirect


# Create your views here.
from .form import LoginForm
from .form import MessageForm

def login(request):
    if request.method == 'POST':
        form =LoginForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home/')
    else:
        form= LoginForm()

        return render (request , 'login.html' , {'form':form})    


def home(request):
    return render(request , 'home.html')


def project(request):
    return render(request , 'project.html')


def skill(request):
    return render(request , "skill.html" ,{})


def bio(request):
    return render(request , 'bio.html',{})


def contact(request):
      if request.method == 'POST':
        form =MessageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('correct/')
      else:
        form= MessageForm()

        return render (request , 'contact.html' , {'form':form})  
def correct(request):
    return render(request , 'correct.html')        


  




