from django.db import models


class Bid(models.Model):
    name = models.CharField(max_length=200)
    OGRN = models.IntegerField()
    INN = models.IntegerField(primary_key=True)
    chief = models.CharField(max_length=100)
    email = models.EmailField()
    target = models.TextField(blank=True, null=True)
    price_project = models.FloatField()
    implementation_period = models.DateField(blank=True, null=True)
    sum_of_self_investments = models.FloatField()
    loan_amount = models.FloatField()
    term_use_of_the_loan = models.SmallIntegerField()
    proposed_collateral = models.CharField(max_length=200)

    def __str__(self):
        return "id=%d, %s : %d" % (self.name.id, self.name, self.INN)

    class Meta:
        ordering = ['name']
