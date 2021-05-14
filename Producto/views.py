from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404

from .models import *
from .forms import *
# Create your views here.
# def listaP(request):
    
    
    
#     if request.method == "POST":
#         busqueda = request.POST.get('producto')
#         productos = Producto.objects.filter(nombre__icontains=busqueda)
#     else:
#         productos = Producto.objects.all()
#     formulario = SearchForm()       
#     categorias = Categoria.objects.all()
    
#     page = request.GET.get('page',1)
    
#     try:
#         paginator = Paginator(productos,5)
#         productos=paginator.page(page)
#     except:
#         raise Http404
    
#     data ={
#         'categorias':categorias,
#         'productos':productos, 
#         'formulario':formulario,
#         'paginator':paginator
#         }
    
#     return render(request,'producto/productoIndex.html',data)

def listaP(request):
    
    productos = Producto.objects.all()
    formulario = SearchForm()       
    categorias = Categoria.objects.all()
    
    page = request.GET.get('page',1)
    
    try:
        paginator = Paginator(productos,5)
        productos=paginator.page(page)
    except:
        raise Http404
    
    data ={
        'categorias':categorias,
        'productos':productos, 
        'formulario':formulario,
        'paginator':paginator
        }
    
    return render(request,'producto/productoIndex.html',data)



def listaP_post(request):

    if request.method == "POST":
        busqueda = request.POST.get('producto')
        productos = Producto.objects.filter(nombre__icontains=busqueda)
    formulario = SearchForm()       
    categorias = Categoria.objects.all()
    
    page = request.GET.get('page',1)
    
    try:
        paginator = Paginator(productos,5)
        productos=paginator.page(page)
    except:
        raise Http404
    
    data ={
        'categorias':categorias,
        'productos':productos, 
        'formulario':formulario,
        'paginator':paginator
        }
    
    return render(request,'producto/productoIndex.html',data)
    

def categoria(request,categoria_id):
    list_categorias = Categoria.objects.all()
    categorias = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categorias=categorias)
    
    data={
        'categorias':categorias,
        'productos':productos,
        'list_categorias':list_categorias}
    return render(request,'producto/categoria.html',data)


def pedidos(request):
    return render(request,'producto/pedidos.html')