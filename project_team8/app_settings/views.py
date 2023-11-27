from django.shortcuts import render

# Create your views here.
def show_app_settings(request):
    return render(request, 'app_settings/app_settings.html')
