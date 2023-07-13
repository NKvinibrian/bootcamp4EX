from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import render
import ecom.models


class HomeView(View):

    def get(self, *args, **kwargs):
        dados = ecom.models.Produtos.objects.all()
        contexto = {
            'dados': dados
        }
        return render(request=self.request, template_name='home.html', context=contexto)
