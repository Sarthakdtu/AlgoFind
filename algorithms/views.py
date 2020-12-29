from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request, 'algorithms/home.html', {})

def view_code(request, code_id):
    code = Code.objects.get(id=code_id)
    code = {"code":}
    return render(request, 'algorithms/view_code.html', )