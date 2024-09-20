from django.shortcuts import render,redirect
from backend.models import Test_request_details
from .forms import SignupForm,TestRequestDetailsForm

# Required login
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_page(request):
    test_request_details = Test_request_details.objects.all()
    return render(request, 'backend/GCLRAShomepage.html', {'test_request_details': test_request_details})

def user_registration(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/authentication')# Assuming you have a 'login' view
    else:
        form = SignupForm()
    
    return render(request,'backend/User_registration_page.html', {'form': form})

def authentication(request):
    return render(request,'backend/authentication.html')

def otp(request):
    upi_id = request.GET.get('upiId')
    amount = request.GET.get('amount')
    return render(request, 'backend/otp.html', {'upi_id': upi_id, 'amount': amount})

@login_required
def test_request(request):
    if request.method == 'POST':
        form = TestRequestDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            test_request_details = form.save(commit=False)
            test_request_details.created_by = request.user
            test_request_details.save()
            return redirect('/home_page')  # Redirect to the appropriate page after saving
    else:
        form = TestRequestDetailsForm()

    return render(request, 'backend/test_request.html', {'form': form})

def test_report(request):
    tests = UploadTestInformation.objects.all()
    context = {
        'tests': tests,
    }
    return render(request,'backend/test_report.html',context)

from .forms import UploadTestInformationForm

# views.py
from django.shortcuts import render, redirect
from .forms import UploadTestInformationForm  # Import your form
from .models import UploadTestInformation  # Import your model

def upload_test_information(request):
    if request.method == "POST":
        print(request.POST)  # Print the POST data for debugging
        form = UploadTestInformationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('/home_page')  # Redirect to a success page
        else:
            print(form.errors)  # Print errors for debugging
    else:
        form = UploadTestInformationForm()

    return render(request, 'backend/upload_test_information.html', {'form': form})

from .forms import OnlinePaymentForm

def payment(request):
    if request.method == 'POST':
        form = OnlinePaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_confirmation')  # Redirect after successful payment
    else:
        form = OnlinePaymentForm()
    
    return render(request, 'backend/payment.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import BloodDonationForm, DonorForm

def bloodbank(request):
    if request.method == 'POST':
        donor_form = DonorForm(request.POST)
        blood_donation_form = BloodDonationForm(request.POST)
        
        if donor_form.is_valid():
            donor_form.save()
            return redirect('/dashboard')  # Redirect to a success page
        
        elif blood_donation_form.is_valid():
            blood_donation_form.save()
            return redirect('/dashboard')  # Redirect to a success page
    
    else:
        donor_form = DonorForm()
        blood_donation_form = BloodDonationForm()
    
    return render(request, 'backend/Bloodbank.html', {
        'donor_form': donor_form,
        'blood_donation_form': blood_donation_form,
    })


from .forms import UploadResultForm

def upload_results(request):
    if request.method == 'POST':
        form = UploadResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')  
    else:
        form = UploadResultForm()

    return render(request, 'backend/upload_result.html', {'form': form})



from backend.models import Test_request_details,TestCategory,UploadTestInformation,blood_donation,Donor,onlinepayments,upload_result


from .models import Test_request_details
@login_required
def dashboard_view(request):
    context = {
        'latest_tests': Test_request_details.objects.all()[:5],  # Query for the latest test details
        'test_category_count': TestCategory.objects.count(),
        'upload_test_info_count': UploadTestInformation.objects.count(),
        'test_request_count': Test_request_details.objects.count(),
        'upload_result_count': upload_result.objects.count(),
        'blood_donation_count': blood_donation.objects.count(),
        'donor_count': Donor.objects.count(),
        'online_payment_count': onlinepayments.objects.count(),
    }
    return render(request, 'backend/dashboard.html', context)