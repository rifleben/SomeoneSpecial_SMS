import openai


def generate_nicety():
    """Generate a message."""
    API_KEY = "YOUR OPEN AI APIT KEY"
    openai.api_key = API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generate a text message from the perspective of a friend who cares for someone very much, "
               "and they want to send them kinds words to make their day better. Start with 'Hey Friend'",
        temperature=0.5,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # clear the white space before the message
    return response['choices'][0]['text'].strip()
