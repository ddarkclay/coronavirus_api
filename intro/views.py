from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt

from PayTm import Checksum
from coronavirus_api.settings import MERCHANT_KEY, MID
from intro.models import SupportModel


def intro(request):
    return render(request, 'intro/index.html')


def graph(request):
    return render(request, 'intro/index2.html')


def contact(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
        return render(request, 'intro/index2.html')
    return render(request, 'intro/index.html')


def payment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        amount = request.POST.get('amount')
        payment_obj = SupportModel(name=name, email=email, mobile=mobile, amount=amount)
        payment_obj.save()
        param_dict = {

            'MID': MID,
            'ORDER_ID': str(payment_obj.id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'coronavirusapis',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'https://coronavirus-apis.herokuapp.com//handler-payment/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'intro/paytm.html', {'param_dict': param_dict})
    return render(request, 'intro/index.html')


@csrf_exempt
def handlePayment(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    try:
        if verify:
            payment = SupportModel.objects.get(id=response_dict['ORDERID'])
            if response_dict['RESPCODE'] == '01':
                payment.status = True
                payment.status_msg = response_dict['RESPMSG']
                print('Order Successful')
            else:
                payment.status_msg = response_dict['RESPMSG']
                print('Order was not successful because' + response_dict['RESPMSG'])
            payment.save()
        else:
            pass
    except SupportModel.DoesNotExist:
        pass
    return render(request, 'intro/paymentstatus.html', {'response': response_dict})
