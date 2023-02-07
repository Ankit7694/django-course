# # i have created this file - ankit
# from django.http import  HttpResponse
# from django.shortcuts import  render

# def index(request):
#     return render(request,'index.html')
# def analyze(request):
#     # get the text
#     djtext=request.GET.get('text','default')
#     # check checkbox values 
#     removepunc=request.GET.get('removepunc','off')
#     fullcaps=request.GET.get('fullcaps','off')
#     newlineremover=request.GET.get('newlineremover','off')
#     extraspaceremover=request.GET.get('extraspaceremover','off')
#     charcount=request.GET.get('charcount','off')
#     # check with check box with on 
    
#     if removepunc=="on":
#          # analyzed=djtext
#          punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~|'''
#          analyzed=" "
#          for char in djtext:
#             if char not in punctuations:
#               analyzed=analyzed+char 
#          params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
#          # analyse the text
#          return render(request,"analyze.html",params)
#     elif fullcaps=="on":
#         analyzed=""
#         for char in djtext:
#             analyzed=analyzed+char.upper()
#         params={'purpose':'changed to uppercase', 'analyzed_text':analyzed}
#             # analyse the text
#         return render(request,"analyze.html",params)
#     elif newlineremover=="on":
#          analyzed=""
#          for char in djtext:
#             if char !="\n" and char !="\r":
#                analyzed=analyzed+char.upper()
#          params={'purpose':'Removes new line', 'analyzed_text':analyzed}
#             # analyse the text
#          return render(request,"analyze.html",params)
#     elif extraspaceremover=="on":
#          analyzed=""
#          for index,char in  enumerate(djtext):
#              if not (djtext[index]==" " and djtext[index+1]==" "):
#                analyzed=analyzed+char
#          params={'purpose':'Removes new line', 'analyzed_text':analyzed}
#             # analyse the text
#          return render(request,"analyze.html",params)
#     elif charcount=="on":
#          analyzed=""
         
#          count=0
#          for char in djtext:
#                 count=count+1
#          print(count)
#          params={'purpose':'character','count':count}
#             # analyse the text
#          return render(request,"analyze.html",params)
       
#     else:
#         return HttpResponse("Error")
 