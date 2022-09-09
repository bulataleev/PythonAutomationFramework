# PythonAutomationFramework
pytest, webdriver with marks and fixtures  

#to run tests  
go to /test, pytest or pytest -m ui -s  

#to generate report (pip install pytest-html)  
pytest --html="results.html" or pytest --junitxml="results.xml"  

#to see all markers  
pytest --markers  

#to run specific test file on specific environment  
pytest test_env.py --env qa -v

