from .models import Ad, ExchangeProposal
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .forms import AdForm, ExchangeProposalForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, get_object_or_404


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class ExchangeProposalRespondView(LoginRequiredMixin, View):
    def post(self, request, pk):
        proposal = get_object_or_404(ExchangeProposal, pk=pk)

        # Только владелец ad_receiver может отвечать
        if proposal.ad_receiver.user != request.user:
            raise PermissionDenied

        status = request.POST.get("status")
        if status in ["accepted", "rejected"]:
            proposal.status = status
            proposal.save()
            messages.success(request, f"Предложение {'принято' if status == 'accepted' else 'отклонено'}.")
        return redirect("my-received-proposals")

class MySentProposalsView(LoginRequiredMixin, ListView):
    model = ExchangeProposal
    template_name = 'ads/exchangeproposal_list.html'
    context_object_name = 'exchangeproposals'

    def get_queryset(self):
        return ExchangeProposal.objects.filter(user=self.request.user).order_by('-created_at')


class MyReceivedProposalsView(LoginRequiredMixin, ListView):
    model = ExchangeProposal
    template_name = 'ads/exchangeproposal_list.html'
    context_object_name = 'exchangeproposals'

    def get_queryset(self):
        return ExchangeProposal.objects.filter(ad_receiver__user=self.request.user).order_by('-created_at')


class AdListView(ListView):
    """Вывод всех объявлений с фильтрацией"""
    model = Ad
    template_name = 'ads/ad_list.html'
    context_object_name = 'ads'
    ordering = ['-created_at']
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        category = self.request.GET.get('category', '')
        condition = self.request.GET.get('condition', '')

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )
        if category:
            queryset = queryset.filter(category__iexact=category)
        if condition:
            queryset = queryset.filter(condition=condition)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        context['category'] = self.request.GET.get('category', '')
        context['condition'] = self.request.GET.get('condition', '')
        context['condition_choices'] = Ad.Condition.choices
        return context
    

class AdDetailView(LoginRequiredMixin, DetailView):
    """Отдельная страничка на каждое объявление"""
    model = Ad
    template_name = "ads/ad_detail.html"
    context_object_name = "ad"


class AdCreateView(LoginRequiredMixin, CreateView):
    """Создание объявление"""
    model = Ad
    template_name = "ads/ad_form.html"
    form_class = AdForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    success_url = reverse_lazy("ads-list")


class AdUpdateView(LoginRequiredMixin, UpdateView):
    """Обновление/редактирование объявление"""
    model = Ad
    template_name = "ads/ad_form.html"
    form_class = AdForm

    def dispatch(self, request, *args, **kwargs):
        # Проверяем, что только пользователь, который создал может редактировать объявление
        ad = self.get_object()
        if ad.user != request.user:
            raise PermissionDenied("У вас нет прав для редактирования этого объявления.")
        return super().dispatch(request, *args, **kwargs)
    
    success_url = reverse_lazy("ads-list")


class AdDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление объявление"""
    model = Ad
    template_name = "ads/ad_confirm_delete.html"

    def dispatch(self, request, *args, **kwargs):
        # Проверяем, что только пользователь, который создал может редактировать объявление
        ad = self.get_object()
        if ad.user != request.user:
            raise PermissionDenied("У вас нет прав для удаление этого объявления.")
        return super().dispatch(request, *args, **kwargs)
    
    success_url = reverse_lazy("ads-list")


class ExchangeProposalListView(ListView):
    """Вывод всех предложений"""
    model = ExchangeProposal
    template_name = 'ads/exchangeproposal_list.html'
    context_object_name = 'exchangeproposals'
    ordering = ['-created_at']
    paginate_by = 5


class ExchangeProposalDetailView(LoginRequiredMixin, DetailView):
    """Отдельная страничка предложения"""
    model = ExchangeProposal
    template_name = "ads/exchangeproposal_detail.html"
    context_object_name = "exchangeproposol"


class ExchangeProposalCreateView(LoginRequiredMixin, CreateView):
    model = ExchangeProposal
    form_class = ExchangeProposalForm
    template_name = "ads/exchangeproposal_form.html"
    success_url = reverse_lazy("exchangeproposal-list")

    def get_initial(self):
        initial = super().get_initial()
        ad_receiver_id = self.request.GET.get("ad_receiver")
        if ad_receiver_id:
            initial["ad_receiver"] = ad_receiver_id
        return initial
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExchangeProposalUpdateView(LoginRequiredMixin, UpdateView):
    """Обновить/редактировать предложение"""
    model = ExchangeProposal
    template_name = "ads/exchangeproposal_form.html"
    form_class = ExchangeProposalForm

    def dispatch(self, request, *args, **kwargs):
        # Проверяем, что только пользователь, который создал может редактировать предложение
        exchangeproposol = self.get_object()
        if exchangeproposol.user != request.user:
            raise PermissionDenied("У вас нет прав для редактирование этого предложение.")
        return super().dispatch(request, *args, **kwargs)
    
    success_url = reverse_lazy("exchangeproposal-list")


class ExchangeProposalDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление предложение"""
    model = ExchangeProposal
    template_name = "ads/exchangeproposal_confirm_delete.html"

    def dispatch(self, request, *args, **kwargs):
        # Проверяем, что только пользователь, который создал может редактировать предложение
        exchangeproposol = self.get_object()
        if exchangeproposol.user != request.user:
            raise PermissionDenied("У вас нет прав для удаление этого предложения.")
        return super().dispatch(request, *args, **kwargs)
    
    success_url = reverse_lazy("exchangeproposal-list")
