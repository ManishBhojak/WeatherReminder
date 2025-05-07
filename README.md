
# WeatherReminder

**WeatherReminder** is a Python script designed to send daily weather updates via email. It fetches the current weather information for a specified city and delivers it straight to your inbox, ensuring you're always prepared for the day's conditions.

## Features

* 🌤️ Retrieves real-time weather data for your chosen city.
* 📧 Sends daily weather summaries to your email.
* 🕒 Automates daily updates using task schedulers like `cron` or Windows Task Scheduler.

## Prerequisites

* Python 3.x
* An API key from [OpenWeatherMap](https://openweathermap.org/api)
* Access to an SMTP server (e.g., Gmail) for sending emails

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ManishBhojak/WeatherReminder.git
   cd WeatherReminder
   ```

2. **Install required packages:**

   Ensure you have the necessary Python packages installed. You can use `pip` to install them:

   ```bash
   pip install requests
   ```

   *(Note: If there are additional dependencies, please list them here.)*

## Configuration

Before running the script, configure the following settings:

1. **API Key:**

   Replace `'YOUR_API_KEY'` in the script with your actual OpenWeatherMap API key.

2. **Email Settings:**

   Update the script with your email credentials and SMTP server details:

   ```python
   sender_email = "your_email@example.com"
   receiver_email = "recipient_email@example.com"
   password = "your_email_password"
   smtp_server = "smtp.example.com"
   smtp_port = 587
   ```

   *(Ensure you handle your credentials securely and avoid hardcoding sensitive information.)*

3. **City Configuration:**

   Set your desired city for weather updates:

   ```python
   city = "Your_City_Name"
   ```

## Usage

Run the script using Python:

```bash
python weatherReminder.py
```

To automate daily execution:

* **On Unix/Linux:**

  Use `cron` to schedule the script. For example, to run daily at 7 AM:

  ```bash
  0 7 * * * /usr/bin/python3 /path/to/weatherReminder.py
  ```

* **On Windows:**

  Use Task Scheduler to create a daily task that runs the script at your preferred time.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

* [OpenWeatherMap](https://openweathermap.org/) for providing the weather API.
