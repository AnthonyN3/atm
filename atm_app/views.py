from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from atm_app.user import User, get_user

def index(request):
    return render(request, 'index.html')
    
@csrf_exempt
def withdraw(request):

    if request.method == 'POST':
        input_amount = request.POST['currency_amount']
        if input_amount == '':
            input_amount = 0
        else:
            input_amount = int(input_amount)

        context = {
            'currency_amount': range(input_amount),
        }
        return render(request, 'thankyou.html', context)
    else:

        user = get_user(request.GET['account'], request.GET['pin'])
        if user == None:
            return render(request, 'index.html')
        else:
            context = {
                'account': user.account,
                'balance': user.balance
            }
            return render(request, 'withdraw.html', context)

def render(request, child, context={}):
    context['child'] = child
    template = loader.get_template('template.html')
    return HttpResponse(template.render(context, request))
