from django import forms
from django.test import TestCase
from django.contrib import admin
from django.contrib.auth.models import User


from django_admin_hstore_widget.forms import HStoreFormField

from .models import DataBag


class DataBagForm(forms.ModelForm):
    data = HStoreFormField()

    class Meta:
        model = DataBag
        fields = ('name', 'data')


class DataBagAdmin(admin.ModelAdmin):
    form = DataBagForm


admin.site.register(DataBag, DataBagAdmin)

class TestModel(TestCase):

    def _create_bags(self):
        alpha = DataBag.objects.create(name='alpha', data={'v': '1', 'v2': '3'})
        beta = DataBag.objects.create(name='beta', data={'v': '2', 'v2': '4'})
        return alpha, beta

    def test_admin_widget(self):
        alpha, beta = self._create_bags()

        # create admin user
        admin = User.objects.create(username='admin', password='tester', is_staff=True, is_superuser=True, is_active=True)
        admin.set_password('tester')
        admin.save()
        # login as admin
        user_login = self.client.login(username='admin', password='tester')
        self.assertTrue(user_login)