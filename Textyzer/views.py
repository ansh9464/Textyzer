# this file is created by ansh jindal i.e it is not a inbuild file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def second(request):
    #to get the text
    original_text=request.POST.get('text','default')
    flag1=0

    #chech the value of the checkbox
    removepunc=request.POST.get('11','off')
    capital=request.POST.get('capatalise','off')
    char_cnt=request.POST.get('char_cnt','off')
    new_line=request.POST.get('newline','off')
    extra_space_remover=request.POST.get('space remover','off')

    #functions for different checkboxes
    if removepunc=='on':
        analyse_text=''
        flag1=1
        punc='''!()-[]{};:'"\,<>./?@#$%^&*~'''
        for char in original_text:
            if char not in punc:
                analyse_text=analyse_text+char
        d={'purpose':'Remove punctuations','analysed_text':analyse_text}
        b='this id the second page <br> <a href=http://127.0.0.1:8000/>back</a>'
        original_text=analyse_text

    if capital=='on':
        analyse_text = ''
        flag1 = 1
        for char in original_text:
            analyse_text = analyse_text + char.upper()
        d = {'purpose': 'capatalise', 'analysed_text': analyse_text}
        original_text=analyse_text

    if char_cnt=='on':
        flag1 = 1
        analyse_text = 'character count is'
        cnt=0
        for char in original_text:
            if char.isalpha():
                cnt=cnt+1
        analyse_text=analyse_text+' '+str(cnt)
        d = {'purpose': 'Char count', 'analysed_text': analyse_text}
        original_text=analyse_text

    if new_line=='on':
        flag1 = 1
        analyse_text = ''
        for char in original_text:
            if char!='\n' and char!='\r':
                analyse_text = analyse_text + char
        d = {'purpose': 'New line remover', 'analysed_text': analyse_text}
        original_text = analyse_text

    if extra_space_remover=='on':
        flag1 = 1
        analyse_text = ''
        for index,char in enumerate(original_text):
            if not(original_text[index]==" " and original_text[index+1]==" "):
                analyse_text = analyse_text + char
        d = {'purpose': 'Space remover', 'analysed_text': analyse_text}
        original_text = analyse_text

    if(flag1!=1):                           #if no checkbox is selected
        return render(request,'error.html')

    else:
        return render(request,'analyse.html',d)