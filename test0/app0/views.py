import os
import re

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt

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
def home(request):
    paper_ids = PaperUploadInfo.objects.order_by('-date')[:10]
    papers = [PaperMetaInfo.objects.get(id=id) for id in paper_ids]
    return render(request, 'app0/home.html', {
        'papers': papers
    })


@csrf_exempt
def register_success(request):
    name = request.POST.get('userName', None)
    password = request.POST.get('password', None)
    meta = UserMetaInfo(id=idshuffler.shuffle(), username=name, password=password)
    meta.save()
    return render(request, 'app0/register_success.html', {
        'info': 'success name: ' + name + ' password: ' + password
    })


def store_pdf(f, path):
    with open(path, 'wb+') as destination:
        # if f.multiple_chunks():
        #     for trunk in f.trunks():
        #         destination.write(trunk)
        # else:
        destination.write(f.read())


@csrf_exempt
def upload(request):
    return render(request, 'app0/upload.html')


@csrf_exempt
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




