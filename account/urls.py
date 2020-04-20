from django.urls import path
from django.contrib.auth.views import(
    LoginView, LogoutView, PasswordChangeForm, PasswordChangeView,
    PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView,
    PasswordResetCompleteView, PasswordResetDoneView
    )
from . import views

urlpatterns = [
	path('profile/', views.profile, name='profile'), 
    path('registe/', views.register, name="register"),
    path('login/', LoginView.as_view(template_name="account/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('update/', views.profileUpdate, name="profile_update"),
    ##PASSWORD_Change
    path('password-change/',
        PasswordChangeView.as_view(template_name="account/password_change_form.html"),
        name="password_change"
        ),
    path('password_change_done/',
        PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"),
        name="password_change_done"
    ),
    #PASSWORD_REST
    path('password-reset/',
        PasswordResetView.as_view(template_name="account/password_reset_form.html"),
         name="password_reset"
    ),
    path('reset/<uidb64>/<token>/',
            PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html"),
            name='password_reset_confirm'
    ),
    path('password-reset/done/',
        PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
           name="password_reset_done"
    ),
    path('reset/done/',
        PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"),
       name='password_reset_complete'
  ),
]
