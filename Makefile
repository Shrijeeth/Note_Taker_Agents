install:
	pip install -r requirements.txt

run:
	python main.py

lint:
	python -m pylint $(shell git ls-files --modified --others '*.py' --exclude-standard)

auto-lint:
	python -m black --safe $(shell git ls-files --modified --others '*.py' --exclude-standard)
