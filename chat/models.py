from django.db import models
from django.contrib.auth.models import User


class Utilisateur(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    # sexe = models.BooleanField(default=False)
    
class Discussion(models.Model):
        nom_discussion = models.CharField(max_length=50 , null=True)

        def __str__(self):
            return self.nom_discussion

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name="sent_messages",null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,related_name="received_messages",null=True)
    message = models.CharField(max_length=150, null=True)
    date_envoye = models.DateTimeField(auto_now_add=True)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE,null=True)
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return self.message 