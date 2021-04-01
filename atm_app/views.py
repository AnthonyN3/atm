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
      return render(request, 'index.html', { 'incorrect_password': True })

@csrf_exempt
def withdraw(request):
  user = authenticate(request)
  if user == None:
    return redirect('/')

  if request.method == 'POST':
    del request.session['auth_token']
    input_amount = parse_input_amount(request.POST['currency_amount'])

    if input_amount == None:
      return render(request, 'invalid_withdrawal.html')
    else:
      
      amount_withdrawn = user.balance if input_amount > user.balance else input_amount
      user.balance -= amount_withdrawn

      context = {
        'currency_amount': range(amount_withdrawn),
        'amount_withdrawn': amount_withdrawn,
        'balance': user.balance
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

def parse_input_amount(input_amount):
  if input_amount == '':
    return None
  else:
    input_amount = int(input_amount)

  if input_amount < 0:
    return None
  else:
    return input_amount