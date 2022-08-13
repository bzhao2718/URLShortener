"""URLShortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from . import views
from .admin import admin_site
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shorturl/<str:url_key>/', views.shorturl, name="shorturl"),
    path('generate/', views.generate, name="generate"),
    path('customize/', views.customize, name="customize"),
    path('user_history/', views.user_url_history, name="user_history"),

    path('accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='accounts')),
    path('accounts/profile/', views.profile, name="profile"),
    path('signup/', views.signup, name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="/"), name="logout"),
    path('', views.generate),
    path('urlshortener/', admin_site.urls),

]
