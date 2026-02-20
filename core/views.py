from django.shortcuts import render

def core_view(request):
    return render(request,'core/index.html')
