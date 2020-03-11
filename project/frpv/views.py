from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, response, JsonResponse
from django.views import generic
from . models import Bid
from django.core.mail import EmailMessage, send_mail
from django.core import mail
from django.conf import settings
from django_db_logging import logging
from django.utils import timezone
import json
from pprint import pformat

labels = ('name', 'OGRN', 'INN', 'chief', 'email', 'target',
          'price_project', 'implementation_period', 'sum_of_self_investmens',
          'loan_amount', 'term_use_of_the_loan', 'proposed_collateral',
          )

FORM = """
Наименование организации: $VALUE$
ОГРН: $VALUE$
ИНН: $VALUE$
Руководитель (ФИО, телефон): $VALUE$ 
email: $VALUE$ 
Цель и краткое описание проекта: $VALUE$
Общая стоимость проекта: $VALUE$ 
Срок реализации проекта: $VALUE$ 
Сумма собственных вложений: $VALUE$
Сумма запрашиваемого займа: $VALUE$
Срок пользования займа(месяцев): $VALUE$ 
Предлагаемое обеспечение: $VALUE$
"""

ROWS = {
    'name': 'Наименование организации',
    'OGRN': 'ОГРН',
    'INN': 'ИНН',
    'chief': 'Руководитель (ФИО, телефон)',
    'email': 'email',
    'target': 'Цель и краткое описание проекта',
    'price_project': 'Общая стоимость проекта',
    'implementation_period': 'Срок реализации проекта',
    'sum_of_self_investments': 'Сумма собственных вложений',
    'loan_amount': 'Сумма запрашиваемого займа',
    'term_use_of_the_loan': 'Срок пользования займа(месяцев)',
    'proposed_collateral': 'Предлагаемое обеспечение',
}

msg = """
Заявка успешно создана! 
Наши менеджеры свяжутся с Вами в самое ближайшее время. 
С уважением, Региональный фонд развития промышленности Воронежской области.
"""


def test_send(request):
    if request.method != 'POST':
        return HttpResponse('Вы ввели некорректные данные. Пожалуйста, попробуйте ещё раз.')
    elif request.method == 'POST':
        data = request.POST.get('test')
        # data = json.loads(data)
        send_mail('topic', data,
                  settings.EMAIL_HOST_USER,
                  ['egrazor@yandex.ru']
                  )
        return HttpResponse(data)


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
        # json_object = json.loads(bid.__dict__)
        with mail.get_connection() as connection:
            mail.EmailMessage(
                'Заявка',
                'message',
                'from',
                ['ezenkin@it-russ.com'],
                connection=connection,
            ).send()
        return HttpResponse("Заявка создана.")



