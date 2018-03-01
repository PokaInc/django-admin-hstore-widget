# django-admin-hstore-field

FormField that properly render HStoreField Data in django Admin based on [djangoauts package](https://github.com/djangonauts/django-hstore)



## Requirements
 * Python 2.7, 3.4, 3.5, 3.6
 * Django 1.11, 2.0
 
 
Using pip:
```bash
pip install django-admin-hstore
```

## Usage

```python
from django_admin_store.forms import HStoreFormField

class MyModelAdminForm(forms.ModelForm):
    my_hstore_field = HStoreFormField()
    

```

## Result

![Rendered result](results.png)