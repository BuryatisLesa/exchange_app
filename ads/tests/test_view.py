import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from ads.models import Ad

@pytest.mark.django_db
def test_ad_list_view(client):
    response = client.get(reverse('ads-list'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_ad_create_view(client):
    user = User.objects.create_user(username='testuser', password='pass')
    client.login(username='testuser', password='pass')
    response = client.post(reverse('ad-create'), {
        'title': 'New ad',
        'description': 'desc',
        'image_url': 'test.jpg',
        'category': 'Test',
        'condition': 'new'
    })
    assert response.status_code in (302, 200)  # редирект или рендер формы
