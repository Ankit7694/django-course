#i have created this file - ankit
from django.http import  HttpResponse
from django.shortcuts import  render

def index(request):
    return render(request,'index.html')
def analyze(request):
    # get the text
    djtext=request.GET.get('text','default')
    # check checkbox values     
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')    
    newlineremover=request.GET.get('newlineremover','off')    
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charcount=request.GET.get('charcount','off')
    # check with check box with on 
         # analyzed=djtext
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~|'''
    # analyzed=" "
    count=0
    # for char in djtext:
    analyzed = djtext
    if fullcaps=="on":
        analyzed = analyzed.upper()
    if extraspaceremover.lower()=="on":
       analyzed = " ".join(analyzed.split()) 
    if newlineremover == "on":
        analyzed = analyzed.strip()
    if removepunc=="on":
        for i in punctuations:
            if i in analyzed:
                analyzed = analyzed.replace(i,"")
    if charcount=="on":
        analyzed = len(analyzed.replace(" ", ""))

   
        
    params={'purpose':'Characters','analyzed_text':analyzed}
        
    return render(request,"analyze.html",params)
