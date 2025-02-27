from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import DonorView, RecipientView
from django.shortcuts import render

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('hospitals/', views.hospitals, name='hospitals'),
    path('contact/', views.contact, name='contact'),
    path("donor/", DonorView.as_view(), name="donor"),
    path("recipient/", RecipientView.as_view(), name="recipient"),
    path("success/", lambda request: render(request, "manager/success.html"), name="success"), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)