from django.db import models


# Create your models here.
class TestCategory(models.Model):  # Renamed to PascalCase
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Test_Category'
        
    def __str__(self):
        return self.name


class UploadTestInformation(models.Model):
    test_category = models.CharField(max_length=100)
    test_name = models.CharField(max_length=100)
    test_id = models.CharField(max_length=100)
    test_fees = models.CharField(max_length=100)
    test_description = models.TextField()
    test_duration = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return self.test_name


from django.db import models
from django.utils import timezone

class Test_request_details(models.Model):
    test_category = models.ForeignKey(
        TestCategory,  
        related_name='category1', 
        on_delete=models.CASCADE
    )
    
    test_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField()
    state = models.CharField(max_length=255, default='Tamilnadu')
    phone_number = models.IntegerField(default=9999999999)
    pincode = models.IntegerField(default=678678)
    country = models.CharField(max_length=255, default='India')
    email_id = models.EmailField(default='arun@gmail.com')
    time_requested = models.DateTimeField(default=timezone.now)  # New field to store the time of request
    is_approved=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Test Request detail'

    def __str__(self):
        return str(self.name)


class upload_result(models.Model):
    test_id=models.CharField(max_length=10)
    patient_id=models.CharField(max_length=10)
    result_upload_date=models.DateTimeField(auto_now_add=True)
    doctor_name=models.CharField(max_length=20)
    doctor_fees=models.IntegerField()
    day_visited=models.DateTimeField()
    test_fees=models.IntegerField()
    hospital_location=models.CharField(max_length=30)
    token_number=models.CharField(max_length=25)
    
    class Meta:
        verbose_name_plural = 'upload_result'

    def __str__(self):
        return str(self.patient_id)
    

class onlinepayments(models.Model):
    upi=models.IntegerField()
    amount=models.FloatField()

    class Meta:
        verbose_name_plural = 'onlinepayment'

    def __str__(self):
        return str(self.amount)
    

class blood_donation(models.Model):
    patient_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    
    blood_group = models.CharField(max_length=255, choices=BLOOD_GROUP_CHOICES, default='A+')
    donation_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Blood Donations'
    
    def __str__(self):
        return self.blood_group


class Donor(models.Model):
    donor_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_group = models.CharField(max_length=255, choices=BLOOD_GROUP_CHOICES, default='A+')

    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=500)
    units = models.PositiveIntegerField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.donor_name







