# WhatsApp Agent with Twilio and OpenAI

This project creates a WhatsApp agent that uses Twilio for WhatsApp integration and OpenAI for natural language processing.

## Setup Instructions

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file with the following variables:

```
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_whatsapp_number
OPENAI_API_KEY=your_openai_api_key
```

3. Set up a Twilio account and get a WhatsApp-enabled phone number
4. Configure your Twilio WhatsApp sandbox or business account
   4.1 - You must configure the webhook endpoint to point to your server's webhook endpoint.
   4.2 - You can use ngrok to create a secure tunnel to your local development server, making it accessible via a public URL for testing webhook integrations
5. Run the application:

```bash
python app.py
```

## Features

- WhatsApp message handling via Twilio
- OpenAI-powered responses
- Flask web server for handling webhooks

## Running with ngrok

To expose your local server to the internet for testing webhook integrations:

1. Install ngrok from [ngrok.com](https://ngrok.com/download)
2. Sign up for a free ngrok account and get your authtoken
3. Configure ngrok with your authtoken:
   ```bash
   ngrok config add-authtoken your_auth_token
   ```
4. Start your Flask application:
   ```bash
   python app.py
   ```
5. In a new terminal, start ngrok:
   ```bash
   ngrok http 5000
   ```
6. Copy the ngrok URL (e.g., `https://xxxx-xx-xx-xxx-xx.ngrok.io`) and append `/webhook` to it
7. Set this URL as your webhook endpoint in your Twilio WhatsApp sandbox settings

Note: The ngrok URL changes each time you restart ngrok. Remember to update your Twilio webhook URL accordingly.
