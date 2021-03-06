import os
import openai
from dotenv import load_dotenv

load_dotenv()

def get_response(input):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    response = openai.Completion.create(
        engine="davinci",
        prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: {}".format(input),
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )

    return response["choices"][0]["text"]


if __name__ == "__main__":
    print(get_response("Hi there"))
