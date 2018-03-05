.PHONY: clean, build

deps-maintainer:
	pip install -r ./requirements/maintainer.txt

check:
	flake8 django_admin_hstore_widget/

clean:
	rm -rfv build
	rm -rfv dist
	rm -rfv django_admin_hstore_widget.egg-info

build:
	python setup.py sdist

upload: clean build
	twine upload dist/*
