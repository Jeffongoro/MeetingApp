from django.utils import timezone
from django.shortcuts import render, redirect
from .forms import MeetingForm
from .models import Meeting

# Dashboard

def dashboard(request):
    return render(request,'dashboard.html')

# Add Meeting

def create_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                meeting_instance = form.save(commit=False)
                meeting_instance.user = request.user  # The logged-in user
                meeting_instance.save()
                return redirect('retrieve-meeting')
            except Exception as error:
                print(error)
    else:
        form = MeetingForm()
    return render(request, 'create.html', {'form': form})

# Retrieve Upcoming Meetings

def retrieve_meeting(request):
    # meetings = Meeting.objects.all()
    meetings = Meeting.objects.filter(user=request.user, start_time__gt=timezone.now()).order_by('-start_time')
    return render(request,'retrieve.html', {'meetings': meetings})


# Past Meetings

def past_meetings(request):
    meetings = Meeting.objects.filter(user=request.user, end_time__lt=timezone.now()).order_by('-start_time')
    return render(request,'past.html', {'meetings': meetings})


# Update Meeting

def update_meeting(request, pk):
    meetings = Meeting.objects.get(id=pk)
    form = MeetingForm(instance=meetings)

    if request.method == 'POST':
        form = MeetingForm(request.POST, request.FILES, instance=meetings)
        if form.is_valid():
            form.save()
            return redirect('retrieve-meeting')

    context = {
        'meetings': meetings,
        'form': form,
    }
    return render(request, 'update.html', context)

# Delete Meeting

def delete_meeting(request, pk):
    meetings = Meeting.objects.get(id=pk)

    if request.method == 'POST':
        meetings.delete()
        return redirect('retrieve-meeting')

    context = {
        'meetings': meetings,
    }
    return render(request, 'remove.html', context)


