from django.shortcuts import render
from .forms import MessageForm
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

def home(request):
     form = MessageForm()

     if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail('sub',"la","sanya08@zohomail.in",['sanyamahajan08@gmail.com'], fail_silently=False)
            messages.success(request, 'You message was successfully sent!.')
            return render(request, 'base/home.html')
            
     context = {'form': form}
     return render(request, 'base/home.html',context)

def posts(request):
    return render(request, 'base/posts.html')

def post(request):
    return render(request, 'base/post.html')

def profile(request):
    return render(request, 'base/profile.html')