#TemperatureAlertAgent

##Description of the Project
The TemperatureAlertAgent Web App is a python-based web application that allows users to input location and temperature range preferences. The app then monitors the temperature at the specified location and generates alerts if the temperature falls outside the specified range.

##Instructions to Run the Project
To run the Weather Alert Web App, follow these steps:

###Prerequisites
Python 3.x installed on your system.
Flask library installed. You can install it using pip install Flask.
Installation
Clone the repository to your local machine:

shell
Copy code
git clone <repository_url>
Navigate to the project directory:

shell
Copy code
cd weather-alert-web-app
Create a virtual environment (optional but recommended):

shell
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

shell
Copy code
venv\Scripts\activate
On macOS and Linux:

shell
Copy code
source venv/bin/activate
Install the required dependencies:

shell
Copy code
pip install -r requirements.txt
Running the Application
Start the Flask application:

shell
Copy code
flask run
By default, the app will run on http://127.0.0.1:5000/.

Open your web browser and navigate to the above URL to access the Weather Alert Web App.

Fill out the form with your location and temperature range preferences, and click the "Submit" button to receive alerts.

##Special Considerations
The app uses a simple subprocess to demonstrate the concept of monitoring temperature ranges. In a production environment, a more robust mechanism for monitoring and alerting should be implemented.
Make sure to replace <repository_url> with the actual URL of your Git repository if you are using version control.
