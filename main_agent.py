import os
import json
import requests
from dotenv import load_dotenv

from tools import message_operations

url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"

load_dotenv()
model_token = os.getenv("MODEL_API_TOKEN")
headers = {'Authorization': model_token, 'Content-Type': 'application/json'}

tool_declaration = {
    "type": "function",
    "function": {
        "name": "send_seatalk_message",
        "description": "send a message via SeaTalk webhook",
        "parameters": {"type": "object",
                       "properties": {"content": {"type": "string", "description": "the message content to send"}}}
    }
}

payload = {
    "model": "deepseek-v3-2-251201",
    "stream": False,
    "messages": [],
    "tools": [tool_declaration]
}

while True:
    # step 1: LLM handles the user input
    messages = input(">>> User: ")
    payload["messages"] = [{"role": "user", "content": messages}]
    response = requests.request("POST", url, headers=headers, json=payload)
    assistant_response = response.json()["choices"][0]["message"]["content"]
    print(f"<<< raw response: {response.json()}")

    # step 2: call the function if the LLM requests it
    tool_calls, tool_response = None, ""
    if "send_seatalk_message" in response.text:
        tool_calls = response.json()["choices"][0]["message"]["tool_calls"]
        tool_args = json.loads(tool_calls[0]["function"]["arguments"])
        tool_response = message_operations.send_seatalk_message(tool_args["content"])
        print(f"<<< tool_response: {tool_response}")

        # step 3: return the function response to the LLM
        payload["messages"] = [{"role": "user", "content": messages},
                               {"role": "assistant", "content": assistant_response, "tool_calls": tool_calls},
                               {"role": "tool", "content": tool_response, "tool_call_id": tool_calls[0]["id"]}]
        response = requests.request("POST", url, headers=headers, json=payload)
        final_response = response.json()["choices"][0]["message"]["content"]
        print(f"<<< final_response: {final_response}")
    else:
        print("<<< No function call in the response")