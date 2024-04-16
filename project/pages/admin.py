from django.contrib import admin
from .models import Post
from django.contrib import admin
from django.contrib import admin
from .models import Client
from twilio.rest import Client as TwilioClient
from django.conf import settings
from django.contrib import messages

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'message_type')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)  # Call the original save_model
        # Attempt to send message and provide feedback
        try:
            obj.send_message()  # Send message method
            messages.success(request, "SMS successfully sent.")
        except Exception as e:
            messages.error(request, f"Failed to send SMS: {str(e)}")


admin.site.register(Post)
# Register your models here.


