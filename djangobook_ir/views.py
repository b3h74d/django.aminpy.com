from django.shortcuts import render_to_response
from django.template.context import RequestContext


def index(request):
    return render_to_response('index.html',
                              context_instance=RequestContext(request))

def toc(request):
    return render_to_response('toc.html',
                              context_instance=RequestContext(request))


def contact_us(request):
    return render_to_response('contact_us.html',
                              context_instance=RequestContext(request))


def about_book(request):
    return render_to_response('about_book.html',
                              context_instance=RequestContext(request))


def controller(request, number):
    return render_to_response("chapter%s.html" % number,
                              context_instance=RequestContext(request))
