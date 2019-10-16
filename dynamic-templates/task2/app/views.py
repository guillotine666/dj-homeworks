from django.shortcuts import render


def home_view(request):
    context = {'title': 'Home'}
    template_name = 'app/home.html'
    return render(request, template_name, context)


def about_view(request):
    context = {
        'active': 'about',
        'title': 'О проекте'
    }
    template_name = 'app/about.html'
    return render(request, template_name, context)


def contacts_view(request):
    context = {
        'active': 'contacts',
        'title': 'Контакты'
    }
    template_name = 'app/contacts.html'
    return render(request, template_name, context)


def examples_view(request):
    template_name = 'app/examples.html'

    items = [{
        'title': 'Apple II',
        'text': 'Легенда',
        'img': 'ii.jpg'
    }, {
        'title': 'Macintosh',
        'text': 'Свежие новинки октября 1983-го',
        'img': 'mac.jpg'
    }, {
        'title': 'iMac',
        'text': 'Оригинальный и прозрачный',
        'img': 'imac.jpg'
    }]
    context = {
        'items': items,
        'active': 'examples',
        'title': 'Примеры'
    }
    return render(request, template_name,
                  context)
