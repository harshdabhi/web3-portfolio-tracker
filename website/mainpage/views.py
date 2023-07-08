from django.shortcuts import render

# Create your views here.

def homepage(request):

    

    context={
        'value':5000
    }


    return render(request,'homepage.html',context=context)