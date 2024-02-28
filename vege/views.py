from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def receipes(request):
    if request.method ==  "POST":

        data = request.POST  #for text
        receipe_image = request.FILES.get('receipe_image') #for files
        receipe_name = data.get('receipe_name') #saving received data
        receipe_description = data.get('receipe_description')


          #this will save data from user 
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description, 
             receipe_image =  receipe_image,



        )
        #this will avoid reloading page after one submission
        #return redirect('/receipes/')



        
        






    return render(request, "receips.html")