from ads.models import Ad, ExchangeProposal
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class AdListView(ListView):
    """Вывод всех объявлений"""
    model = Ad
    template_name = 'ads/ad_list.html'
    context_object_name = 'ads'
    ordering = ['-created_at']
    paginate_by = 5
    

class AdDetailView(LoginRequiredMixin, DetailView):
    """Отдельная страничка на каждое объявление"""
    model = Ad
    template_name = "ads/ad_detail.html"
    context_object_name = "ad"


class AdCreateView(LoginRequiredMixin, CreateView):
    """Создание объявление"""
    model = Ad
    fields = ["title"]
    template_name = "ads/ad_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    success_url = reverse_lazy("ads-list")


class AdUpdateView(LoginRequiredMixin, UpdateView):
    """Обновление/редактирование объявление"""
    model = Ad
    fields = ["title"]
    template_name = "ads/ad_form.html"

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


class ExchangeProposolListView(ListView):
    """Вывод всех предложений"""
    model = ExchangeProposal
    template_name = 'ads/exchangeproposal_list.html'
    context_object_name = 'exchangeproposals'
    ordering = ['-created_at']
    paginate_by = 5


class ExchangeProposolDetailView(LoginRequiredMixin, DetailView):
    """Отдельная страничка предложения"""
    model = ExchangeProposal
    template_name = "ads/exchangeproposal_detail.html"
    context_object_name = "exchangeproposol"


class ExchangeProposolCreateView(LoginRequiredMixin, CreateView):
    """Создание предложений"""
    model = ExchangeProposal
    fields = ["ad_sender_id", "ad_receiver_id"]
    template_name = "ads/exchangeproposal_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    success_url = reverse_lazy("exchangeproposal-list")


class ExchangeProposolUpdateView(LoginRequiredMixin, UpdateView):
    """Обновить/редактировать предложение"""
    model = ExchangeProposal
    fields = ["ad_sender_id", "ad_receiver_id"]
    template_name = "ads/exchangeproposal_form.html"

    def dispatch(self, request, *args, **kwargs):
        # Проверяем, что только пользователь, который создал может редактировать предложение
        exchangeproposol = self.get_object()
        if exchangeproposol.user != request.user:
            raise PermissionDenied("У вас нет прав для редактирование этого предложение.")
        return super().dispatch(request, *args, **kwargs)
    
    success_url = reverse_lazy("exchangeproposal-list")


class ExchangeProposolDeleteView(LoginRequiredMixin, DeleteView):
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
