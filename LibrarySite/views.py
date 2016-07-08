from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Book
from django.http import HttpResponseRedirect
from .forms import RegistrationForm, LoginForm
from django.template import RequestContext
from blog.models import Post
from itertools import chain
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import myUser
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Create your views here.
def index(request):
    return render(request, 'LibrarySite/index.html', {})

def test(request):
    return render(request, 'LibrarySite/homePages/testPage.html', {})

def userRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'])
            # Allows to login
            user.save()

            userVar = myUser(user=user, firstName=form.cleaned_data['firstName'],
                             lastName = form.cleaned_data['lastName'],
                             birthday = form.cleaned_data['birthday'])
            userVar.save()

            return HttpResponseRedirect('/profile/')
        else:
            return render_to_response('LibrarySite/homePages/register.html', {'form': form}, context_instance=RequestContext(request))

    else:
        ''' User is not submitting the form, show them a blank registration form '''
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('LibrarySite/homePages/register.html', context, context_instance=RequestContext(request))

def search(request):
    if request.method == 'GET':
        try:
            q = request.GET['q'].lower()
            results =   Book.objects.filter(title__icontains=q) | \
                        Book.objects.filter(author__icontains=q)| \
                        Book.objects.filter(genre__icontains=q)| \
                        Book.objects.filter(description__icontains=q) | \
                        Book.objects.filter(subject__icontains=q) \
                    .order_by('id')
            posts = Post.objects.filter(title__icontains=q) | \
                    Post.objects.filter(text__icontains=q)
            fresults = list(chain(results,posts))
            bookhits = (Book.objects.filter(title__icontains=q) | \
                        Book.objects.filter(author__icontains=q)| \
                        Book.objects.filter(genre__icontains=q)| \
                        Book.objects.filter(description__icontains=q) | \
                        Book.objects.filter(subject__icontains=q)).count()
            bloghits = (Post.objects.filter(title__icontains=q) | \
                       Post.objects.filter(text__icontains=q)).count()
            context = {
                'results':fresults,
                'bookhits':bookhits,
                'bloghits':bloghits,
                'q':q
            }

            return render_to_response('LibrarySite/homePages/results.html', context)
        except KeyError:
            return render_to_response('LibrarySite/homePages/results.html')


@login_required
def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    return render_to_response('LibrarySite/homePages/profile.html', {}, context_instance=RequestContext(request))


def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            myUser = authenticate(username=username, password=password)
            if myUser is not None:
                login(request, myUser)
                return HttpResponseRedirect('/profile/')
            else:
                return HttpResponseRedirect('/login/')
        else:
            return render_to_response('LibrarySite/homePages/login.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = LoginForm()
        context = {'form': form }
        return render_to_response('LibrarySite/homePages/login.html', context, context_instance=RequestContext(request))

def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/')

def books(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 10)

    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        #first page
        books = paginator.page(1)
    except EmptyPage:
        #page out of range
        books = paginator.page(paginator.num_pages)

    return render(request, 'LibrarySite/homePages/books.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'LibrarySite/homePages/book_detail.html', {'book': book})

def news(request):
    return render(request, 'LibrarySite/homePages/news.html', {})
