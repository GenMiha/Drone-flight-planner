from django.urls import path

from droneSelling import views

urlpatterns = [
    path('', views.TestView.as_view(), name='home'),
    path('signup', views.SingUpView.as_view(), name='signup'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('logout', views.UserLogoutView.as_view(), name='logout'),
    path('request', views.RequestCreateView.as_view(), name='create_request'),
    path('request-history', views.RequestHistoryView.as_view(), name='request_history'),
    path('My park', views.ParkView.as_view(), name='park'),
    path('My park/<int:pk>', views.DroneDetailView.as_view(), name='drone_detail'),
    path('profile', views.UserView.as_view(), name='user'),
    path('profile/edit', views.UserEditView.as_view(), name='user_edit'),
    path('drone-register', views.DroneAddView.as_view(), name='add_drone'),
]
