from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

class LoginRequiredMixin(object):
    @method_decorator(login_required, name='dispatch')
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
            


# Create your views here.
class HomeView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'registration/index.html'
    queryset = User.objects.all()