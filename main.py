# main.py
from openai import OpenAI
import os  # For environment variables


# import config # Uncomment if you're loading from config.py

def get_openai_client():
    """Initializes and returns the OpenAI client."""
    # Option 1: Load API key from environment variable (RECOMMENDED)
    api_key = os.environ.get("OPENAI_API_KEY")

    # Option 2: Load API key from config.py (if you choose this method)
    # api_key = config.OPENAI_API_KEY

    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set or not found in config.py")

    return OpenAI(api_key=api_key)


def chat_with_openai(prompt_message: str):
    """
    Sends a message to the OpenAI chat model and prints the response.
    """
    client = get_openai_client()

    print(f"User: {prompt_message}")
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can try "gpt-4o", "gpt-4", etc. if you have access
            messages=[
                {"role": "system", "content": "You are a helpful and concise assistant."},
                {"role": "user", "content": prompt_message}
            ]
        )

        assistant_response = chat_completion.choices[0].message.content
        print(f"Assistant: {assistant_response}")
        return assistant_response

    except Exception as e:
        print(f"An error occurred while communicating with OpenAI: {e}")
        return None


if __name__ == "__main__":
    # Example usage:
    print("--- Starting OpenAI Chat Example ---")

    # You can get input from the user:
    # user_input = input("Ask the AI something: ")
    # chat_with_openai(user_input)

    # Or use a predefined prompt:
    chat_with_openai("What is the capital of France?")
    print("\n")
    chat_with_openai("Tell me a short, inspiring quote.")

    print("\n--- OpenAI Chat Example Finished ---")

        # say(query)