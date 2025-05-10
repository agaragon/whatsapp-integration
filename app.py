from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize Twilio client
twilio_client = Client(
    os.getenv('TWILIO_ACCOUNT_SID'),
    os.getenv('TWILIO_AUTH_TOKEN')
)

# Initialize OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_openai_response(message):
    """Get response from OpenAI API"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful WhatsApp assistant."},
                {"role": "user", "content": message}
            ],
            max_tokens=150
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Error getting OpenAI response: {e}")
        return "I apologize, but I'm having trouble processing your request right now."

@app.route("/webhook", methods=['POST'])
def webhook():
    """Handle incoming WhatsApp messages"""
    # Get the message the user sent
    incoming_msg = request.values.get('Body', '').strip()
    
    # Get the sender's phone number
    sender = request.values.get('From', '')
    
    # Get response from OpenAI
    response_text = get_openai_response(incoming_msg)
    
    # Create Twilio response
    resp = MessagingResponse()
    resp.message(response_text)
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000) 