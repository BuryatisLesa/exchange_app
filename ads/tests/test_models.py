import pytest
from django.contrib.auth.models import User
from ads.models import Ad, ExchangeProposal

@pytest.mark.django_db
def test_ad_creation():
    user = User.objects.create_user(username="user1", password="pass")
    ad = Ad.objects.create(user=user, title="Test", description="Desc", image="image.jpg", category="Категория")
    assert ad.title == "Test"
    assert ad.user == user

@pytest.mark.django_db
def test_exchange_proposal_creation():
    user = User.objects.create_user(username="user2", password="pass")
    ad1 = Ad.objects.create(user=user, title="Ad 1", description="...", image="img.jpg", category="A")
    ad2 = Ad.objects.create(user=user, title="Ad 2", description="...", image="img.jpg", category="B")
    
    proposal = ExchangeProposal.objects.create(user=user, ad_sender=ad1, ad_receiver=ad2)

    assert proposal.user == user
    assert proposal.ad_sender == ad1
    assert proposal.ad_receiver == ad2
