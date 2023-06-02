from django.shortcuts import render, redirect
from django.http import HttpResponse
from application1.models import Student

from django.core import serializers
from django.http import HttpResponse


# Create your views here.


def ruta_nueva_view(self):
    name = "Luis Rios"
    average = 4 + 6
    return HttpResponse(f'Hola esta es una respuesta {name} promedio {average}')


def about_view(request):
    project = "Book catalog final project"
    name = "Cruz Salinas Jesus Arturo"
    matter = "Web Framework Programming"
    group ="8vo Semester C"


    average = 40 + 60
    lista = [2, 3, 4, 6, 1, 2, 3, 4, 5]
    var_context = {
        "title": "ABOUT",
        "proyecto": project,
        "materia": matter,
        "nombre": name,
        "semestre":group,
        "periodo":period,
        "promedio": average,
        "edad": 50,
        "horario": "vespertino",
        "lista": lista
    }
    return render(request, "about.html", context=var_context)


def home_view(request):
    students = Student.objects.all()
    var_context = {
        "title": "Inicio",
        "students": students
    }
    return render(request, "home.html", context=var_context)


def contact_view(request):
    project = "Book catalog final project"
    name = "Nuñez Enriquez paola"
    phone = "9612547252"
    email = "l19270353@tuxtla.tecnm.mx"
    var_context = {
        "title": "CONTACT US",
        "proyecto": project,
        "nombre": name,
        "telefono": phone,
        "correo": email
    }
    return render(request, "contact.html", context=var_context)

def book_view(request):
    var_context = {
        "title": "BOOKS"
    }
    return render(request, "catalogo_libro.html", context=var_context)

def add_student(request):
    if request.method == 'GET':
        return render(request, "form_student.html")
    else:
        print("guardar")
        student = Student()
        student.name = request.POST.get('name')
        student.first_name = request.POST.get('first_name')
        student.second_name = request.POST.get('second_name')
        student.gender = request.POST.get('gender')
        student.birth_date = request.POST.get('birth_date')
        student.save()
        return redirect('home_view')


def update_student(request, student_id):
    student = Student.objects.get(id=student_id)
    variable = {
        "student": student
    }
    if request.method == 'GET':
        return render(request, "form_student.html", context=variable)
    else:
        student.name = request.POST.get('name')
        student.first_name = request.POST.get('first_name')
        student.second_name = request.POST.get('second_name')
        student.gender = request.POST.get('gender')
        student.birth_date = request.POST.get('birth_date')
        student.save()
        return redirect('home_view')


def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('home_view')


def all_students(request):
    students = Student.objects.all()
    qs_json = serializers.serialize('json', students)
    return HttpResponse(qs_json, content_type='application/json')

