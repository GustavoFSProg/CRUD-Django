from django.shortcuts import render, redirect
from .models import Usuarios
from django.http import HttpResponse

# def ver_usuarios(request):
#     return HttpResponse("Olá")

def insere_user(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    user = Usuarios(name=name, email=email,senha=senha)
    user.save()
    # userss = Usuarios.objects.all()
    usuarios={'usuarios': Usuarios.objects.all()}    
    return render(request, 'seeds.html', usuarios)
    return render(request, 'ver_all.html', usuarios)


# def update_user(request):
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     senha = request.POST.get('senha')
#     user = Usuarios(name=name, email=email,senha=senha)
    
#     # userss = Usuarios.objects.all()
#     usuarios={'usuarios': Usuarios.objects.all()}    
#     return  redirect('ver_all')




def ver_cadastro(request):
   if request.method == "GET":       
        return render(request, 'inserir.html')
   



def seeds(request):
   if request.method == "GET":  
    usuarios={'usuarios': Usuarios.objects.all()}
    return render(request, 'seeds.html',  usuarios)



def editar(request, id):
    usuarios= Usuarios.objects.get(id=id)
    # usuarios={'usuarios': Usuarios.objects.all()}
    return render(request, 'update.html', {'usuario': usuarios})



def delete(request, id):
    usuarios= Usuarios.objects.get(id=id)
    usuarios.delete()
    usuarios={'usuarios': Usuarios.objects.all()}   
    return render(request, 'seeds.html', usuarios)





def update(request, id):
    vnome = request.POST.get('name')
    vemail = request.POST.get('email')
    vsenha = request.POST.get('senha')
    usuarios= Usuarios.objects.get(id=id)

    usuarios.name = vnome
    usuarios.email = vemail
    usuarios.senha = vsenha
    usuarios.save()

    usuarios={'usuarios': Usuarios.objects.all()}    
    return render(request, 'seeds.html', usuarios)

    





def ver_usuarios(request):
   if request.method == "GET":   
        usuarios={'usuarios': Usuarios.objects.all()}    
        return render(request, 'ver_all.html', usuarios)