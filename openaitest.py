# openaitest.py
from openai import OpenAI
import os
# import config # Uncomment if you're loading from config.py

def test_openai_connection():
    """
    Tests the connection to the OpenAI API by requesting a simple chat completion.
    """
    try:
        # Option 1: Load API key from environment variable (RECOMMENDED)
        api_key = os.environ.get("OPENAI_API_KEY")

        # Option 2: Load API key from config.py (if you choose this method)
        # api_key = config.OPENAI_API_KEY

        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set or not found in config.py")

        client = OpenAI(api_key=api_key)

        print("Attempting a simple OpenAI chat completion...")
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Hello, is this test working?"}
            ]
        )

        response_content = chat_completion.choices[0].message.content
        print(f"OpenAI Test Successful! Response: {response_content[:50]}...") # Print first 50 chars
        return True

    except Exception as e:
        print(f"OpenAI Test Failed! An error occurred: {e}")
        return False

if __name__ == "__main__":
    test_openai_connection()