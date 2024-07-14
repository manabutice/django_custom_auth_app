from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import Store
from django.views.generic import View
from django.shortcuts import render


class StoreView(View):
    def get(self, request, *args, **kwargs):
        store_data = Store.objects.all()

        return render(request, 'app/store.html', {
            'store_data': store_data,
        })

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "app/index.html"
    login_url = "/accounts/login/"