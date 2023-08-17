from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('create/',views.create,name='create'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard_transfer/',views.dashboard_transfer,name='dashboard_transfer'),
    path('dashboard_onlinepass/',views.dashboard_onlinepass,name='dashboard_onlinepass'),
    path('dashboard_more/',views.dashboard_more,name='dashboard_more'),
    path('dashboard_disable/',views.dashboard_disable,name='dashboard_disable'),
    path('dashboard_chargesim/',views.dashboard_chargesim,name='dashboard_chargesim'),
    path('dashboard_bill/',views.dashboard_bill,name='dashboard_bill'),
    path('otp/',views.otp,name='otp'),
    path('registration/', views.registration, name='registration'),
    path('verify-otp/', views.verifyotp),

    path('login_data/', views.login_data, name='login_data'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
