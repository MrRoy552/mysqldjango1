from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from crud.models import employee


def home(request):
    return render(request,"index.html")

def savedata(request):
    s=employee()
    s.name=request.POST["name"]
    s.gender=request.POST["gender"]
    s.salary=request.POST["salary"]
    s.phone_number=request.POST["phone_number"]
    s.Emp_address=request.POST["Emp_address"]
    s.save()
    data=employee.objects.all()
    #return render(request,"index.html")

    return render(request,"record.html",{"data":data})  #data i want to save in tabular format
def viewrecords(request):
    data = employee.objects.all()
    return render(request,"record.html",{"data": data})


def updaterecords(request,id):
    obj=employee.objects.get(id=id)
    if request.method=="POST":
        obj.name = request.POST["name"]
        obj.gender = request.POST["gender"]
        obj.salary = request.POST["salary"]
        obj.phone_number = request.POST["phone_number"]
        obj.Emp_address = request.POST["Emp_address"]
        obj.save()
        return redirect(viewrecords)
    return render(request,"updaterecords.html",{"obj":obj})

def deleterecords(request,id):
    obj=employee.objects.get(id=id)
    obj.delete()
    data = employee.objects.all()
    return redirect(viewrecords)