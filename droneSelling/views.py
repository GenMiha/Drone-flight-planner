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
                    'name': drone.name,
                    'description': drone.description,
                    'deployed length': drone.deployed_length,
                    'deployed width': drone.deployed_width,
                    'deployed height': drone.deployed_height,
                    'rolled up length': drone.rolled_up_length,
                    'rolled up width': drone.rolled_up_width,
                    'rolled up height': drone.rolled_up_height,
                    'weight': drone.weight,
                    'max weight': drone.max_weight,
                    'speed': drone.speed,
                    'max speed': drone.max_speed,
                    'flight time with full tank': drone.flight_time_full,
                    'flight time with empty tank': drone.flight_time_empty,
                    'area per flight': drone.area_per_flight,
                    'area per hour': drone.area_per_hour,
                    'tank': drone.tank,
                    'drop size': drone.drop_size,
                    'price': drone.price,
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

    # def form_valid(self, form):
    #     print('anybody')
    #     form.save()
    #     return super().form_valid(form)
        # form.save()
        # data = form.cleaned_data
        # Request.objects.create(user=self.request.user, **data)
        # logger.info('[+] Request created...')
        # print(f"\n\n{Request}\n\n\n")
        # print('1233123')
        # return redirect(self.success_url)


class ResponseCreateView(LoginRequiredMixin, UpdateView):
    template_name = 'response.html'
    form_class = RequestResponseForm

    pass


class RequestHistoryView(LoginRequiredMixin, ListView):
    template_name = 'requestHistory.html'
    model = Request

    # def get_queryset(self):
    #     return Request.objects.filter(user=self.request.user)


class ParkView(LoginRequiredMixin, ListView):
    template_name = 'myPark.html'
    model = Drone

    # def get_queryset(self):
    #     return super().get_queryset().filter(user=self.request.user)


class UserView(LoginRequiredMixin, ListView): #detailview
    template_name = 'user.html'
    model = User

    # def get_queryset(self):
    #     return Request.objects.filter(user=self.request.user)


class UserEditView(LoginRequiredMixin, FormView):
    pass


class FlightView(LoginRequiredMixin, FormView):
    pass


class DroneAddView(LoginRequiredMixin, CreateView):
    template_name = 'addDrone.html'
    form_class = DroneForm
    success_url = reverse_lazy('park')

    #def form_valid(self, form):
    #    print("sdffssd")
    #    super().form_valid(form)
    #   register
