from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm


def feedback_list(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj=form.save()
            request.session['user_name'] = obj.name
            return redirect('thanks')
    else:
        form=FeedbackForm()
    context = {
            'form':form,
            'feedback':Feedback.objects.filter(is_active=True).order_by('-created_at')
        }
    return render(request, 'feedback.html', context)

def thanks(request):
    name = request.session.get('user_name')
    return render(request, 'thanks.html', {'name': name})
