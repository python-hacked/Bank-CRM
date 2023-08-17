from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index),
    path('create_account_page/',views.create_account_page,name="create_account_page"),
    path('createaccount/',views.createaccount,name="createaccount"),
    path('addemail/',views.addemail,name="addemail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)