from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404

from .models import Apuntar, Contact, Post

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
    if request.method=='POST':
        contact=Contact()
        nombre=request.POST.get('nombre')
        email=request.POST.get('email')
        telefono=request.POST.get('telefono')
        consulta=request.POST.get('consulta')
        contact.nombre=nombre
        contact.email=email
        contact.telefono=telefono
        contact.consulta=consulta
        contact.save()
        return render(request, 'mensaje.html')

    return render(request, 'home.html')

def cursos(request):
    return render(request, 'cursos.html')

def contacto(request):
    if request.method=='POST':
        contact=Contact()
        nombre=request.POST.get('nombre')
        email=request.POST.get('email')
        telefono=request.POST.get('telefono')
        consulta=request.POST.get('consulta')
        contact.nombre=nombre
        contact.email=email
        contact.telefono=telefono
        contact.consulta=consulta
        contact.save()
        return render(request, 'mensaje.html')
    return render(request, 'contacto.html')

def apuntarse(request):
    if request.method=='POST':
        apuntar=Apuntar()
        nombre=request.POST.get('nombre')
        email=request.POST.get('email')
        telefono=request.POST.get('telefono')
        apellidos=request.POST.get('apellidos')
        curso=request.POST.get('curso')
        mes=request.POST.get('mes')
        apuntar.nombre=nombre
        apuntar.email=email
        apuntar.telefono=telefono
        apuntar.apellidos=apellidos
        apuntar.curso=curso
        apuntar.mes=mes
        apuntar.save()
        return render(request, 'contestacion.html')
        
    return render(request, 'apuntarse.html')

def handle_not_found(request,exception):
    return render(request, '404.html')



def post_list(request):
    posts = Post.published.all()
    
    paginator = Paginator(posts, 10) # 10 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
        
    return render(request,'post_list.html',{'posts':posts, page:'pages'})

def post_detail(request, post):
    post=get_object_or_404(Post,slug=post,status='published')
    return render(request, 'post_detail.html',{'post':post})