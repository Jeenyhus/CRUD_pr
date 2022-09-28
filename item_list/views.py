from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ItemForm
from .models import Item

# Create your views here.
def add(request):
    form = ItemForm(request.POST)
    #item = Item.objects.all()
    if form.is_valid():
        form.save()
    return render(request, 'add.html', {'form': form})

def show(request):
    item = Item.objects.all()
    return render(request, 'show.html', {'item': item})


def update(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'update.html', {'item': item})


def delete(request, id):
    form = Item.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect('/')