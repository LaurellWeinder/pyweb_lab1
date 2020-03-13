from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


class AboutPage(View):
    def get(self, request):
        return render(request, template_name='about.html')

    def post(self):
        pass


class BlogPage(View):
    def get(self, request):
        return render(request, template_name='blog.html')


class BlogSinglePage(View):
    def get(self, request):
        return render(request, template_name='blog-single.html')


class CartPage(View):
    def get(self, request):
        return render(request, template_name='cart.html')


class CheckoutPage(View):
    def get(self, request):
        return render(request, template_name='checkout.html')


class ContactPage(View):
    def get(self, request):
        return render(request, template_name='contact.html')


class DefaultPage(View):

    def get(self, request):
        return render(request, template_name='index.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key} : {value} <br>'
        html += '</html></body>'
        return HttpResponse(html)


class MenuPage(View):
    def get(self, request):
        return render(request, template_name='menu.html')

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key} : {value} <br>'
        html += '</html></body>'
        return HttpResponse(html)


class ProductPage(View):
    def get(self, request):
        return render(request, template_name='product-single.html')


class ServicesPage(View):
    def get(self, request):
        return render(request, template_name='services.html')


class ShopPage(View):
    def get(self, request):
        return render(request, template_name='shop.html')
