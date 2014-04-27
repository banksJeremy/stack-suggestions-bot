default: test run

run: install-dependencies
	PYTHONPATH="src/:$(PYTHONPATH)" python -m stacksuggestionsbot \
		< settings/se-suggestion.cs1692x.moocforums.org-unauthenticated.json

test: install-dependencies
	PYTHONPATH="src/:$(PYTHONPATH)" python -m pytest

install-dependencies:
	rm -rf src/*.egg-info
	# also links our packages into the environment
	pip install -r requirements.txt
