# I have created this file- Sonali Sharma
# creating http response because views return http response.
from django.http import HttpResponse
from django.shortcuts import render # for templates

# for pipelining
# Pipeline is an asset packaging library for Django, providing both CSS and JavaScript concatenation and compression, built-in JavaScript template support, and optional data-URI image and font embedding
def index(request):
    #params = {'name':'Sonali','place':'Mars'}
    return render (request,'index.html') # requesting to run index.html
    # third arg is also present, i.e, a variable, i.e you can pass dictionary 
   # return HttpResponse("<h2>Home</h2>")

def analyze(request):
 
    djtext = request.POST.get('text', 'default') # displays text , if not presesnt will dispaly default
    # GET is used if we want the resultant text to view in url. If the size of text is too long it will give error, in that case
    # POST is used to gather all the text and it display it from the server to our page without error.
    # POST is basically used so that our entered data do not shows in url and hence the url must look clean and clear


    # Check checkbox values
    rempunctuations = request.POST.get('rempunctuations', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    
    #Check which checkbox is on
    if rempunctuations == "on":
        punctuations = '''!()-[]{};:,'"\\<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext= analyzed
        #return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        djtext= analyzed
        #return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext= analyzed
        #return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext= analyzed
        #return render(request, 'analyze.html', params)

    if (charcount == "on"):
        count=0
        for char in djtext:
            count=count+1
        params = {'purpose': 'Total Characters Counted', 'analyzed_text': count}
     
    if(rempunctuations != "on" and fullcaps !="on" and extraspaceremover !="on" and newlineremover != "on" and charcount != "on"):
        analyzed = ""
        for char in djtext:
            if char in djtext:
                analyzed = analyzed + char
        params = {'purpose':'with no operation selected', 'analyzed_text': analyzed }
        djtext= analyzed

    return render(request, 'analyze.html', params)
 


# Templating - Creating html files separately
# step-1 go to settings.py , add templates to DIRS[]
# step 2 create dir templates, add index.html

