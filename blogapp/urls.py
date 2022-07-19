from .import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index' ),
    path('registration', views.registration, name='registration' ),
    path('login', views.loginuser, name='login' ),
    path('logout', views.logoutuser, name='logout' ),
    path('selected_blog/<id>', views.selected_blog,name='selected_blog'),
    path('upload-blog',views.upload_blog,name='upload-blog')
]