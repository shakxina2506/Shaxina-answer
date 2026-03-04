from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm


def feedback_list(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form=FeedbackForm()
    context = {
            'form':form,
            'feedback':Feedback.objects.filter(is_active=True).order_by('-created_at')
        }
    return render(request, 'feedback.html', context)