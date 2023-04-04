from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductAdditionForm


def product_add_view(request):
    form = ProductAdditionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductAdditionForm()
    context = {
        'form': form
    }
    return render(request, 'product_addition.html', context)


def product_update_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    form = ProductAdditionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'product_addition.html', context)


def products_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products.html', context)


def product_detail_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    context = {
        'object': obj
    }
    return render(request, 'product_detail.html', context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, 'product_delete.html', context)
