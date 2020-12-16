from django.urls import path
from crud import views

urlpatterns = [

    path("",views.home),
    path("savedata",views.savedata),
    path("update/<int:id>",views.updaterecords),
    path("viewrecords",views.viewrecords),
    path("delete/<int:id>",views.deleterecords)
]