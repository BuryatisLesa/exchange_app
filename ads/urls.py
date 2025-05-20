from django.urls import path
from .views import (
    AdListView,
    AdDetailView,
    AdCreateView,
    AdUpdateView,
    AdDeleteView,
    ExchangeProposalListView,
    ExchangeProposalDetailView,
    ExchangeProposalCreateView,
    ExchangeProposalUpdateView,
    ExchangeProposalDeleteView,
    MySentProposalsView,
    MyReceivedProposalsView,
    ExchangeProposalRespondView,
)

urlpatterns = [
    # Объявления
    path('', AdListView.as_view(), name='ads-list'),
    path('ads/<int:pk>/', AdDetailView.as_view(), name='ad-detail'),
    path('ads/create/', AdCreateView.as_view(), name='ad-create'),
    path('ads/<int:pk>/update/', AdUpdateView.as_view(), name='ad-update'),
    path('ads/<int:pk>/delete/', AdDeleteView.as_view(), name='ad-delete'),

    # Предложения на обмен
    path('proposals/', ExchangeProposalListView.as_view(), name='exchangeproposal-list'),
    path('proposals/<int:pk>/', ExchangeProposalDetailView.as_view(), name='exchangeproposal-detail'),
    path('proposals/create/', ExchangeProposalCreateView.as_view(), name='exchangeproposal-create'),
    path('proposals/<int:pk>/update/', ExchangeProposalUpdateView.as_view(), name='exchangeproposal-update'),
    path('proposals/<int:pk>/delete/', ExchangeProposalDeleteView.as_view(), name='exchangeproposal-delete'),

    # Личные предложения
    path('proposals/sent/', MySentProposalsView.as_view(), name='my-sent-proposals'),
    path('proposals/received/', MyReceivedProposalsView.as_view(), name='my-received-proposals'),

    # Ответ на входящее предложение
    path('proposals/<int:pk>/respond/', ExchangeProposalRespondView.as_view(), name='proposal-respond'),
]
