from django.shortcuts import render
from .forms import RegisterForm
from django.http import Http404

def register_view(request):
        
    if request.POST:
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })
    
def register_create(request):
    if request.POST:
        raise Http404()
    form = RegisterForm(request.POST)
    return render(request, '', {
            'form': form,
        } ) 