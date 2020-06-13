from django.shortcuts import render,redirect
from .models import persona
from .forms import PersonaForm
# Create your views here.
def inicio(request):
    personas = persona.objects.all()
    contexto={
        'personas':personas
    }
    return render(request,'index.html', contexto)

def crear_persona(request):
    if request.method=='GET':
        form = PersonaForm()
        contexto ={
            'form':form
        }
    else:
        form= PersonaForm(request.POST)
        contexto ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')  
    return render(request,'nuevapersona.html',contexto)

def editar_persona(request,id):
    person= persona.objects.get(id = id)
    if request.method == 'GET':
        form = PersonaForm(instance = person)
        contexto = {
            'form':form
        }
    else:
        form= PersonaForm(request.POST, instance = person)
        contexto ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'nuevapersona.html',contexto)
def eliminarPersona(request,id):
    personas= persona.objects.get(id=id)
    personas.delete()
    return redirect('index')