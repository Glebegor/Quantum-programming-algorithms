
# Commands to run
run:
	python3 main.py


# Quantum
run-quantum:
	python3 testquantum.py

# Packages
ipackages:
	pip install -r requirements.txt
cpackages:
	pip freeze > requirements.txt
