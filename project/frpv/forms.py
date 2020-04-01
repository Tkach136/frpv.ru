from django import forms
from . models import Bid


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        exclude = ('date',)
        labels = {
            'name': 'Полное наименование организации',
            'chief': 'Руководитель проекта: Ф.И.О., номер телефона',
            'email': 'Адрес электронной почты',
            'target': 'Цель и краткое описание проекта (Включая раздел вида экономической деятельности в рамках которой планируется проект для финансирования)',
            'price_project': 'Общая стоимость проекта',
            'implementation_period': 'Срок реализации проекта',
            'sum_of_self_investments': 'Сумма собственных вложений',
            'loan_amount': 'Сумма запрашиваемого займа',
        }

