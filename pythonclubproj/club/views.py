from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting, Minutes

# Create your views here.
def index (request):
    return render(request, 'club/index.html')


def resources (request):
    resource_list=Resource.objects.all()
    # if you have a big table than you can select only some
    return render (request, 'club/resources.html',{'resource_list': resource_list})

def meetings (request):
    meeting_list=Meeting.objects.all()
    return render (request, 'club/meetings.html',{'meeting_list': meeting_list})

def minutes (request, id):
    minutes_list=get_object_or_404(Meeting, pk=id)
    # minutes_list=Meeting.objects.all()
    return render (request, 'club/minutes.html',{'minutes_list': minutes_list})    

