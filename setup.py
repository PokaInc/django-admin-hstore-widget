from setuptools import setup, find_packages

version = '1.0.0'

setup(
    name='django-admin-hstore',
    version=version,
    description="Widget and Field to properly render HStore data in Django-Admin",
    keywords="django admin hstore render",
    author='Alexandre Dufour',
    author_email='adufour@poka.io',
    maintainer='Alexandre Dufour',
    maintainer_email='adufour@poka.io',
    url='https://github.com/PokaInc/django-admin-hstore',
    packages=find_packages(),
    include_package_data=True,
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
