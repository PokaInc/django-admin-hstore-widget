import os
from setuptools import setup, find_packages

version = '1.0.1'


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


setup(
    name='django-admin-hstore-widget',
    version=version,
    description="Widget and Field to properly render HStore data in Django-Admin",
    keywords="django admin hstore render",
    author='Alexandre Dufour',
    author_email='adufour@poka.io',
    maintainer='Alexandre Dufour',
    maintainer_email='adufour@poka.io',
    url='https://github.com/PokaInc/django-admin-hstore-widget',
    packages=find_packages(),
    package_data=get_package_data('django_admin_hstore_widget'),
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    zip_safe=False,
)
