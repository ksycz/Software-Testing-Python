### Environment Setup

1. Global Dependencies
    * [Install Python](https://www.python.org/downloads/)
    * Or Install Python with [Homebrew](http://brew.sh/)
    ```
    $ brew install python
    ```
    * Install [pip](https://pip.pypa.io/en/stable/installing/) for package installation
    
### The event_form_testing.py project
Testing a web form created by me at http://www.123contactform.com/form-3079673/Event-Form

Testing environment: Mozilla Firefox 55.0.3 (32-bits)
----
Used:
Python 3.6 with the unittest testing framework
Selenium Webdriver
Gecko driver for Mozilla Firefox (downloaded from https://github.com/mozilla/geckodriver/releases)
PyCharm Community Edition

Preconditions:
No specific  preconditions for web form fields.  I checked the fields for standard functionality and validation.

Test scenarios: 
- Checking form fields one by one.
- Checking the form submission.

Testing cases are commented in the event_form_testing.py (function = one test case).
Testing data are included in the event_form_testing.py

After performing each test case the driver closes the browser and opens a new window.

