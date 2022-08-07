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
powerlinearlog:
	pytest -v -s --durations=0 main.py::test_power_linear_log
powerlog:
	pytest -v -s --durations=0 main.py::test_power_log
fibogold:
	pytest -v -s --durations=0 main.py::test_check_fibo_gold
fibomatrix:
	pytest -v -s --durations=0 main.py::test_check_fibo_matrix
