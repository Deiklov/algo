power:
	pytest -v -s --durations=0 main.py::test_check_power
fiboexp:
	pytest -v -s --durations=0 main.py::test_check_fibo_exp
fibolinear:
	pytest -v -s --durations=0 main.py::test_check_fibo_linear
simplequadratic:
	pytest -v -s --durations=0 main.py::test_count_of_simple
full:
	pytest -v -s --durations=0 --timeout=10 main.py
