# E-commerce Payment API
This API allows payments to be made on an e-commerce website. It provides an interface to validate and process the user's credit card information.

## Prerequisites
- Python 3.x
- Fast API required libraries (can be installed using `pip install fastapi uvicorn`)
- Download the index.html, style.css (web page) and index.py (API) documents. Save them in the same folder (recommended). 


## Usage
1. Open a command prompt or terminal in the project directory.
2. Run the following command to start the development server: `python -m uvicorn index:app --reload` you should get a message similar to:

INFO: Will watch for changes in these directories: ['C:\Users...']
INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO: Started reloader process [27564] using StatReload
INFO: Started server process [34580] INFO: Waiting for application start [34580].
INFO: Waiting for application startup.
INFO: Application startup complete.


3. Access the html file and open the page in your web browser to open the payment interface.
4. Fill in the payment fields with your credit card information and click on the "Pay" button.
5. The API will validate the data entered and return a success message if the information is valid. Otherwise, it will display an error message.


## Contact us
If you have any questions or suggestions, feel free to contact orizaba_2@hotmail.com
