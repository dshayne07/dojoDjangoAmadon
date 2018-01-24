from django.shortcuts import render, redirect

def index(request):
    return render(request, 'store/index.html')

def buy(request):
    if 'list' not in request.session:
        request.session['list'] = {
            'counter':0,
            'sum':0.0,
            'price':0.0
        }

    price = 0
    if request.POST['id'] == '0':
        price = 19.99
    elif request.POST['id'] == '1':
        price = 29.99
    elif request.POST['id'] == '2':
        price = 4.99
    elif request.POST['id'] == '3':
        price = 49.99
    
    price*= int(request.POST['amount'])

    request.session['list']['counter']+=int(request.POST['amount'])
    request.session['list']['sum']+=price
    request.session['list']['price']=price
    request.session.modified = True
    print request.session['list']['price']

    return redirect('/store/checkout/')

def reset(request):
    request.session.clear()
    return redirect('/store/')

def checkout(request):
    return render(request, 'store/checkout.html')