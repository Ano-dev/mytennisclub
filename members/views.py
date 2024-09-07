from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members
# Create your views here.

def members(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    members_details = Members.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember':members_details,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mydata = Members.objects.filter(firstname='anold',id=2).values()
    template = loader.get_template('testing.html')
    context = {
        "mymembers":mydata
    }
    return HttpResponse(template.render(context,request))