from django.shortcuts import get_object_or_404, render, redirect

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, url):
        obj = get_object_or_404(self.model, url__iexact=url)
        return render(request, self.template,
                      context={self.model.__name__.lower():obj})

class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template,
                      context={'form':form})

    def post(self, request):
        bounds_form = self.model_form(request.POST, request.FILES)
        if bounds_form.is_valid():
            new_post = bounds_form.save()
            return redirect(new_post)
        return render(request, self.template,
                      context={'form':bounds_form})


