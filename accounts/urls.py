from django.urls import path, include

from .views import (
    UserRegistrationView,
    UserLoginView,
    UserListView,
    UserProfileView,
    UserRetrieveView,
)


urlpatterns = [ 
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),

    path('auth/', include('rest_framework.urls')),
    path('', UserListView.as_view(), name="user-list"),
    path('<int:pk>/', UserRetrieveView.as_view(), name='user-detail'),
    path('profile/', UserProfileView.as_view(), name='profile'),


]

