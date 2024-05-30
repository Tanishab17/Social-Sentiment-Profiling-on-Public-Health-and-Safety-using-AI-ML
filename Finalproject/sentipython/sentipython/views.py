from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
def external(request):
    inp = request.POST.get('hero-field')
    out= run([sys.executable,'D:\\Sentimental analysis\\MY\\sentipython\\sentipython\\Main.py',inp],shell=False,stout=PIPE)
    print(out)

    return render(request,'index.html',{'data1':out})

