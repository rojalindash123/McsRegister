from django.conf.urls import url
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
   # url('users/', views.UserCreate.as_view(), name='account-create'),
     path('',views.welcome),
     path('register/',views.register,name='register'),
     # path('status/',views.status),
     path('login_user/',views.login_user,name='login_user'),
     path('logout/',views.logout,name='logout'),

     path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
     path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
     path('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
     path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_sent_done.html"), name="password_reset_complete"),

]