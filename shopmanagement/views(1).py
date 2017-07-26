from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.db.models import F
from shopmanagement.forms import UserForm
from shopmanagement.models import Item
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

def Home(request):
    return render(request, "Home.html")

@method_decorator(login_required,name='dispatch')
class ItemView(ListView):
    model = Item
    template_name = "item_list"

    def get_queryset(self):
        return Item.objects.all().filter(owner=self.request.user)
        # return super(ItemView, self).get_queryset()



@method_decorator(login_required,name='dispatch')
class ItemCreate(CreateView):
    model = Item
    fields = ['product_name','quantity','type','min_count','price_per_piece']
    success_url = "list/"
    def get_queryset(self):
        return Item.objects.all().filter(owner=self.request.user)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ItemCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('item-list')

@method_decorator(login_required,name='dispatch')
class ItemUpdate(UpdateView):
    model = Item
    fields = ['product_name','quantity','type','min_count','price_per_piece']

    def get_success_url(self):
        return reverse("item-list")

    def get_queryset(self):
        obj = Item.objects.all().filter(owner=self.request.user)
        return obj
        # return super(CardCreateView, self).get_queryset()

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ItemUpdate, self).form_valid(form)

@method_decorator(login_required,name='dispatch')
class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'items'

    def get_queryset(self):
        obj = Item.objects.all().filter(owner=self.request.user)
        return obj

@method_decorator(login_required,name='dispatch')
class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('item-list')

def adduser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            #login(new_user)
            # redirect, or however you want to get to the main view
            #return HttpResponseRedirect('homepage')
            return render(request, "Home.html")
    else:
        form = UserForm()

    return render(request, 'adduser.html', {'form': form})

