from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index),
    path('create_account_page/',views.create_account_page,name="create_account_page"),
    path('createaccount/',views.createaccount,name="createaccount"),
    path('addemail/',views.addemail,name="addemail"),
    path("loginpage/",views.loginpage,name="loginpage"),
    path('login/',views.login,name="login"),
    path('dashbord/',views.dashbord,name="dashbord"),
    path('transferpage/<int:pk>',views.transferpage,name="transferpage"),
    path('transfermoney/',views.transfermoney,name="transfermoney"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)