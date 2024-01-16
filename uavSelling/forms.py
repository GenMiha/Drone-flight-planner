from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from uavSelling.models import User, Request, TechService, Repairing, PartReplace, SimpleRequest


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class RequestCreateForm(ModelForm):
    class Meta:
        model = SimpleRequest
        fields = ('request_goal', )


