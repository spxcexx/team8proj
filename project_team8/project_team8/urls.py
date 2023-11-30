"""
URL configuration for project_team8 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_page.views import *
from contact_page.views import *
from app_settings.views import *
from product_page.views import *
from registration.views import *
from shopping_cart_page.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', show_main_page , name="show_main"),
    path('contact/', show_contact_page , name="show_contact"),
    path('settings/', show_app_settings , name="show_app_settings"),
    path('product/', show_product_page , name="show_product"),
    path('registration/', show_registration , name="show_registration"),
    path('shopping_cart/', show_shopping_cart_page , name="show_shopping_cart"),
    path('login/', show_login, name="show_login"),
    path("logout/", user_logout, name="logout")
]
