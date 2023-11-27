from django.shortcuts import render

# Create your views here.

def show_contact_page(request):

    return render(request, 'contact_page/contact_page.html')
