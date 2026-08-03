import cohere
import sys

# 1. API key
API_KEY = "YOUR_COHERE_API_KEY"

try:
    # 2. Init client
    co = cohere.Client(API_KEY)
except Exception as e:
    print(f"❌ Error connecting to Cohere: {e}")
    sys.exit()

print("="*60)
print("🤖 AI Assistant (Cohere) - English Mode")
print("Type 'exit' or 'quit' to end the conversation.")
print("="*60)

# Chat history
chat_history = []

while True:
    # User input
    user_input = input("\n>>> You: ")
    
    # Exit condition
    if user_input.lower() in ['خروج', 'exit', 'quit']:
        print("\n<<< Assistant: It was a pleasure talking to you. Goodbye! 👋")
        break
        
    # Skip empty input
    if not user_input.strip():
        continue

    try:
        # API request (Auto-selects default model)
        response = co.chat(
            message=user_input,
            preamble="You are a highly capable AI assistant. You MUST strictly reply in English only, regardless of the language the user speaks. Do not use any other language.",
            chat_history=chat_history
        )
        
        bot_reply = response.text
        print(f"<<< Assistant: {bot_reply}")
        
        # Update history
        chat_history.append({"role": "USER", "message": user_input})
        chat_history.append({"role": "CHATBOT", "message": bot_reply})
        
    except Exception as e:
        print(f"\n❌ Error connecting to the server: {e}")
