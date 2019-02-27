from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting, Minutes
from .forms import MeetingForm
from .forms import ResourceForm
from django.contrib.auth.decorators import login_required


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

def meetingdetail(request, id):
    details=get_object_or_404(Meeting, pk=id)
    # minutes_list=Meeting.objects.all()
    return render (request, 'club/details.html',{'details': details})   

# form view
@login_required 
def newMeeting(request):
    form=MeetingForm
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
            
    else:
        form=MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})            
           
def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')

@login_required 
def newresource(request):
    form=ResourceForm
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()

    else:
        form=ResourceForm()
    return render(request, 'club/newresource.html', {'form': form})  
def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')   


# def newMeeting(request):
#     form=MeetingForm
#     if request.method=='POST':
#         form=MeetingForm(request.POST)
#         if form.is_valid():
#             post=form.save(commit=True)
#             post.save()
#             form=MeetingForm()
            
#     else:
#         form=MeetingForm()
#     return render(request, 'club/newmeeting.html', {'form': form})            
# def newresource(request):
#     form=ResourceForm
#     if request.method=='POST':
#         form=ResourceForm(request.POST)
#         if form.is_valid():
#             post=form.save(commit=True)
#             post.save()
#             form=ResourceForm()

#     else:
#         form=ResourceForm()
#     return render(request, 'club/newresource.html', {'form': form})            
# def loginmessage(request):
#     return render(request, 'club/loginmessage.html')

# def logoutmessage(request):
#     return render(request, 'club/logoutmessage.html')
