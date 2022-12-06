import logging

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView, DetailView, DeleteView, ListView

from uavSelling.forms import SignUpForm
from uavSelling.models import *


logger = logging.getLogger(__name__)


class TestView(LoginRequiredMixin, TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        logger.debug('[+] Home page context is rendering...')
        uavs = UAV.objects.all()

        uavs_list = []
        for uav in uavs:
            uavs_list.append(
                {
                    'name': uav.name,
                    'description': uav.description,
                    'deployed length': uav.deployed_length,
                    'deployed width': uav.deployed_width,
                    'deployed height': uav.deployed_height,
                    'rolled up length': uav.rolled_up_length,
                    'rolled up width': uav.rolled_up_width,
                    'rolled up height': uav.rolled_up_height,
                    'weight': uav.weight,
                    'max weight': uav.max_weight,
                    'speed': uav.speed,
                    'max speed': uav.max_speed,
                    'flight time with full tank': uav.flight_time_full,
                    'flight time with empty tank': uav.flight_time_empty,
                    'area per flight': uav.area_per_flight,
                    'area per hour': uav.area_per_hour,
                    'tank': uav.tank,
                    'drop size': uav.drop_size,
                    'price': uav.price,
                    'status': uav.status

                }
            )

        context = {'UAVs': uavs_list}
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


class UserLogoutView(LogoutView):
    pass


class RequestCreateView(LoginRequiredMixin, FormView):
    template_name = ''

    def form_valid(self, form):
        request = Request
        pass




class RequestHistoryView(LoginRequiredMixin, ListView):
    template_name = 'requestHistory.html'

    def get_queryset(self):
        return Request.objects
