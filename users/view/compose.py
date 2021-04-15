from django.shortcuts import render, redirect , HttpResponseRedirect
import pickle
from django.views import View
from users.models import Mail
import os
import joblib




from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ComposeView(View):
    search_products = None
    def post(self, request):
        toemail = request.POST.get('toemail')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        filename1 = os.path.join(os.path.dirname(os.path.dirname(__file__)),'view/nlp_model.pkl')
        filename2 = os.path.join(os.path.dirname(os.path.dirname(__file__)),'view/tranform.pkl')
        clf = pickle.load(open(filename1, 'rb'))
        cv  = pickle.load(open(filename2,'rb'))

        data = [subject + message]
        vect = cv.transform(data).toarray()
        my_prediction = clf.predict(vect)
		
        # validation
        values = {
            'toemail':toemail,
            'subject':subject,
            'message':message
        }
        error_message = None
        usr = Mail(fromemail = request.user.email,
                            toemail=toemail,
                            subject=subject,
                            message=message,
                            label=my_prediction 
                            )
        error_message = self.validateUser(usr)
        
        if not error_message:
            usr.mailsave()
            return redirect('sent')
        else:
            data = {
                'error': error_message,
                'values': values
            }
            return render(request, 'users/compose.html', data)
        

    def get(self, request):
        return render(request, 'users/compose.html')

    def validateUser(self, usr):
        error_message = None
        if(usr.toemail == usr.fromemail):
            error_message = "This is your email please enter a valid email !!!"
        elif(not usr.toemail):
            error_message = "Email Required !!!"
        elif(Mail.isExists(usr.toemail)):
            error_message = "Enter a valid email !!!"
            

        return error_message