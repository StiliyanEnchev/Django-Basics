from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from departments.models import Department


# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the app index.</h1>")


def redirect_to_softuni(request):
    #raise Http404
    return redirect('home')


def view_with_int(request, pk):
    return HttpResponse(f"<h1>Int with: {pk}</h1>")


def view_with_slug(request, slug):
    department = Department.objects.get(slug=slug)
    return HttpResponse(f"<h1>Department with slug: {department}</h1>")


def show_archive(request, archive_year):
    return HttpResponse(f"<h1>The year is: {archive_year}</h1>")


def view_with_name(request, variable):
#    return HttpResponse(f"<h1>Index with var: {variable}</h1>")
     return render(request, 'departments/name_template.html', {"variable": variable})