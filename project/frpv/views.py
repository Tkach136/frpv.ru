from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, response
from django.views import generic
from . models import Bid
from django_db_logging import logging
from time import timezone


labels = ('name', 'OGRN', 'INN', 'chief', 'email', 'target',
          'price_project', 'implementation_period', 'sum_of_self_investmens',
          'loan_amount', 'term_use_of_the_loan', 'proposed_collateral',
          )


def index(request):
    content = request.headers.items()
    return HttpResponse(content)


def application(request):
    context = {'labels': labels}
    return render(request, 'frpv/application.html', context)


def send(request):
    if request.method != 'POST':
        return HttpResponse('Вы ввели некорректные данные. Пожалуйста, попробуйте ещё раз.')
    elif request.method == 'POST':
        data = request.headers.items()
        bid = Bid(
            name=data['name'],
            OGRN=data['OGRN'],
            INN=data['INN'],
            chief=data['chief'],
            email=data['email'],
            target=data['target'],
            price_project=data['price_project'],
            implementation_period=data['implementation_period'],
            sum_of_self_investmens=data['sum_of_self_investments'],
            loan_amount=data['loan_amount'],
            term_use_of_the_loan=data['term_use_of_the_loan'],
            proposed_collateral=data['proposed_collateral']
        )
        if bid.is_valid:
            bid.save()
            logging('%s была создана Заявка № %d компании %s , ИНН %d на сумму %d'
                    % (timezone.now(), bid.id, bid.name, bid.INN, bid.loan_amount)
            )
        return HttpResponse("Пук, моделька отправляется почтой")
    # TODO моделька отправляется почтой