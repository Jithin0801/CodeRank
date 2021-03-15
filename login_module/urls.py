from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static

urlpatterns = [
    path("sign_up/", views.DevSignUpPage, name="DevSignUp"),
    path("login/", views.DevLogIn, name="DevLogIn"),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='login_module/logout.html'), name='DevLogOut'),
    path("profile/", views.DevMyProfile, name="DevMyProfile"),
    path("account_setup/", views.CompleteYourProfile, name="AccountSetUp"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
