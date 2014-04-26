run: install-dependencies
	PYTHONPATH="src/:$(PYTHONPATH)" python -m stacksuggestionsbot

install-dependencies:
	pip install -qr requirements.txt
