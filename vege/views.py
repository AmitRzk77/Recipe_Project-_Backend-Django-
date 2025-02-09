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
        return redirect('/')
    

    
      #Set View of data
    queryset = Receipe.objects.all()
    context = {'receips': queryset}


    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))    #search
    
    



        
    return render(request, "receips.html", context)

def update_receipe(request, id):
    queryset = Receipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        
        receipe_image = request.FILES.get('receipe_image') #for files
        receipe_name = data.get('receipe_name') #saving received data
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name,
        queryset.receipe_description = receipe_description


        if receipe_image:
         queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/')


    context = {'receipe': queryset}
    return render(request, "update_receipe.html", context)


    


#this is for delete id , setting id for items and delete
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect ('/')
