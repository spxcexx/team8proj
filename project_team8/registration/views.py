from django.shortcuts import render

# Create your views here.
def show_registration(request):
    return render(request, 'registration/registration.html')
