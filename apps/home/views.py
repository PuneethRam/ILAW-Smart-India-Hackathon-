# -*- encoding: utf-8 -*-

from multiprocessing import context
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Todo,Case,Sec,UploadCaseFile
from django.views.decorators.http import require_POST
from .forms import TodoForm,UploadFileForm
import os
from .get_sec_def import getDef
from .getTranslate import getTranslate


IMAGE_FILE_TYPES = ['txt']
@require_POST
@login_required(login_url="/login/")



def translate(request):
    form=UploadFileForm()
    if request.method == 'POST':
        print("request post")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("form valid")
            # user_pr = form.save(commit=False)
            # user_pr.uploadfile = request.FILES['uploadfile']
            # print(user_pr.uploadfile.path)
            # for file in os.listdir('C:\Users\sumit\OneDrive\Desktop\black-dashboard-django\core\media_root\media'):
            #     if user_pr.uploadfile.name.split('.')[0] in file:
            #         case_content=''
            #         with open(user_pr.uploadfile.path,'r') as f:
            #             for line in f.readlines():
            #                 case_content += line.strip()
            

            file_type = user_pr.uploadfile.name.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                html_template = loader.get_template('home/translator.html')
                context={}
                return HttpResponse(html_template.render(context, request))
            user_pr.save()


    #with open(newfile.uploadfile.path,'r') as f:
    #    for line in f.readlines():
    #        case_content += line.strip()


    language=request.POST.get("dropdown", "")
    print(language)
    output=getTranslate(language,case_content)

    context={'output':output,'language':language,'form':form}

    html_template = loader.get_template('home/translator.html')
    return HttpResponse(html_template.render(context, request))




@require_POST
@login_required(login_url="/login/")

def sec(request):
    
    input=request.POST.get("SecNo", "")
    output=getDef(int(input))

    sec_def=Sec(sec_name=input,sec_def=output)
    sec_def.save()
    context={'output':output}

    html_template = loader.get_template('home/sec_def.html')
    return HttpResponse(html_template.render(context, request))
                                                

data_path = "apps\sihdoc\Object_casedocs"

@require_POST
@login_required(login_url="/login/")
def addCasetoDB(request):
    context = {}

    for case_path in os.listdir(data_path):
        
        case_path_new = data_path + '/' + case_path        
        # read case
        case_filename = case_path
        content = ""
        if ".txt" in case_filename:
            with open(case_path_new, 'r') as f:
                for line in f.readlines():
                    content += line.strip()
                
            case_description = content
            case_status = "completed"

            new_case = Case(case_name=case_filename, case_description=case_description, case_status=case_status)
            new_case.save()

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

def analysis(request):
    context = {}

    html_template = loader.get_template('home/analysis.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def index(request):
    form=TodoForm()
    todo_list=Todo.objects.order_by('id')
    context = {'segment': 'index','todo_list' : todo_list ,'form' : form}


    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

def index(request):
    todo_list = Todo.objects.order_by('id')
    context = {'todo_list' : todo_list}
    return render(request, 'home/index.html', context)

def index(request):
    todo_list = Todo.objects.order_by('id')

    form = TodoForm()

    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'home/index.html', context)

@require_POST
@login_required(login_url="/login/")
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
    context = {}
    html_template = loader.get_template('home/index.html')

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
