"""
tools for message operations
"""
import requests
import json


def send_seatalk_message(content: str) -> str:
    """
    send a message via SeaTalk webhook
    Args:
        content: the message content to send
    Returns:
        tuple of (success: bool, message: str)
    """
    url = "https://openapi.seatalk.io/webhook/group/9ZnfSDqKSKuzabNYkYtM4Q"
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "tag": "text",
        "text": {
            "content": content
        }
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return f"Message sent successfully: {content}"
        else:
            return f"Failed to send message. Status code: {response.status_code}, Response: {response.text}"
    except Exception as e:
        return f"Error sending message: {str(e)}"