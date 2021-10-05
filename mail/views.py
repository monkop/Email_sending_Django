from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse, Http404

# Create your views here.
def home(request):
    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            email,
            
            ['mayankmehra428@gmail.com'],
            fail_silently=False 
)
        return render(request, 'home.html', {'name' : name})
    else:
        return render(request,'home.html', {})