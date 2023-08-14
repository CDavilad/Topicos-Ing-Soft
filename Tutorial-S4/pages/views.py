from django.shortcuts import render
from django.views.generic import TemplateView

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