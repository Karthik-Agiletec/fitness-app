"""BreastCancer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from FitnessApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index,name='index'),
    path('login/<str:user_type>/', login_view, name='login'),
    path('register/<str:user_type>/', register_view, name='register'),
    path('create_account/', createAccount, name='create_account'),
    path('login_account/', loginAccount, name='login_account'),
    path('home/', home_view, name='home'),
    path('upload/', upload, name='upload'),
    path('upload_form/', upload_form, name='upload_form'),
    # path('detect_disease/', detect_disease, name='detect_disease'),
    path('predict_form/', predict_form, name='predict_form'),
    path('package/', Package, name='package'),
    path('logout/', logout, name='logout'),
    path('activity/<str:type>/', activity, name='activity'),
    path('activity/<str:act_type>/<str:part>/', activity_part, name='activity_part'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

