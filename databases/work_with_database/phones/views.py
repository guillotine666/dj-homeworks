from django.db.models.functions import Coalesce
from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort_arg = request.GET.get('sort')
    sorting_direction = ''
    order = 'name'
    if sort_arg == 'name':
        order = 'name'
    elif sort_arg == 'asc_price':
        order = 'price'
    elif sort_arg == 'desc_price':
        order = 'price'
        sorting_direction = '-'

    phones_dict = Phone.objects.all().order_by(f'{sorting_direction}{order}')
    context = {'phones': phones_dict, 'page': request.path[:-1]}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_info = Phone.objects.get(slug=slug)
    context = {'phone': phone_info}
    return render(request, template, context)
