import logging

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView, DetailView, DeleteView, ListView, CreateView

from droneSelling.forms import *
from droneSelling.models import *


logger = logging.getLogger(__name__)


class TestView(LoginRequiredMixin, TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        logger.debug('[+] Home page context is rendering...')
        drones = Drone.objects.all()

        drones_list = []
        for drone in drones:
            drones_list.append(
                {
                    'model': drone.model,
                    'description': drone.description,
                    'status': drone.status

                }
            )

        context = {'Drones': drones_list}
        logger.info('[+] Home page context rendered successfully.')
        return context


class SingUpView(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        logger.info('[+] New user created successfully.')
        return redirect(self.success_url)


class UserLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        print("something")
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    pass


class RequestCreateView(LoginRequiredMixin, CreateView):
    template_name = 'request.html'
    form_class = RequestCreateForm
    success_url = reverse_lazy('request_history')

    # def get_context_data(self, **kwargs):
    #     user_id = self.request.user_id
    #     drone_id = self.request.drone_id



class ResponseCreateView(LoginRequiredMixin, UpdateView):
    template_name = 'response.html'
    form_class = RequestResponseForm
    pass


class RequestHistoryView(LoginRequiredMixin, ListView):
    template_name = 'requestHistory.html'
    model = Request


class ParkView(LoginRequiredMixin, ListView):
    template_name = 'myPark.html'
    model = Drone


class UserView(LoginRequiredMixin, ListView):
    template_name = 'user.html'
    model = User


class UserEditView(LoginRequiredMixin, FormView):
    pass


class FlightView(LoginRequiredMixin, FormView):
    pass


class DroneAddView(LoginRequiredMixin, CreateView):
    template_name = 'addDrone.html'
    form_class = DroneForm
    success_url = reverse_lazy('park')


class DroneDetailView(LoginRequiredMixin, DetailView):
    model = Drone
    template_name = 'drone.html'
    context_object_name = 'drone'
