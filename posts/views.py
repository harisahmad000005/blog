from django.contrib.auth.models import User
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import PostComments, Posts
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import PostsModelForm
# Create your views here.
class HomeView(ListView):
    model=Posts
    ordering = ['-id']
    template_name="home.html"
    context_object_name = "post_list"
    paginate_by=7
    def get_queryset(self):
        result = super(HomeView, self).get_queryset()
        filter_val = self.request.GET.get('search', '')
        user_val = self.request.GET.get('user', '')
        if filter_val:
            result = Posts.objects.filter(active=filter_val)
        return result

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        user = self.request.user.is_superuser
        if user:
            context['users'] = User.objects.all().exclude(is_superuser=True)
        context["filter_val"] = self.request.GET.get('search', '')
        return context

class PostDetailView(DetailView):
    model = Posts
    template_name="post/postDetailView.html"
    context_object_name = "post_object"
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context['comments_list'] = PostComments.objects.filter(post_id=self.kwargs['pk'])
        return context
class PostCreateView(CreateView):
    model = Posts
    form_class = PostsModelForm
    success_url = 'post/'
    template_name="post/postCreateView.html"
    def form_valid(self, form):
        form.instance.author_name = self.request.user
        super().form_valid(form)
        return redirect(self.object.get_absolute_url())


class PostUpdateView(UpdateView):
    model = Posts
    form_class = PostsModelForm
    template_name="post/postCreateView.html"
    def get_success_url(self):
        return redirect(self.object.get_absolute_url())



def post_comment(request):
    if request.method=="POST":
        print("-------------------------------")
    return JsonResponse({'Message':"WORKING"})
