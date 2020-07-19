from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView

from posts.forms import TagForm, PostForm
from posts.models import Post, Tag

from posts.utils import ObjectDetailMixin, ObjectCreateMixin

#CRUD

#==================READ===================


#this is generic
#class PostListView(ListView):
#    model = Post
#    template_name = 'posts/post_list.html'

class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'posts/post_list.html',
                      context={'posts': posts})


# this is generics
#class PostDetailView(DetailView):
#    model = Post
#    template_name = 'posts/post_detail.html'
#    slug_field = 'url'


class PostDetailView(ObjectDetailMixin, View):
    model = Post
    template = 'posts/post_detail.html'


class TagListView(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'posts/tags_list.html',
                      context={'tags':tags})

class TagDetailView(ObjectDetailMixin, View):
    model = Tag
    template = 'posts/tag_detail.html'




#============ CREATE ===============
class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'posts/tag_create.html'



class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'posts/post_create.html'

#======== UPDATE ============

class PostUpdate(UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    form_class = PostForm


class TagUpdate(View):
    def get(self, request, url):
        tag = Tag.objects.get(url__iexact=url)
        bound_form = TagForm(instance=tag)
        return render(request, 'posts/tag_update.html',context={'form':bound_form,
                                                                'tag':tag})
    def post(self, request, url):
        tag = Tag.objects.get(url__iexact=url)
        bound_form = TagForm(request.POST, instance=tag)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'posts/tag_update', context={'form':bound_form, 'tag':tag})


 #============= DELETE ==========
class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = 'tags/'
    template_name = 'tag_confirm_delete.html'
    login_url = 'login'

def post_delete(request, url):
    post = get_object_or_404(Post, url=url)
    post.delete()
    return redirect(reverse('post_list'))

#========== Search ========
def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'posts/search_results.html', context)
