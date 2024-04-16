from django.db import models
from django.contrib.auth.models import User
from django.db import models
from twilio.rest import Client as TwilioClient
from django.conf import settings
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




class Client(models.Model):
    MESSAGE_CHOICES = (
        ('rain', 'rain Warning'),
        ('heat', 'Heat Warning'),
    )
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    message_type = models.CharField(max_length=10, choices=MESSAGE_CHOICES, default='fire')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the real save() method first
        self.send_message()            # Then send the message after saving

    def send_message(self):
        message_texts = {
            'rain': "Digniin Roobab Culus: Waxaa la saadaalinayaa roobab culus oo ka da’aya deegaanka. Fadlan ka fogow meelaha biyuhu maraan iyo daadadka, iskana ilaali safarka aan loo baahnayn. Hubso inaad haysato agabkaaga gurmadka haddii loo baahdo",
            'heat': "Digniin Cimilo Kulul: Waxaa la filayaa in heer kulku si aad ah u kordho maalmaha soo socda. Fadlan iska ilaali qorraxda tooska ah inta u dhexeysa 10ka subaxnimo ilaa 4ta galabnimo, cab biyo badan, oo xiro dhar fudud oo hawo leh",
        }
        message_body = message_texts.get(self.message_type, "No message specified")

        twilio_client = TwilioClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        try:
            message = twilio_client.messages.create(
                body=message_body,
                from_=settings.TWILIO_PHONE_NUMBER,
                to=self.phone_number
            )
            print(f"SMS sent to {self.phone_number}")
        except Exception as e:
            print(f"Failed to send SMS: {str(e)}")

    def __str__(self):
        return self.name