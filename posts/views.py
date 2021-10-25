from django.contrib.auth.models import User
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import PostComments, Posts
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import PostsModelForm
import re

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
        context['comments_list'] = PostComments.objects.filter(post_id=self.kwargs['pk']).order_by('-id')
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
        # return reverse('postDetail', kwargs={"pk":self.kwargs["pk"]})  
        return self.object.get_absolute_url()


def post_comment(request):
    if request.method=="POST":
        comment = request.POST.get('comment', '')
        post_id = request.POST.get('post_id', '')
        new_comment =PostComments.objects.create(post_id=post_id,comment=comment,name=request.user)
        del new_comment.__dict__['_state']
        new_comment_data = {
            'new_comment': new_comment.__dict__ ,
             'user' : request.user.username
                   }
    return JsonResponse(new_comment_data)

def post_comment_update_delete(request):
    if request.method=="POST":
        comment = request.POST.get('comment', '')
        comment_id_str = request.POST.get('comment_id', '')
        if comment_id_str :
            comment_id = int(re.sub("[^0-9]", "", comment_id_str))
            if comment:
                PostComments.objects.filter(id=comment_id).update(comment=comment)
                new_comment_data = {
                "massage": "Successfully Updated",
                "comment":comment,
                "comment_id": comment_id_str}
            else:
                PostComments.objects.filter(id=comment_id).delete()
                new_comment_data = {
                "massage": "Successfully Deleted",
                'comment_card_delete' : f"comment_card_delete{comment_id}"
                 }
        else:
            new_comment_data = {
            "massage": "Something Went Worng",
                 }

    return JsonResponse(new_comment_data)
