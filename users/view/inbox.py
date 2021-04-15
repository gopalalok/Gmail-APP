from django.shortcuts import render, redirect , HttpResponseRedirect
from django.contrib.auth.models import User
from django.views import View
from users.models import Mail
from django.core.paginator import Paginator

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required, name='dispatch')
class InboxView(View):

    def get(self, request):
        data = {}
        user_email = User.objects.get(id = request.user.id)
        data['allmail'] = Mail.get_ham_mail(user_email.email)
        paginator = Paginator(data['allmail'],5)
        page_number = request.GET.get('page')
        data['page_obj'] = paginator.get_page(page_number)
        return render(request, 'users/inbox.html',data)
        

    