from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from contactus.forms import ContactForm


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/")

    else:
        form = ContactForm()

    render_dict = {
        "form": form,
    }

    return render_to_response("contact_us.html", render_dict,
                              context_instance=RequestContext(request))
