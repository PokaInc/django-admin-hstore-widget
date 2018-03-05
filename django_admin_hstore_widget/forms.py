import json
from django.contrib.postgres.forms import HStoreField

from .widgets import HStoreFormWidget


class HStoreFormField(HStoreField):
    widget = HStoreFormWidget

    def clean(self, value):
        return json.loads(value)
