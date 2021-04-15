from django.shortcuts import render, redirect , HttpResponseRedirect
from users.models import Mail
from django.views import View
from django.core.paginator import Paginator

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required, name='dispatch')
class SearchView(View):
    search_res = None
    def post(self, request):
        pass

    def get(self, request):
        
        query = request.GET.get('query')
        if query:
            if len(query) > 50:
                products = Mail.objects.none()
            else:
                mail_subject = Mail.objects.filter(toemail = request.user.email).filter(subject__icontains = query)
                mail_fromemail = Mail.objects.filter(toemail = request.user.email).filter(fromemail__icontains = query)
                mail_message = Mail.objects.filter(toemail = request.user.email).filter(message__icontains = query)
                SearchView.search_res = mail_subject.union(mail_fromemail)
                SearchView.search_res = SearchView.search_res.union(mail_message)
        
        total_res = SearchView.search_res
        paginator = Paginator(SearchView.search_res,5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {'allmail':SearchView.search_res,'query':query,'page_obj':page_obj,'total_res':total_res}
        return render(request, 'users/search.html',data)