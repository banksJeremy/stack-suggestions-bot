default: test run

run: install-dependencies
	PYTHONPATH="src/:$(PYTHONPATH)" python -m stacksuggestionsbot \
		< settings/se-suggestion.cs1692x.moocforums.org-unauthenticated.json

test: install-dependencies
	PYTHONPATH="src/:$(PYTHONPATH)" python -m pytest

install:
	rm -rf src/*.egg-info
	pip install .

install-dependencies:
	rm -rf src/*.egg-info
	pip install -qe .
