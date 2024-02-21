from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from droneSelling.models import *


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )


class DroneTypeForm(ModelForm):
    class Meta:
        model = DroneType
        fields = (
            'type',
            'description',
            'rolled_up_state',
            'deployed_state'
        )


class RequestCreateForm(ModelForm):
    class Meta:
        model = Request
        fields = (
            'description',
            'user_id',
            'drone_id'
        )


class RequestResponseForm(ModelForm):
    class Meta:
        model = Request
        fields = (
            'response',
        )


class RepairResponseForm(ModelForm):
    class Meta:
        model = Request
        fields = (
            'response',
            'status',
            'summary'
        )


class DroneForm(ModelForm):
    class Meta:
        model = Drone
        fields = (
            'model',
            'serial_number',
            'description',
            'manufacture_date',
            'registration_date',
            'status',
            'drone_type_id',
            'user_id'
        )


class TechCardForm(ModelForm):
    class Meta:
        model = TechCard
        fields = (
            'description',
            'drone_type_id'
        )


class TechOperationForm(ModelForm):
    class Meta:
        model = TechOperation
        fields = (
            'tech_card_id',
            'description',
            'html_content',
            'instruction_order'
        )


class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = (
            'drone_id',
            'start',
            'duration',
            'status',
        )


class CompletedTechCardForm(ModelForm):
    class Meta:
        model = CompletedTechCard
        fields = (
            'tech_card_id',
            'perform_date',
        )


class CompletedTechOperationForm(ModelForm):
    class Meta:
        model = CompletedTechOperation
        fields = (
            'comp_tech_card_id',
            'tech_oper_id',
            'perform_date',
            'done_confirm_date'
        )




# class ServiceForm(ModelForm):
#     class Meta:
#         model = Service
#         fields = (
#             'type',
#             'criteria'
#         )
