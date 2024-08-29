from django.contrib import admin
from backend.models import UploadTestInformation,TestCategory,Test_request_details,upload_result
# Register your models here.
admin.site.register(TestCategory)
admin.site.register(UploadTestInformation)
admin.site.register(Test_request_details)
admin.site.register(upload_result)