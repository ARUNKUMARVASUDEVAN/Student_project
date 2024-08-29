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

def upload_test_information(request):
    if request.method == 'POST':
            form = UploadTestInformationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/dashboard')  # Redirect to a success page after saving
    else:
            form = UploadTestInformationForm()
    return render(request, 'backend/upload_test_information.html', {'form': form})

def payment(request):
    return render(request,'backend/payment.html')

from .forms import UploadResultForm

def upload_result(request):
    if request.method == 'POST':
        form = UploadResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')  
    else:
        form = UploadResultForm()

    return render(request, 'backend/upload_result.html', {'form': form})



from backend.models import Test_request_details,TestCategory,UploadTestInformation


from .models import Test_request_details
@login_required
def dashboard_view(request):
    context = {
        'test_category_count': TestCategory.objects.count(),
        'upload_test_info_count': UploadTestInformation.objects.count(),
        'test_request_count': Test_request_details.objects.count(),
        'latest_tests': UploadTestInformation.objects.order_by('-id')[:5],  # Latest 5 tests
    }
    return render(request, 'backend/dashboard.html', context)
