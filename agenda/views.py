from django.shortcuts import render

def agenda_view(request):
    return render(request,'agenda/agenda.html')