Name: Philip Turk; JHED ID pturk1

Module Info: Module 4, Testing and Documentation, due 2025_06_15

Approach and Notes:

2025_06_12:
- Set up appropriate folder structure and build all my tests (*test_integration.py*, *test_order.py*, *test_pizza.py*).
- Add *pytest.ini* to define pytest markers.
- Add Order (*order.py*) and Pizza (*pizza.py*) classes for managing pizza orders and cost calculations.

2025_06_13:
- Finished building out Sphinx-generated HTML using `sphinx_rtd_theme` theme.

2025_06_14:
- Enhance documentation in Order and Pizza classes; edit Sphinx-generated HTML documentation

Known Bugs and Potential Issues:

2025_06_13: Running `PYTHONPATH=. pytest --cov=src --cov-report term-missing tests/`, I hit 97% coverage. The reason it is not perfect is because of Line 26 in *pizza.py*:
- I'm missing only the error branch in `Pizza.__init__()`.
- My scripts are still fully tested; this is just defensive code.
- I could hit 100% coverage with another small test to trigger a "non-mozzarella cheese" error.
