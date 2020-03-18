from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.template import loader
from .models import Books
from django.shortcuts import get_object_or_404, render
import requests

booklist = [
    {
    'author_first_name':'Toni',
    'author_last_name':'Morrison',
    'book_title': 'Beloved',
    'list_pub_date':'March 16 2020'
    },
    {
    'author_first_name':'Haruki',
    'author_last_name':'Murakami',
    'book_title': '1Q84',
    'list_pub_date':'March 16 2020'
    }
]

def index(request):
    context = {
        'booklist': Books.objects.all()
    }
    return render(request, 'listApp/index.html', context)

class BooksListView(ListView):

    model = Books
    template_name = 'listApp/index.html'
    context_object_name = 'booklist'
    ordering = ['-list_pub_date']

class BooksDetailView(DetailView):

    model = Books

class BooksCreateView(CreateView):
    model = Books
    fields = ['author_first_name', 'author_last_name', 'book_title']

    def form_vaild(self, form):
        return super().form_vaild(form)
    #
    # def post(self, request):
    #     author_first_name = request.POST['author_first_name']
    #     author_last_name = request.POST['author_last_name']
    #     book_title = request.POST['book_title']

class BooksUpdateView(UpdateView):
    model = Books
    fields = ['author_first_name', 'author_last_name', 'book_title']

    def form_vaild(self, form):
        return super().form_vaild(form)

class BooksDeleteView(DeleteView):
    model = Books
    success_url = '/listApp/'

def listen():
    # return render_template('get_voice.html')
    # Speech to text

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        print('audio', audio)
