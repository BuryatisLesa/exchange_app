from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    """Модель объявлений"""
    class Condition(models.TextChoices):
        USED = "used", "б/у"
        NEW = "new", "Новое"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='ads_image/')
    category = models.CharField(max_length=150)
    condition = models.CharField(max_length=20, choices=Condition.choices, default=Condition.NEW)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | {self.category}"


class ExchangeProposal(models.Model):
    """Модель для обмена товарами"""
    class Status(models.TextChoices):
        ACCEPTED = "accepted", "принято"
        REJECTED = "rejected", "отклонено"
        WAITING = "waiting", "ожидание"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_sender = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="sent_proposals")
    ad_receiver = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="received_proposals")
    comment = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.WAITING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ad_sender} => {self.ad_receiver}"
