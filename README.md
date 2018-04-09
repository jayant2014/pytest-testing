#Pytest help documentation

1. To run single test
	py.test -s -v test_API_demo.py

2. To run all test modules in the folder
	py.test -s -v

3. To run a single test case from a test module
	py.test -s -v test_API_demo.py::test_get_API

4. To create different reports
	py.test -s -v test_API_demo.py —junit-xml=report.xml
	py.test -s -v test_API_demo.py —html=report.html
	py.test -s -v test_API_demo.py --html=report.html --self-contained-html
