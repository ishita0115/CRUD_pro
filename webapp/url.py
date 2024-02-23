from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name=''),
    path("register/",views.register,name='register'),
    path('my-login/',views.my_login,name='my-login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path("signout/",views.signout,name='logout'),
    path('create-record/',views.create_record,name='create-record'),
    path('update-record/<int:pk>',views.update_record,name='update-record'),
    path('record-view/<int:pk>',views.singular_record,name='view-record'),
    path('delete-record/<int:pk>',views.delete_record,name='delete-record')
]