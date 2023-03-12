export PYTHONPATH := "${PYTHONPATH}:${CURDIR}/src"

PYTHON=. venv/bin/activate && python

init_venv:
	python3 -m venv venv

requirements: init_venv
	$(PYTHON) -m pip install -U pip
	$(PYTHON) -m pip install -r requirements.txt

run: requirements
	$(PYTHON) src/main.py
