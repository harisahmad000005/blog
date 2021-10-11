from django.shortcuts import redirect, render
from .models import Posts
from django.views.generic import ListView, DetailView
# Create your views here.

# def home_view(request):
#     post_obj= Posts.objects.all()
#     context = {
#         'posts': post_obj
#     }
#     return render(request,'index.html',context)


class HomeView(ListView):
    model=Posts
    template_name="index.html"
    context_object_name = "post_list"
    paginate_by=2

    def get_queryset(self):
        result = super(HomeView, self).get_queryset()
        filter_val = self.request.GET.get('search', '')
        if filter_val:
            result = Posts.objects.filter(active=filter_val)
        return result

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["filter_val"] = self.request.GET.get('search', '')
        return context

class PostDetailView(DetailView):
    model = Posts
    template_name="post/postDetailView.html"
    context_object_name = "post_object"