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
5. Run the application:

```bash
python app.py
```

## Features

- WhatsApp message handling via Twilio
- OpenAI-powered responses
- Flask web server for handling webhooks

## Note

Make sure to keep your API keys and tokens secure and never commit them to version control.
