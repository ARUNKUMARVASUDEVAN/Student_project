from django.contrib import admin
from backend.models import UploadTestInformation,TestCategory,Test_request_details,upload_result,onlinepayments,blood_donation,Donor
# Register your models here.
admin.site.register(TestCategory)
admin.site.register(UploadTestInformation)
# admin.py

from django.contrib import admin

class test_request_details_Admin(admin.ModelAdmin):
    list_display = ('test_name', 'is_approved')  # Show these fields in the list view
    actions = ['approve_tests']  # Custom action for approving tests

    def approve_tests(self, request, queryset):
        queryset.update(is_approved=True)  # Approve selected tests
        self.message_user(request, "Selected tests have been approved.")

    approve_tests.short_description = "Approve selected tests"  # Description for the action

# Register the model with the admin site
admin.site.register(Test_request_details, test_request_details_Admin)
admin.site.register(upload_result)
admin.site.register(onlinepayments)
admin.site.register(blood_donation)
admin.site.register(Donor)

