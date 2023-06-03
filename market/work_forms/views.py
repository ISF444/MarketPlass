from django.shortcuts import render

from .forms import CarForm, Rassa


def get_page_all_forms(request):
    form = CarForm()
    context = {"form": form}
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
    return render(request, 'forms_page.html', context)


def get_people(request):
    form = Rassa()
    context = {"form": form}
    if request.method == "POST" and request.FILES:
        form = Rassa(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'people_page.html', context)

