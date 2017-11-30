import os
import re

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from .models import UserMetaInfo
from .models import PaperMetaInfo
from .models import PaperUploadInfo

from .src import idshuffler

# Create your views here.


@csrf_exempt
def sample(request):
    return render(request, 'app0/sample.html', {})


@csrf_exempt
def index(request):
    template = loader.get_template('app0/index.html')
    context = {

    }
    return HttpResponse(template.render(context))


@csrf_exempt
@login_required
def home(request):
    paper_ids = PaperUploadInfo.objects.order_by('-date')[:10]
    papers = [PaperMetaInfo.objects.get(id=id) for id in paper_ids]
    return render(request, 'app0/home.html', {
        'papers': papers
    })


@csrf_exempt
def register(request):
    name = request.POST.get('userName', None)
    password = request.POST.get('password', None)
    email = request.POST.get('email', None)
    if not name or not password:
        # MARK: -username or password lacked, should be detected at js(?)
        return HttpResponse(loader.get_template('app0/register.html').render({
            'info': 'please input username and password.'
        }))
    user = User.objects.create_user(username=name, password=password, email=email)
    login(request, user)
    return HttpResponse(loader.get_template('app0/home.html').render())


@csrf_exempt
def my_login(request):
    name = request.POST.get('userName', None)
    password = request.POST.get('password', None)
    user = authenticate(username=name, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'app0/home.html')
        else:
            return HttpResponse(loader.get_template('app0/login.html').render({
                'info': 'user disabled.'
            }))
    else:
        return HttpResponse(loader.get_template('app0/login.html').render({
            'info': 'invalid password.'
        }))


def store_pdf(f, path):
    with open(path, 'wb+') as destination:
        # if f.multiple_chunks():
        #     for trunk in f.trunks():
        #         destination.write(trunk)
        # else:
        destination.write(f.read())


@csrf_exempt
@login_required
def upload(request):
    return render(request, 'app0/upload.html')


@csrf_exempt
@login_required
def do_upload(request):
    if request.method == 'POST':
        pdf = request.FILES.get('pdf')
        title = request.POST.get('title')
        summary = request.POST.get('summary')

        if not request.session.get('id'):
            return render(request, 'app0/index.html', {
                'info': 'login time-out.',
            })

        if title and pdf and re.match('^.+\.pdf', pdf.name):
            paper = PaperMetaInfo()
            paper.title = title
            paper.filepath = './pdf/' + pdf.name
            paper.summary = summary if summary else ""
            paper.save()

            upload = PaperUploadInfo()
            upload.paper_id = paper.id
            upload.uploader_id = request.session.get('id')

            store_pdf(pdf, './pdf/' + pdf.name)
        else:
            return render(request, 'app0/upload_success.html', {'info': 'upload failed.'})

    return render(request, 'app0/upload_success.html', {'info': 'upload success.'})




