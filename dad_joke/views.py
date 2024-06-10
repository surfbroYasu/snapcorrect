import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Joke, JokeComment, FavoriteJoke
from .forms import CommentForm

def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        joke_id = data.get("id")
        joke_content = data.get("joke")
        return joke_id, joke_content
    return None, None
  
@login_required
def joke_view(request):
    joke_id, joke_content = get_dad_joke()
    if joke_content:
        joke, created = Joke.objects.get_or_create(joke_id=joke_id, defaults={"content": joke_content})

        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.joke = joke
                comment.user = request.user
                comment.save()
                return redirect("dad_joke:joke")
        else:
            form = CommentForm()

        comments = JokeComment.objects.filter(joke=joke)
        is_favorite = FavoriteJoke.objects.filter(joke=joke, user=request.user).exists()

        context = {
            "joke": joke,
            "form": form,
            "comments": comments,
            "is_favorite": is_favorite,
        }
        return render(request, "dad_joke/joke.html", context)
    else:
        return render(request, "dad_joke/joke.html", {"error": "Failed to retrieve a joke."})


class AddFavoriteJoke(LoginRequiredMixin, CreateView):
    model = FavoriteJoke
    fields = '__all__'
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        joke_id = kwargs.get('joke_id')
        joke = get_object_or_404(Joke, joke_id=joke_id)
        favorite, created = FavoriteJoke.objects.get_or_create(joke=joke, user=request.user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('dad_joke:joke')