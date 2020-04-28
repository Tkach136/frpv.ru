from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views import generic
from . models import Bid
from django.core.mail import EmailMessage, send_mail
from django.core import mail
from django.conf import settings
from django_db_logging import logging
from django.utils import timezone
from django.views import generic
from .models import Entry, Topic, Info
from .forms import BidForm
import datetime
from pprint import pformat

labels = ('name', 'OGRN', 'INN', 'chief', 'email', 'target',
          'price_project', 'implementation_period', 'sum_of_self_investments',
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

by_user = """
Заявка на финансирование компании %s (ИНН %s) успешно создана. 
Дата заявки: %s 
Наши менеджеры свяжутся с Вами в течение суток. 
С уважением, Региональный фонд развития промышленности Воронежской области.
+7 (473) 212-75-01
rfrp@govvrn.ru
"""


class IndexView(generic.ListView):
    template_name = 'frpv/index.html'
    context_object_name = 'entries'

    def get_queryset(self):
        """Возвращает последние 3 новости"""
        return Entry.objects.order_by('-date')[:3]


def index(request):
    return render(request, 'frpv/index.html')


def struktura(request):
    return render(request, 'frpv/struktura.html')


def ruko(request):
    return render(request, 'frpv/ruko.html')


def sovet(request):
    return render(request, 'frpv/sovet.html')


def expsovet(request):
    return render(request, 'frpv/expsovet.html')


def doki(request):
    return render(request, 'frpv/doki.html')

def reliz_proj(request):
    return render(request, 'frpv/reliz_proj.html')

def proj_razv(request):
    return render(request, 'frpv/proj_razv.html')

def kompl_izd(request):
    return render(request, 'frpv/kompl_izd.html')

def soglas(request):
    return render(request, 'frpv/soglas.html')


def about(request):
    data = Info.objects.get(blockname='about')
    return render(request, 'frpv/about.html', {'about': data})


def video(request):
    return render(request, 'frpv/video.html')


class EntryDetailView(generic.DetailView):
    model = Entry
    template_name = 'frpv/news.html'


class ArchiveListView(generic.ListView):
    template_name = 'frpv/arhiv.html'

    def get_queryset(self):
        return Entry.objects.all()


def navigator(request):
    fed = Info.objects.filter(header='navigator', group='федеральный')
    reg = Info.objects.filter(header='navigator', group='региональный')
    context = {'fed': fed, 'reg': reg}
    return render(request, 'frpv/navig.html', context=context)


def navDetail(request, blockname):
    # TODO добавить исключение при попытке доступа к несуществующей странице (раскомментить строку ниже)
    # qs = get_list_or_404(Info, group=blockname)
    qs = Info.objects.filter(group=blockname)

    if blockname.isupper():
        title = blockname
    else:
        title = blockname.capitalize()
    if not qs:
        title = 'Нет никаких данных по запросу "%s"' % title
    context = {'rows': qs, 'title': title}
    return render(request, 'frpv/nav_detail.html', context=context)


def archive(request):
    context = Entry.objects.all()
    return render(request, 'frpv/arhiv.html', {'entries': context})


def application(request):
    """определяет страницу заявки"""
    if request.method != 'POST':
        form = BidForm()
    elif request.POST.get('checkbox') == 'yes':
        form = BidForm(request.POST)
        if form.is_valid():
            form.save()
            topic = 'Заявка на финансирование компании %s , ИНН %s' % (form['name'].value(), form['INN'].value())
            email_body = ''
            for (key, value) in ROWS.items():
                row = value + ' : ' + str(form['%s' % key].value()) + '\n'
                email_body += row

            # email на сервер
            send_mail(
                topic,
                email_body,
                settings.EMAIL_HOST_USER,
                ['egrazor@yandex.ru']
            )

            # email пользователю
            date = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            msg_by_user = by_user % (form['name'].value(), form['INN'].value(), date)
            send_mail(
                topic,
                msg_by_user,
                settings.EMAIL_HOST_USER,
                [form['email'].value()]
            )
            msg = """
            <h1>Заявка на финансирование успешно создана</h1>
            <h3>Наши менеджеры свяжутся с Вами в течение суток</h3>
            <p></p><h3>С уважением, Региональный фонд развития промышленности Воронежской области !</h3>
            """
            return HttpResponse(msg)
            # return HttpResponseRedirect('/application')
    else:
        msg = """
        Вы не подтвердили своё согласие на обработку персональных данных.
        Вернитесь на предыдущую страницу и повторите попытку.
        """
        return HttpResponse(msg)

    context = {'form': form}
    return render(request, 'frpv/new_app.html', context)




