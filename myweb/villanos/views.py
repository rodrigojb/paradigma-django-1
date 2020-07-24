import datetime

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'villanos/index.html')

def vista_hoy(request):
    now = datetime.datetime.now()
    context = {
        'now': now
    }
    return render(request, 'villanos/today.html', context)

def list(request):
    listado_villanos = [
        {
            'nombre': 'Darth Vader',
            'recompensa': 100000,
            'moneda': 'AR'
        },
        {
            'nombre': 'Joker',
            'recompensa': 500000,
            'moneda': 'USD'
        },
        {
            'nombre': 'Oso Yoghi',
            'recompensa': 900000,
            'moneda': 'USD'
        }
    ]

    villano_mas_caro = sorted(listado_villanos, key= lambda villano: villano['recompensa'], reverse=True)[0]

    context = {
        'listado_villanos': listado_villanos,
        'villano_mas_caro': villano_mas_caro,
    }

    return render(request, 'villanos/list.html', context)