from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

class HomePageView(TemplateView): 
    template_name = 'pages/home.html'

class AboutPageView(TemplateView): 

    template_name = 'pages/about.html' 

    def get_context_data(self, **kwargs): 

        context = super().get_context_data(**kwargs) 

        context.update({ 

            "title": "About us - Online Store", 

            "subtitle": "About us", 

            "description": "This is an about page ...", 

            "author": "Developed by: Your Name", 

        }) 

        return context 
    
class ContactPageView(TemplateView): 

    template_name = 'pages/contact.html' 

    def get_context_data(self, **kwargs): 

        context = super().get_context_data(**kwargs) 

        context.update({ 

            "title": "Contact us - Online Store", 

            "subtitle": "Contact us", 

            "description": "Contacts", 

            "email": "E-mail: example@enterprise.com",

            "addres": "Addres: 742 Evergreen Terrace",

            "phone": "Phone number: 3000000000",

        }) 

        return context 
    
class Product: 

    products = [ 

        {"id":"1", "name":"TV", "description":"Best TV", "price":"103"}, 

        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":"101"}, 

        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":"95"}, 

        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":"50"} 

    ] 

class ProductIndexView(View): 

    template_name = 'products/products.html' 

 

    def get(self, request): 

        viewData = {} 

        viewData["title"] = "Products - Online Store" 

        viewData["subtitle"] =  "List of products" 

        viewData["products"] = Product.products 

 

        return render(request, self.template_name, viewData) 

class ProductShowView(View): 

        template_name = 'products/show.html' 

        def get(self, request, id): 
            if 1 <= int(id) <= len(Product.products): 
                viewData = {} 

                product = Product.products[int(id)-1] 
                
                viewData["title"] = product["name"] + " - Online Store" 

                viewData["subtitle"] =  product["name"] + " - Product information" 

                viewData["product"] = product 

                product['price'] = float(product['price'])

                return render(request, self.template_name, viewData)
            else:
                return HttpResponseRedirect(reverse('home'))
            
    