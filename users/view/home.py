from django.contrib.auth.models import User
from users.models import Mail
from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {}    
            user_email = User.objects.get(id = request.user.id)
            data['allmail'] = Mail.get_all_mail(user_email.email)
            paginator = Paginator(data['allmail'],5)
            page_number = request.GET.get('page')
            data['page_obj'] = paginator.get_page(page_number)
            return render(request, 'blog/home.html',data)
        return render(request, 'blog/home.html')