from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from openai import OpenAI

import os
import json

# Initialize Twilio client
twilio_client = Client(
    os.environ['TWILIO_ACCOUNT_SID'],
    os.environ['TWILIO_AUTH_TOKEN']
)
print(os.environ['TWILIO_ACCOUNT_SID'])
print(os.environ['TWILIO_AUTH_TOKEN'])

def get_openai_response(message):
    """Get response from OpenAI API"""
    try:
        client = OpenAI(
            # This is the default and can be omitted
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
        response = client.responses.create(
            model="gpt-3.5-turbo",
            instructions="You will translate the message to italian.",
            input=message
        )
        return response.output_text
    except Exception as e:
        print(f"Error getting OpenAI response: {e}")
        return "I apologize, but I'm having trouble processing your request right now."

def lambda_handler(event, context):
    """AWS Lambda handler function"""
    try:
        # Parse the incoming request body
        print(event)
        print(event['body'])
        print(context)
        body = json.loads(event['body'])
        print(body)
        body = json.loads(body['body'])
        print(body)
        # print(body.get('body'))
        # Get the message the user sent
        incoming_msg = body.get('Body', '').strip()
        # Get the sender's phone number
        sender = body.get('From', '')
        
        # Get response from OpenAI
        print(f"Incoming message: {incoming_msg}")
        response_text = get_openai_response(incoming_msg)
        
        # Create Twilio response
        resp = MessagingResponse()
        print(resp)
        print(resp.message(response_text))
        
        # Return the response in the format expected by API Gateway
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/xml'
            },
            'body': str(resp)
        }
    except Exception as e:
        print(f"Error processing request: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error'})
        } 