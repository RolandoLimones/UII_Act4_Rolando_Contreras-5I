from django.shortcuts import render

# Create your views here.
def index(request):
    productos = [
        {'nombre': 'Camiseta de Algodón', 'precio': 25.99, 'stock': 150},
        {'nombre': 'Pantalón Vaquero Slim Fit', 'precio': 49.95, 'stock': 80},
        {'nombre': 'Zapatillas Deportivas', 'precio': 75.00, 'stock': 120},
    ]
    contexto = {'productos': productos}
    return render(request, 'index.html', contexto)