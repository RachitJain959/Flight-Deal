# Flight Deal Finder

Flight Deal Finder is a Python project designed to assist users in discovering the most affordable flight deals to their desired destinations within a six-month timeframe. The project leverages a combination of web scraping and API integrations to automate the process of identifying flights with significantly lower prices than expected.

## How it Works

1. **Automated Price Tracking:** The core idea is to replicate the manual process of repeatedly searching for flights on a daily basis. The program simulates this by automatically querying flight prices for various locations over a span of six months.

1. **Historical Data Analysis:** The program identifies instances where the flight prices drop significantly compared to historical data. For example, if a flight from Kolkata to Delhi usually ranges between ₹8000 to ₹10000, the program tracks the moments when the prices dip to ₹2000 or lower.

1. **User Preferences:** Users input their desired destinations and a price threshold (historically low price) into a Google Sheet. This data is then fetched and used to guide the program's search.

1. **API Integrations:** The project utilizes multiple APIs to gather data and facilitate notifications:

   - **Sheety API:** Fetches user data of destination cities & their contact information from Google Sheet. Updates the Google sheet with airports in those cities along with their IATA codes from Tequila API.
   - **Tequila API:** Provides real-time flight prices, real-time details of departing & arriving flights, details of airports along with their IATA codes.

   - **Twilio API:** Sends notifications to users via SMS or email whenever a flight deal that matches their criteria is found.

## How to Use

1. Update the Google Sheet with your preferred destinations the price threshold you're willing to pay, and your contact information.
1. Run the program, which automatically searches for the cheapest flight deals based on your preferences.
1. Once a deal meeting your criteria is identified, you'll receive a notification via SMS or email, allowing you to promptly book the deal.

## Technologies Used

- **Python**: Utilizes object-oriented programming concepts to structure the project.
- **Twilio API**: Facilitates notifications to users regarding flight deals via SMS or email.
- **Sheety API**: Manages data storage for different airports and their IATA codes.
- **Tequila API**: Provides detailed flight prices and deals information.

## Getting Started

1. Clone this repository.
1. Install the required Python packages using pip install -r requirements.txt.
1. Configure the necessary API keys and credentials in the designated files.
1. Update the Google Sheet with your preferred destinations and price threshold.
1. Run the Python script to initiate the flight deal search and notification process.

## Contribution

Feel free to contribute and enhance the project to make flight deal hunting more convenient and efficient!

_Note: This project is designed for educational and personal use only._
