from django.shortcuts import render
from django.http import HttpResponseRedirect
from commingsoon.form import NewsletterForm
from django.contrib import messages
# Create your views here.
def Commingsoon_views(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Yor ticket submited successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Yor ticket dident submited.')
    form=NewsletterForm()
    return render(request,'soon/soon.html',{'form': form})


def handler404(request, exception):
    return HttpResponseRedirect("/")