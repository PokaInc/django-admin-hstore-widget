from django import forms
from django.urls import reverse
from django.test import TestCase
from django.contrib import admin
from django.contrib.auth.models import User


from django_admin_hstore_widget.forms import HStoreFormField

from .models import Cat


class CatForm(forms.ModelForm):
    data = HStoreFormField()

    class Meta:
        model = Cat
        fields = ('name', 'data')


class CatAdmin(admin.ModelAdmin):
    form = CatForm


admin.site.register(Cat, CatAdmin)


class TestModel(TestCase):

    ADMIN_USERNAME = 'murphy'
    ADMIN_PASSWORD = 'cat'

    def _create_admin_user(self):
        admin = User.objects.create(
            username=self.ADMIN_USERNAME,
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        admin.set_password(self.ADMIN_PASSWORD)
        admin.save()

    def _login(self):
        self.client.login(username=self.ADMIN_USERNAME, password=self.ADMIN_PASSWORD)

    def test__hstore_field_edit_view__render(self):
        self._create_admin_user()
        self._login()

        cat = Cat.objects.create(name='Murphy', data={'race': '', 'gender': 'male'})
        url = reverse('admin:tests_cat_change', args=(cat.pk,))
        edit_view_response = self.client.get(url)

        self.assertEqual(edit_view_response.status_code, 200)

        # If the template is rendered with the django-admin-hstore-widget this class will be added to the textarea
        self.assertContains(edit_view_response, 'class="hstore-original-textarea"')

    def test__hstore_field_add_view__render(self):
        self._create_admin_user()
        self._login()

        url = reverse('admin:tests_cat_add')
        edit_view_response = self.client.get(url)

        self.assertEqual(edit_view_response.status_code, 200)
        # If the template is rendered with the django-admin-hstore-widget this class will be added to the textarea
        self.assertContains(edit_view_response, 'class="hstore-original-textarea"')
