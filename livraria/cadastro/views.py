from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import LivrosForm
from .models import Livros


def cadastros(request, livro_id= None):
    registro = None

    if livro_id:
        registro = get_object_or_404(Livros, pk=id)
    if request.method == 'POST':
        form = LivrosForm(request.POST, instance=registro)

        if form.is_valid():
            registro = form.save()
            form = LivrosForm()
    else:
        form = LivrosForm(instance=registro)

    context = {'form': form,
               'livros': Livros.objects.all()}
    return render(request,
                  template_name='cadastrolivro.html',
                  context=context)


def numero(request):
    return HttpResponse('funcionou')


def index(request):
    return render(request, template_name='index.html')
