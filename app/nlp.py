import openai
from app.config import OPENAI_API_KEY
openai.api_keu = OPENAI_API_KEY
conversation = []

def handle_user_input(user_input):
    global conversation
    
    conversation.append({"role": "user","content":user_input.content})
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=conversation
        )
        ai_response = response['choices'][0]['messages']['content']
        conversation.append({"role":"assistant","content":ai_response})
        return ai_response
    except Exception as e:
        return f"Error: {str(e)}"