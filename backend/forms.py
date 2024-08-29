from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Username',
            'class': 'w-full p-3 rounded border border-gray-300'
        })
    )
     
    password = forms.CharField(  # Corrected to 'password'
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your Password',
            'class': 'w-full p-3 rounded border border-gray-300'
        })
    )

class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your First Name',
            'class': 'w-full p-3 rounded border border-gray-300'
        })
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Last Name',
            'class': 'w-full p-3 rounded border border-gray-300'
        })
    )

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={
            'placeholder': 'Your Date of Birth',
            'type': 'date',
            'class': 'w-full p-3 rounded border border-gray-300'
        })
    )

    gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        widget=forms.Select(attrs={
            'class': 'w-full p-3 rounded border border-gray-300'
        })
    )

    address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Address',
            'class': 'w-full p-3 rounded border border-gray-300'
        })
    )

    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your Email',
            'class': 'w-full p-3 rounded border border-gray-300'
        })
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Username',
            'class': 'w-full p-3 rounded border border-gray-300'
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your Password',
            'class': 'w-full p-3 rounded border border-gray-300'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat Your Password',
            'class': 'w-full p-3 rounded border border-gray-300'
        })
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'date_of_birth', 'gender', 'address', 'email', 'username', 'password1', 'password2')


from .models import Test_request_details

from django import forms
from .models import Test_request_details

class TestRequestDetailsForm(forms.ModelForm):
    class Meta:
        model = Test_request_details
        fields = (
            'test_category',    
            'test_name',        
            'name',             
            'address',          
            'date_of_birth',    
            'state',            
            'phone_number',     
            'pincode',          
            'country',          
            'email_id',         
        )
        widgets = {
            'test_category': forms.Select(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100'
            }),
            'test_name': forms.TextInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter the test name'
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter your full name'
            }),
            'address': forms.Textarea(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter your address',
                'rows': 4,
                'style': 'resize:none;'  # Prevents resizing
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'type': 'date'
            }),
            'state': forms.TextInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter your state'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter your phone number'
            }),
            'pincode': forms.TextInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter your pincode'
            }),
            'country': forms.TextInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter your country'
            }),
            'email_id': forms.EmailInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter your email'
            }),
        }

from .models import UploadTestInformation

class UploadTestInformationForm(forms.ModelForm):
    class Meta:
        model = UploadTestInformation
        fields = (
            'test_category',   
            'test_name',       
            'test_fees',       
            'test_id',         
            'patient_id',      
        )
        widgets = {
            'test_category': forms.Select(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100'
            }),
            'test_name': forms.TextInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter the test name'
            }),
            'test_fees': forms.NumberInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter the test fees'
            }),
            'test_id': forms.TextInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter the test ID'
            }),
            'patient_id': forms.TextInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter the patient ID'
            }),
        }

from .models import upload_result

class UploadResultForm(forms.ModelForm):
    class Meta:
        model = upload_result
        fields = (
            'test_id',
            'patient_id',
            'doctor_name',
            'doctor_fees',
            'day_visited',
            'test_fees',
            'hospital_location',
            'token_number',
        )
        widgets = {
            'test_id': forms.TextInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter the test ID'
            }),
            'patient_id': forms.TextInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter the patient ID'
            }),
            'doctor_name': forms.TextInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter the doctor name'
            }),
            'doctor_fees': forms.NumberInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter the doctor fees'
            }),
            'day_visited': forms.DateTimeInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'type': 'datetime-local',
                'placeholder': 'Enter the day visited'
            }),
            'test_fees': forms.NumberInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter the test fees'
            }),
            'hospital_location': forms.TextInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter the hospital location'
            }),
            'token_number': forms.TextInput(attrs={
                'class': 'w-3/4 py-3 px-4 rounded-lg border bg-gray-100',
                'placeholder': 'Enter the token number'
            }),
        }