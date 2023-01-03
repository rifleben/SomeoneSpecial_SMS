# SomeoneSpecial_SMS

This is a SMS generator that uses OpenAI's GPT-3 API to generate text messages from the perspective of a friend who cares for someone very much. It also has a user interface built with tkinter that allows users to input a phone number and send the generated message to that phone number via the Twilio API.

![](https://github.com/rifleben/SomeoneSpecial_SMS/blob/main/someone_special.gif)

## Requirements
- A OpenAI API key
- A Twilio account and API keys
- Python 3 and the following libraries:
- openai
- twilio
- tkinter


## Usage
- Replace YOUR OPENAI API KEY in generate_nicety() with your own OpenAI API key.
- Replace YOUR TWILIO ACCOUNT SID, YOUR TWILIO AUTH TOKEN, and YOUR TWILIO PHONE NUMBER in send_sms() with your own Twilio API keys and phone number.
- Run the Interface class to open the user interface.
- In the phone number field, input the phone number you want to send the message to (in the format "+11234567890").
- You can either write your own message in the "User Message" field or click the "Generate Message" button to generate a message with the OpenAI API.
- Click the "Send" button to send the message.


## Notes
- The temperature and max tokens parameters in openai.Completion.create() can be adjusted to change the randomness and length of the generated message.
- The user interface image can be changed by replacing "Someone Special.png" with a different image file.
