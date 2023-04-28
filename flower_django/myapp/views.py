from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect # < here
from .forms import MyForm

# import local models
from .models import (
    Flower
)

# ? Create your views here.
# ? Home Page
def index(request): 
    template_name = 'myapp/index.html'

    q = request.GET.get('q', None)
    items = ''
    if q is None or q == "":
        flowers = Flower.objects.all()
    elif q is not None:
        flowers = Flower.objects.filter(title__contains=q)
    # flowers = Flower.objects.all()
    context = {
        "flowers"   :   flowers
    }
    return render(request,  template_name , context)

# ? Flower Detail Page
def detail(request, slug=None): # < here
    template_name = 'myapp/detail.html'
    flower = get_object_or_404(Flower, slug=slug)
    context = {
        'flower': flower
    }
    return render(request, template_name, context)


# ? Tags View
def tags(request, slug=None): 
    template_name = 'myapp/index.html'
    flowers = Flower.objects.filter(tags__slug=slug)
    context={
        'flowers': flowers 
    }
    return render(request, template_name , context)


# ? Create Flower View
def create_flower(request): # < here
    template_name = 'myapp/edit.html'
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
    context = {
        'form': form
    }
    return render(request, template_name , context)

# ? Update Flower View
def edit_flower(request, pk=None): # < here
    template_name = 'myapp/edit.html'
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == "POST":
        form = MyForm(request.POST, instance=flower)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm(instance=flower)
    context = {'form': form
    }
    return render(request,  template_name, context)

# ? Delete Flower View
def delete_flower(request, pk=None): 
    temaplte_name = 'myapp/index.html'
    flower = get_object_or_404(Flower, pk=pk)
    flower.delete()
    context = {

    }
    return render(request, temaplte_name, context)