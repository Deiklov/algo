runsimple:
	pytest -v -s --durations=0 main.py::test_check_power
runfibo:
	pytest -v -s --durations=0 main.py::test_check_fibo
