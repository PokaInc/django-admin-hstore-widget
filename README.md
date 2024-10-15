# django-admin-hstore-widget (Abandoned)

## This project is officially abandoned and won't receive any new updates. This repository will be archived as of January 2025
There's a hard fork of this project that is actively maintained and has more features. You can find more information [here](https://github.com/PokaInc/django-admin-hstore-widget/issues/27)

### New fork
[GitHub](https://github.com/PokaInc/django-admin-hstore-widget/issues/27)

[pypi](https://pypi.org/project/django-hstore-widget/)


---

FormField that properly render HStoreField Data in django Admin based on [djangoauts package](https://github.com/djangonauts/django-hstore)

[![Build Status](https://travis-ci.org/PokaInc/django-admin-hstore-widget.svg?branch=master)](https://travis-ci.org/PokaInc/django-admin-hstore-widget)


## Requirements
 * Python 2.7, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9
 * Django 1.11, 2.0, 2.1, 2.2, 3.0, 4.0
 
 
Using pip:
```bash
pip install django-admin-hstore-widget
```

## Installation

Add django_admin_hstore_widget to your INSTALLED_APPS ( in base.py )

## Usage

```python
# yourmodel/admin.py
from django.contrib import admin
from django import forms

from django_admin_hstore_widget.forms import HStoreFormField
from models import Yourmodel

class MyModelAdminForm(forms.ModelForm):
    my_hstore_field = HStoreFormField()
    
    class Meta:
       model = Yourmodel
       exclude = ()
    
@admin.register(Yourmodel)
class YourmodelAdmin(admin.ModelAdmin):
    form = MyModelAdminForm
    
```

## Result

![Rendered result](results.png)
