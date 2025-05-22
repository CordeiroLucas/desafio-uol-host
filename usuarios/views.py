from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import UsuarioForm
from .models import Usuario
import requests
import xml.etree.ElementTree as ET
from django.core.cache import cache

class Index(View):
    def get(self, request):
        return redirect('cadastro')

class Cadastro(View):
    template_name = 'cadastro.html'
    form_class = UsuarioForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            codinome = self.get_codinome(form.cleaned_data['grupo'])
            if codinome is not None:
                obj = form.save(commit=False)
                obj.codinome = codinome
                obj.save()
                return render(
                    request, self.template_name, {'form': form, 'status': 0}
                )
            return render(
                request, self.template_name, {'form': form, 'status': 1}
            )
        return render(request, self.template_name, {'form': form, 'status': 2})

    def get_codinome(self, grupo):
        if grupo == 'V':
            if not cache.get('vingadores'):
                response = requests.get(
                    'https://raw.githubusercontent.com/uolhost/test-backEnd-Java/refs/heads/master/referencias/vingadores.json'
                ).json()
                cache.set('vingadores', response)

            codinomes = [
                item['codinome']
                for item in cache.get('vingadores')['vingadores']
            ]

        elif grupo == 'LJ':
            if not cache.get('liga_da_justica'):
                response = requests.get(
                    'https://raw.githubusercontent.com/uolhost/test-backEnd-Java/refs/heads/master/referencias/liga_da_justica.xml'
                ).content

                cache.set('liga_da_justica', response)

            root = ET.fromstring(cache.get('liga_da_justica'))
            codinomes_element = root.find('codinomes')
            codinomes = [
                codinome.text
                for codinome in codinomes_element.findall('codinome')
            ]

        codinomes_usados = Usuario.objects.values_list('codinome', flat=True)

        print(f'Utilizados: {codinomes_usados}')

        codinomes_disponiveis = set(codinomes) - set(codinomes_usados)

        print(f'Disponíveis: {codinomes_disponiveis}')

        if not codinomes_disponiveis:
            return

        return list(codinomes_disponiveis)[0]


class Visualizar(View):
    template_name = 'visualizar.html'

    def get(self, request):
        usuarios = Usuario.objects.all()

        sort_by = request.GET.get('sort_by', 'id')
        usuarios = usuarios.order_by(sort_by)

        if request.GET.get('order') == 'desc':
            usuarios = usuarios.reverse()
            


        return render(request, self.template_name, {'usuarios': usuarios, 'sort_by': sort_by ,'order': request.GET.get('order')})
