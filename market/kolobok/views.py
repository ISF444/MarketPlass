from django.shortcuts import render


def get_kolobok_page(request):
    return render(request, "kolobok_page.html")

