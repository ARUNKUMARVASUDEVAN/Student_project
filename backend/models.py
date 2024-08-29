from django.db import models


# Create your models here.
class TestCategory(models.Model):  # Renamed to PascalCase
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Test_Category'
        
    def __str__(self):
        return self.name


class UploadTestInformation(models.Model):
    test_category = models.ForeignKey(
        TestCategory,  # Referencing the renamed model directly
        related_name='category', 
        on_delete=models.CASCADE
    )
    test_name = models.CharField(max_length=255)
    test_fees = models.FloatField()
    test_id = models.CharField(max_length=255)
    patient_id = models.CharField(max_length=255)
    

    class Meta:
        verbose_name_plural ='Uploaded_test_info'

    def __str__(self):
        return str(self.test_category,self.test_name)

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


