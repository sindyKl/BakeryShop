from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('register/', views.UserRegistration.as_view(), name='register'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('signout/', views.signout, name='signout'),
    path('password_change/', views.ChangePassword.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    
    # Forget Password
    path('password_reset/', name='password_reset', view=auth_views.PasswordResetView.as_view(
        template_name='users/password_reset/password_reset.html',
        subject_template_name='users/password_reset/password_reset_subject.txt',
        email_template_name='users/password_reset/password_reset_email.html'
    )),
    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset/password_reset_done.html'), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset/password_reset_confirm.html'), name='password_reset_confirm'),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset/password_reset_complete.html'), name='password_reset_complete'),
]