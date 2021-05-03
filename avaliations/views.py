from django.contrib import messages
from django.db.models import Avg, Max, Min, Sum
from django.urls import reverse_lazy, reverse
from .models import Avaliation, Account
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from .forms import CreateForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect


# class HomeView(ListView):
#   model = Avaliation
#  template_name = 'home.html'

# def get_context_data(self, *args, **kwargs):
# identfy = get_object_or_404(Avaliation, id = self.kwargs[])
# context["total_likes"] = total_likes
# return context

class HomeView(ListView):
    model = Avaliation
    template_name = 'home.html'


class AvaliationDetailView(DetailView):

    model = Avaliation
    template_name = '../templates/avaliations/avaliation_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AvaliationDetailView,
                        self).get_context_data(*args, **kwargs)

        identfy = get_object_or_404(Avaliation, id=self.kwargs['pk'])
        total_likes = identfy.total_likes()

        liked = False
        if identfy.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


def createForm(request):
    try:
        author = Account.object.get(pk=request.user.id)
    except:
        return redirect('/login')
    author.save()

    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.instance.author_id = request.user.id
            form.save()
            return redirect('home')
        else:
            return render(request, '../templates/avaliations/createavaliation.html', {'form': form})

    else:
        form = CreateForm()
        return render(request, '../templates/avaliations/createavaliation.html', {'form': form})


def updateForm(request, pk):
    edit = Avaliation.objects.get(id=pk)
    form = CreateForm(instance=edit)

    if request.method == 'POST':
        form = CreateForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return (redirect('home'))
        else:
            return render(request, '../templates/avaliations/createavaliation.html', context)

    context = {'form': form}
    return render(request, '../templates/avaliations/createavaliation.html', context)


def deleteForm(request, pk):
    delete = Avaliation.objects.get(id=pk)

    if request.method == "POST":
        delete.delete()
        return redirect('/')

    context = {'item': delete}
    return render(request, '../templates/avaliations/deleteavaliation.html', context)


def likeView(request, pk):
    avaliation = get_object_or_404(
        Avaliation, id=request.POST.get('avaliation_id'))
    liked = False
    if avaliation.likes.filter(id=request.user.id).exists():
        avaliation.likes.remove(request.user)
        liked = False
    else:
        avaliation.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('avaliationDetail', args=[str(pk)]))


def recommendationAvaliation(request):
    average = Avaliation.objects.all().aggregate(Avg('ratingAvaliation'))

    avaliationListGreater = Avaliation.objects.exclude(
        ratingAvaliation__lte=average['ratingAvaliation__avg'])[:6]
    avaliationListWorse = Avaliation.objects.exclude(
        ratingAvaliation__gte=average['ratingAvaliation__avg'])[:6]

    return render(request, '../templates/home.html', {'avaliationsGreater': avaliationListGreater, 'average': average['ratingAvaliation__avg'], 'avaliationsWorse': avaliationListWorse})


def searchAvaliations(request):

    if request.method == "POST":

        search = request.POST['search']
        users_search = Avaliation.objects.filter(
            store_instagram__contains=search)

        return render(request, '../templates/avaliations/list_avaliation.html', {'search': search, 'users_search': users_search})
    else:
        return render(request, '../templates/avaliations/list_avaliation.html', {})


def CategoryView(request, cats):
    category_avaliations = Avaliation.objects.filter(category=cats)
    return render(request, '../templates/categories/categories.html', {'cats': cats.title(), 'category_avaliations': category_avaliations})


def userAvaliations(request):
    avaliations = Avaliation.objects.all()
    avaliations = avaliations.filter(author_id=request.user.id)
    for avaliation in avaliations:
        print(avaliation.titleAvaliation)
    return render(request, 'profile/profile.html', {"avaliations": avaliations})
