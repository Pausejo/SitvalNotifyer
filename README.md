# 🚗 ITV Appointment Checker 🔔
This Python script automates the process of checking for available ITV appointments in various stations in València, Spain. It uses Selenium for web scraping and automation, and the Sinch API for sending SMS notifications when appointments are available.

## 🛠️ Prerequisites
- Python 3.x
- Chrome WebDriver
- Sinch API credentials (Service Plan ID and API Token)

## 💾 Installation
1. Clone the repository.
2. Install the required Python packages: `pip install -r requirements.txt`
3. Create a free account into [Sinch](https://www.sinch.com/).

## ⚙️ Configuration
- `SINCH_SERVICE_PLAN_ID`: Your Sinch service plan ID.
- `SINCH_API_TOKEN`: Your Sinch API token.
- `SINCH_FROM`: Your Sinch phone number.
- `SMS_RECIPIENT`: The phone number to which you want to send the SMS notifications.
- `LOCATION`: The location for which appointments are being checked.
- `ITV_STATIONS`: List of ITV stations to check for appointments in selected location.
- `MONTH`: The month for which appointments are being checked.
- `PLATE_NUMBER`: The vehicle's plate number.

## 🚀 Run
To run the script, execute the following command in your terminal:
```
python itv_checker.py
```

csharp
## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
