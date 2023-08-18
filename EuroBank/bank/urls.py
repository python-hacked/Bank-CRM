from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.register),
    path('registration',views.registration),
    path('userlogin',views.userlogin, name='userlogin'),
    path('login',views.login, name='login'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('verifyotp',views.verifyotp, name='verifyotp'),
    path('verify',views.verify, name='verify'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
