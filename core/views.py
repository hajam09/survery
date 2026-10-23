from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from core.forms import SurveyForm
from core.models import Survey


@login_required
def listSurvey(request):
    surveys = Survey.objects.filter(owner=request.user)

    query = request.GET.get('q')
    active = request.GET.get('active')

    if query:
        surveys = surveys.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    if active in ['true', 'false']:
        surveys = surveys.filter(isActive=(active == 'true'))

    context = {
        'surveys': surveys,
        'query': query,
        'active': active,
    }
    return render(request, 'core/survey-list.html', context)


@login_required
def createSurvey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.owner = request.user
            survey.save()
            return redirect('core:survey-list-view')
    else:
        form = SurveyForm()

    return render(request, 'core/survey-create.html', {'form': form})


def viewSurvey(request, pk):
    survey = get_object_or_404(Survey, pk=pk)

    # If private, only owner can view
    if not survey.isActive and survey.owner != request.user:
        return redirect('core:survey-list-view')

    return render(request, 'core/survey-detail.html', {'survey': survey})


@login_required
def editSurvey(request, pk):
    survey = get_object_or_404(Survey, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = SurveyForm(request.POST, instance=survey)
        if form.is_valid():
            form.save()
            return redirect('core:survey-list-view')
    else:
        form = SurveyForm(instance=survey)

    return render(request, 'core/survey-edit.html', {'form': form, 'survey': survey})


@login_required
def deleteSurvey(request, pk):
    survey = get_object_or_404(Survey, pk=pk, owner=request.user)

    if request.method == 'POST':
        survey.delete()

    return redirect('core:survey-list-view')


@login_required
def textField(request, pk):
    survey = get_object_or_404(Survey, pk=pk, owner=request.user)
    return render(request, 'core/field-text.html', {'survey': survey})


@login_required
def passwordField(request, pk):
    pass


@login_required
def emailField(request, pk):
    pass


@login_required
def telephoneField(request, pk):
    pass


@login_required
def textAreaField(request, pk):
    pass


@login_required
def numberField(request, pk):
    pass


@login_required
def rangeField(request, pk):
    pass


@login_required
def checkBoxField(request, pk):
    pass


@login_required
def radioField(request, pk):
    pass


@login_required
def selectField(request, pk):
    pass


@login_required
def dateField(request, pk):
    pass


@login_required
def monthField(request, pk):
    pass


@login_required
def timeField(request, pk):
    pass


@login_required
def dateTimeField(request, pk):
    pass
