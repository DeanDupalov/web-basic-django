# •	GET 'localhost:8000/accounts/' – include the django.contrib.auth.urls
# •	GET 'localhost:8000/accounts/profile/<int:pk>' – create a view that will render the provided 'user_profile.html' with the needed information
# •	POST 'localhost:8000/accounts/profile/<int:pk>' – update the profile picture of the user
# •	GET 'localhost:8000/accounts/signup' – render the provided 'signup.html' with the register form
# •	POST 'localhost:8000/accounts/signup' – register the user and create a user profile (with the default.png as profile picture)
#
from django.urls import path, include

from accounts.views import user_profile, signup_user

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>/', user_profile, name='profile page'),
    path('signup/', signup_user, name='signup user'),


]