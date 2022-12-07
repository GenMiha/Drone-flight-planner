from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from uavSelling.models import User, Request, TechService, Repairing, PartReplace


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class RequestCreateForm(ModelForm):
    class Meta:
        model = Request
        fields = ('request_type', 'request_goal', 'user', 'status')


class TechServiceCreateForm(ModelForm):
    class Meta:
        model = TechService
        fields = ('request', 'contract')


class PartReplaceCreateForm(ModelForm):
    class Meta:
        model = PartReplace
        fields = ('request', 'parts')


class RepairingCreateForm(ModelForm):
    class Meta:
        model = Repairing
        fields = ('request', 'contract', 'parts')

