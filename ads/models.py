from django.db import models
from django.contrib.auth.models import User

#П·	ExchangeProposal: Модель для предложений обмена (id, ad_sender, ad_receiver, comment, status, created_at).


class Ad(models.Model):
    """Модель объявлений"""
    class Condition(models.TextChoices):
        USED = "used", "б/у"
        NEW = "new", "Новое"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField()
    image_url = models.ImageField(upload_to='ads_image/')
    category = models.CharField(max_length=150)
    condition = models.CharField(max_length=20, choices=Condition.choices, default=Condition.NEW)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return f"{self.title}|{self.category}"


class ExchangeProposal(models.Model):
    """Модель для обмена товарами"""
    class Status(models.TextChoices):
        ACCEPTED = "accepted", "принято"
        REJECTED = "rejected", "отклонено"
        WAITING = "waiting", "ожидание"

    ad_sender_id = models.ForeignKey("Ad", on_delete=models.CASCADE, related_name="ad_sender")
    ad_receiver_id = models.ForeignKey("Ad",on_delete=models.CASCADE, related_name="ad_receiver")
    comment = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.WAITING)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return f"{self.ad_sender_id} => {self.ad_receiver_id}"