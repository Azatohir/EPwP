from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Note, Topic

class DodajNotatkeView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'myapp/dodaj_notatke.html'
    fields = ['tytul', 'tresc']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('lista_notatek')

class AktualizujNotatkeView(UserPassesTestMixin, UpdateView):
    model = Note
    template_name = 'myapp/aktualizuj_notatke.html'
    fields = ['tytul', 'tresc']

    def test_func(self):
        return self.get_object().created_by == self.request.user

class UsunNotatkeView(UserPassesTestMixin, DeleteView):
    model = Note
    template_name = 'myapp/usun_notatke.html'
    success_url = reverse_lazy('lista_notatek')

    def test_func(self):
        note = self.get_object()
        return note.created_by == self.request.user or self.request.user.is_staff

class ListaNotatekView(ListView):
    model = Note
    template_name = 'myapp/lista_notatek.html'

class ListaTematowView(ListView):
    model = Topic
    template_name = 'myapp/lista_tematow.html'

class SzczegolyTematuView(DetailView):
    model = Topic
    template_name = 'myapp/szczegoly_tematu.html'

class DodajTematView(CreateView):
    model = Topic
    template_name = 'myapp/dodaj_temat.html'
    fields = ['title', 'description', 'parent', 'public']
    success_url = reverse_lazy('lista_tematow')

class AktualizujTematView(UpdateView):
    model = Topic
    template_name = 'myapp/aktualizuj_temat.html'
    fields = ['title', 'description', 'parent', 'public']
    success_url = reverse_lazy('lista_tematow')

class UsunTematView(DeleteView):
    model = Topic
    template_name = 'myapp/usun_temat.html'
    success_url = reverse_lazy('lista_tematow')