from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from django.views import View
from .forms import BookForm
from .models import Book
# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(*args, **kwargs)
        context["title"] = "Add Book"
        context['list_book'] = Book.objects.all()

        return context


class BookAddView(View):
    template_name = "formbook.html"
    http_method_names = ['get', 'post']
    def get(self,request, *args, **kwargs):

        form = BookForm()
        context={
            'form':form
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self,request,*args, **kwargs):

        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            data_published = form.cleaned_data['data_published']
            number_of_page = form.cleaned_data['number_of_page']
            type_of_book = form.cleaned_data['type_of_book']

            saveBook = Book(
                title = title,
                author = author,
                data_published = data_published,
                number_of_page = number_of_page,
                type_of_book = type_of_book
            )
            saveBook.save()
            return HttpResponseRedirect("/")


        context = {
            'form': form
        }
        return render(request, template_name=self.template_name, context=context)


class BookEditView(View):
    template_name = "editformbook.html"
    http_method_names = ['get', 'post']
    def get(self,request,fid, *args, **kwargs):
        context={
            'book' : Book.objects.get(id=fid)
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self,request,*args, **kwargs):
        id = request.POST['id']
        if request.method == "POST":
            print(request.POST['title'])
            book = Book.objects.get(id=id)
            book.title = request.POST['title']
            book.author = request.POST['author']
            book.data_published = request.POST['data_published']
            book.number_of_page = request.POST['number_of_page']
            book.type_of_book = request.POST['type_of_book']
            book.save()
            return HttpResponseRedirect("/")


        context = {
            'book' : Book.objects.get(id=id)
        }
        return render(request, template_name=self.template_name, context=context)

class BookDeleteView(View):
    http_method_names = ['get']
    def get(self,request,fid,*args,**kwargs):
        isntance =Book.objects.get(id=fid)
        isntance.delete()
        return HttpResponseRedirect("/")



