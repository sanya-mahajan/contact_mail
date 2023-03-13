from django.shortcuts import render
from .forms import MessageForm
from django.contrib import messages
from django.core.mail import send_mail
from sanya import settings

# Create your views here.

def home(request):
     form = MessageForm()

     if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            body = form.cleaned_data.get('body')
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,auth_user=settings.EMAIL_HOST_USER,auth_password=settings.EMAIL_HOST_PASSWORD,
                connection=None,html_message=None
            )


            messages.success(request, 'You message was successfully sent!.')
            return render(request, 'base/home.html')
            
     context = {'form': form}
     return render(request, 'base/home.html',context)
