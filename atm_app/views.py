from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from atm_app.user import User, login, authenticate

@csrf_exempt
def index(request):
  if request.method != 'POST':
    return render(request, 'index.html')
  else:
    if login(request.POST['account'], request.POST['pin'], request):
      print('login successful')
      return redirect('withdraw')
    else:
      print('login failed')
      return render(request, 'index.html')

@csrf_exempt
def withdraw(request):
  user = authenticate(request)
  if user == None:
    return redirect('/')

  if request.method == 'POST':
    input_amount = request.POST['currency_amount']
    if input_amount == '':
      input_amount = 0
    else:
      input_amount = int(input_amount)

      user.balance -= input_amount
      context = {
        'currency_amount': range(input_amount),
      }
      return render(request, 'thankyou.html', context)

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
