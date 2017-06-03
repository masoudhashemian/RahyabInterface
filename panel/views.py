from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from subprocess import check_output, CalledProcessError
from django.contrib.auth.decorators import login_required


@login_required
def main_page(request):
    template = loader.get_template('main_page.html')
    if request.method == 'POST':
        if request.POST.get("b1"):
            try:
                result = check_output('./hello.sh')
            except CalledProcessError as err:
                result = str(err.output).strip()
            print result
        if request.POST.get("b2"):
            print 'b2 press'

    return HttpResponse(template.render({}, request))