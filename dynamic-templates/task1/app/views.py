from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    context = {}
    with open('./inflation_russia.csv', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        context['headers'] = next(reader)
        data = []
        for row in reader:
            data.append([float(x) if x else '' for x in row])

        context['data'] = data

    return render(request, template_name,
                  context)
