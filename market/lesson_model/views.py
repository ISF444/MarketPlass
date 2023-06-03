from django.shortcuts import render

from .models import Category, Product, Person


# Create your views here.
def get_products(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    per = Person.objects.all()
    context = {"categories": categories, "products": products, "per": per}
    if request.method == 'POST':
        person = Person(login=request.POST.get('login'), password=request.POST.get('password'))
        person.save()
        pers = Person.objects.last()
        context['pers'] = pers
        print(person.pk)
    return render(request, 'page_products.html', context)


def get_all_product_category(request, id):
    categories = Category.objects.all()
    products = Product.objects.filter(categories_id=id)
    context = {"categories": categories, "products": products}
    return render(request, 'page_products.html', context)
