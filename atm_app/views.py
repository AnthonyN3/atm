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
      return redirect('menu')
    else:
      print('login failed')
      return render(request, 'index.html', { 'incorrect_password': True })

@csrf_exempt
def menu(request):
  user = authenticate(request)
  if user == None:
    return redirect('/')

  if request.method == 'POST':
    goto = request.POST['type']
    if goto in {'/', 'withdraw', 'change_pin', 'deposit'}:
      if goto == '/':
        print('deleted session')
        del request.session['auth_token']
      return redirect(goto)
    else:
      return redirect('menu')
  else:
    context = {
      'account': user.account,
      'balance': user.balance
    }
    return render(request, 'menu.html', context)

@csrf_exempt
def change_pin(request):
  user = authenticate(request)
  if user == None:
    return redirect('/')

  if request.method == 'POST':
    if 'back' in request.POST:
      return redirect('menu')

    if (request.POST['old_pin'] == user.pin and request.POST['new_pin'] != ""):
      user.pin = request.POST['new_pin']
      return redirect('menu')
    else:
      context = {
        'account': user.account,
        'incorrect_pin': True,
      }
      return render(request, 'change_pin.html', context)
  else:
    context = {
      'account': user.account,
    }
    return render(request, 'change_pin.html', context)

@csrf_exempt
def deposit(request):
  user = authenticate(request)
  if user == None:
    return redirect('/')

  if request.method == 'POST':
    if 'back' in request.POST:
      return redirect('menu')

    input_amount = parse_input_amount(request.POST['currency_amount'])

    if input_amount == None or input_amount > 10000:
      return render(request, 'invalid_transaction.html')
    else:

      amount_deposited = 0 if input_amount < 0 else input_amount
      user.balance += amount_deposited
      print(amount_deposited)

      context = {
        'currency_amount': range(amount_deposited),
        'amount': amount_deposited,
        'type': 'Deposited',
        'balance': user.balance
      }
      return render(request, 'thankyou.html', context)

  else:
    context = {
      'account': user.account,
      'balance': user.balance,
    }
    return render(request, 'deposit.html', context)

@csrf_exempt
def withdraw(request):
  user = authenticate(request)
  if user == None:
    return redirect('/')

  if request.method == 'POST':
    if 'back' in request.POST:
      return redirect('menu')

    input_amount = parse_input_amount(request.POST['currency_amount'])

    if input_amount == None or input_amount > 2500:
      return render(request, 'invalid_transaction.html')
    else:
      
      amount_withdrawn = user.balance if input_amount > user.balance else input_amount
      user.balance -= amount_withdrawn

      context = {
        'currency_amount': range(amount_withdrawn),
        'amount': amount_withdrawn,
        'type': 'Withdrew',
        'balance': user.balance
      }
      return render(request, 'thankyou.html', context)

  else:
    context = {
      'account': user.account,
      'balance': user.balance,
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