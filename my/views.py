from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    firstcap=request.POST.get('firstcap','off')
    extraspaceremove=request.POST.get('extraspaceremove','off')
    newlineremove=request.POST.get('newlineremove','off')
    charcount=request.POST.get('charcount','off')

    if removepunc=="on":
        punctuations='''~!@#$%^&*()_+[]|:;"',./<>?'''
        analized=""
        for char in djtext:
            if char not in punctuations:
                analized=analized+char
        djtext=analized

    if uppercase=="on":
        analized=""
        for char in djtext:
            analized = analized + char.upper()
        djtext=analized

    if firstcap=="on":
        analized=""
        analized=djtext.capitalize()
        djtext=analized

    if extraspaceremove=="on":
        analized=""
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analized=analized+char
        djtext=analized

    if newlineremove=="on":
        analized=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analized = analized + char

    if charcount=="on":
        c=0
        for index,char in enumerate(djtext):
            c=index+1
        params={'purpose':'character counter','analized_text':c}
        return render(request,'analyze.html',params)

    if(removepunc!="on" and firstcap!="on" and extraspaceremove!="on" and newlineremove!="on" and uppercase!="on"):
        return HttpResponse("please select any option and try again")

    params={'purpose':'text utils','analized_text':analized}
    return render(request,'analyze.html',params)