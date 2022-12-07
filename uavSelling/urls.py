from django.urls import path

from uavSelling import views

urlpatterns = [
    path('', views.TestView.as_view(), name='home'),
    path('signup', views.SingUpView.as_view(), name='signup'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('logout', views.UserLogoutView.as_view(), name='logout'),
    path('request-history', views.RequestHistoryView.as_view(), name='request_history'),
]
