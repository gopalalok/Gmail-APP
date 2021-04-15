from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Mail(models.Model):
    fromemail = models.EmailField()
    toemail = models.EmailField()
    subject = models.TextField(null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    label = models.TextField(null=True,blank=True)
    dtime = models.DateTimeField(default=timezone.now)

    def mailsave(self):
        self.save()

    @staticmethod
    def isExists(toemail):
        if User.objects.filter(email = toemail):
            return False
        return True

    @staticmethod
    def get_all_mail(user_mail):
        queryset = Mail.objects.all().order_by('-dtime')
        res = [entry for entry in queryset if entry.toemail == user_mail]
        return res

    @staticmethod
    def get_ham_mail(user_mail):
        queryset = Mail.objects.all().order_by('-dtime')
        res = [entry for entry in queryset if entry.toemail == user_mail and entry.label == '[0]']
        return res

    @staticmethod
    def get_spam_mail(user_mail):
        queryset = Mail.objects.all().order_by('-dtime')
        res = [entry for entry in queryset if entry.toemail == user_mail and entry.label == '[1]']
        return res

    @staticmethod
    def get_all_sent_mail(user_mail):
        queryset = Mail.objects.all().order_by('-dtime')
        res = [entry for entry in queryset if entry.fromemail == user_mail]
        return res
            

        