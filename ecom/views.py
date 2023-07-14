from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import render
import ecom.models
from django.http import HttpResponse


class HomeView(View):

    def get(self, *args, **kwargs):
        dados = ecom.models.Produtos.objects.filter(status=True)
        contexto = {
            'dados': dados
        }
        return render(request=self.request, template_name='home.html', context=contexto)


class ProdutoView(View):

    def post(self, *args, **kwargs):
        produto_id = self.request.POST.get('id')
        nome = self.request.POST.get('nome')
        preco = self.request.POST.get('preco')
        estoque = self.request.POST.get('estoque')
        imagem = self.request.FILES.get('imagem')
        if produto_id is None or produto_id == '':
            produto = ecom.models.Produtos()
        else:
            produto = ecom.models.Produtos.objects.filter(id=produto_id).first()

        produto.nome = nome
        produto.preco = preco
        produto.imagem = imagem
        produto.estoque = estoque
        produto.save()
        return HttpResponse('Produto cadastrado com sucesso!')

    def delete(self, *args, **kwargs):
        produto_id = self.request.GET.get('id')
        produto = ecom.models.Produtos.objects.filter(id=produto_id).first()
        produto.status = False
        produto.save()
        return HttpResponse('Produto excluído com sucesso!')
