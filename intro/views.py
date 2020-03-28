from http.client import HTTPResponse

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from PayTm import Checksum
from intro.models import SupportModel

MERCHANT_KEY = 'rKx0db2cc71VonCf'


def intro(request):
    return render(request, 'intro/index.html')


def graph(request):
    return render(request, 'intro/index2.html')


def contact(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
    return render(request, 'intro/index.html')


def payment(request):
    if request.method == 'POST':
        param_dict = {}
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # mobile = request.POST.get('mobile')
        # amount = request.POST.get('amount')
        # print('payment details : '+name, email, mobile, amount)
        # payment_obj = SupportModel(name=name, email=email, mobile=mobile, amount=amount)
        # payment_obj.save()
        # param_dict = {
        #
        #     'MID': 'QStzkN37825458068760',
        #     'ORDER_ID': str(payment_obj.id),
        #     'TXN_AMOUNT': str(amount),
        #     'CUST_ID': email,
        #     'INDUSTRY_TYPE_ID': 'Retail',
        #     'WEBSITE': 'coronavirus-apis',
        #     'CHANNEL_ID': 'WEB',
        #     'CALLBACK_URL': 'http://127.0.0.1:8000/handler-payment/',
        # }
        # param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        # print(param_dict)
        return render(request, 'intro/paytm.html', {'param_dict': param_dict})
    return render(request, 'intro/index.html')


@csrf_exempt
def handlePayment(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('Order Successful')
        else:
            print('Order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})