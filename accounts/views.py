from django.shortcuts import render

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email.endswith('@'):
            return render (request, 'accounts/partials/error.html'), {
                    'msg': 'Apenas e-mails são permitidos!'
                }
    return render(request, 'accounts/register.html')