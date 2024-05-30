from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, render
# GENERIC VIEWS
from django.views.generic import View, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

# FORMS
from .forms import CompositionForm, CommentForm

# MODELS
from photos.models import Photo
from .models import Composition, Comment




class PhotoList(ListView):
    model = Photo
    template_name = "writing_exercise/list_photos.html"
    context_object_name = "photo"


class CompositionCreate(CreateView):
    model = Composition
    form_class = CompositionForm
    template_name = "writing_exercise/writing_page.html"
    context_object_name = "composition"
    http_method_names = ["post", "get"]

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        self.photo_id = kwargs.get('pk')
        print(f"&&&&&&&&&yeeeet{self.photo_id}")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        print("****CALLLLLLLL")
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.photo_id = self.photo_id
        obj.save()
        self.composition_id = obj.id 
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo_id = self.kwargs['pk']
        photo = get_object_or_404(Photo, id=photo_id)
        context['photo'] = photo
        return context

    def get_success_url(self):
        return reverse_lazy('writing:class_room', kwargs={'pk': self.composition_id})
    
    
class DeleteComposition(DeleteView):
    model = Composition
    template_name = "writing_exercise/delete_composition.html"
    def get_success_url(self):
        return reverse_lazy('writing:collection')


class MyCollection(ListView):
    model = Composition
    template_name = "writing_exercise/collection.html"
    context_object_name = "collections"
    
    def get_queryset(self):
        user_id = self.request.user.id
        if user_id:
            queryset = Composition.objects.filter(author=user_id)
        else:
            queryset = Composition.objects.none()
        return queryset
    
    
class WaitingList(ListView):
    model = Composition
    template_name = "writing_exercise/waiting_list.html"
    context_object_name = "collections"
    

class ClassRoom(CreateView):
    http_method_names = ['get', 'post']
    model = Comment
    template_name = "writing_exercise/class_room.html"
    form_class = CommentForm
    
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.composition_id = kwargs.get('pk')
        self.composition = get_object_or_404(Composition, id=self.composition_id)
        print(f"&&&&&&&&&yeeeet{self.composition_id}")
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        print("form validated")
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.commenting_to = self.composition
        obj.save()
        return super().form_valid(form)
    
    
    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['composition'] = self.composition
        context['comments'] = Comment.objects.filter(commenting_to=self.composition).order_by("id")
        # context['replies'] = Comment.objects.filter(parent=self.composition).order_by("id")
        context['comment_form'] = CommentForm()
        return context
    def get_success_url(self):
        # 成功後のリダイレクトURLを設定
        return reverse_lazy('writing:class_room', kwargs={'pk': self.composition_id})

#TODO This needs to change
class CommentUpdate(UpdateView):
    # http_method_names = ["post"]
    model = Comment
    template_name = "writing_exercise/comment_update.html"
    fields = ["like"]

    def post(self, request, *args, **kwargs):
        data = request.POST.dict()
        
        if "action" not in data:
            return HttpResponseBadRequest("Missing data")

        comment = self.get_object()
        print(comment.id)
        print(comment.like)

        # アクションに応じてlikeフィールドを更新
        if data['action'] == "like":
            comment.like = True
        elif data['action'] == "unlike":
            comment.like = False
        else:
            return HttpResponseBadRequest("Invalid action")

        # 更新を保存
        comment.save()

        return JsonResponse({
            'success': True,
            'like': comment.like,
            'comment_id': comment.id,
            'class': "text-red-500" if data['action'] == "like" else "text-gray-200"
        })
