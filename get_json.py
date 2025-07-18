from config import groq_client
from datetime import datetime
import json


def get_json(text):
    day = datetime.now().strftime("%A")
    time = datetime.now().strftime("%H:%M:%S")
    date = datetime.now().strftime("%Y-%m-%d")
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.0,
        messages=[
            {
                "role": "system",
                "content": """You are an intelligent and precise assistant designed to extract structured JSON data from text. Your task is as follows:

                1. **Language Handling**: You will receive input text written in **Hindi or Urdu**. First, accurately translate the text into **English** if you get something like this:  मैं याहया के साथ एक मीरिंग शेजूल करना चाहती हूँ, जुम्मा की सुबा 10 बच कर 25 मिनिट पर. then the 10 is HH 25 is MM, so it's 10:25.
                2. **Information Extraction**: After translation, identify if the message contains any **meeting-related information**.
                3. **Output Format**: If a meeting is identified, extract the relevant details and output only the JSON in the following format it should be in ENGLISH ONLY:
                {
                    "name": "Name of the person mentioned in the text",
                    "time": "Time in 24-hour format (e.g., '05:30' for AM and '17:30' for PM)",
                    "day": "Day of the week (e.g., Monday, Tuesday) based on references like 'tomorrow', 'after 2 days', etc. so tomorrow is current day + 1",
                    "date": "Exact date of the meeting in YYYY-MM-DD format, inferred from today's date which is {date} and the day is {day} and time is {time} so calculate the date accordingly if it is not mentioned in the text, so if today is Monday and the text says 'tomorrow' then the date should be Tuesday's date. which will be today's date + 1 day, or if it says Tuesday then it should be Tuesday's date, or if it says 'day after tomorrow' then it should be today's date + 2 days, or if it says 'after 3 days' then it should be today's date + 3 days, etc.",
                 }

                4. **Date and Time Reference**: You have access to the current **date: {date}, time = {time}, day = {day} **. Use this to calculate relative time expressions like "tomorrow", "day after tomorrow", or "after 3 days, eg if something like this is given:  मैं अली के साथ एक मीटिंग स्केजूल करना चाहता हूँ कल रात को दस बजे। this current day {day} + 1 so the next day and since it's mentioned that it's for night so it should be PM but converted into 24 HOURS format.", etc.

                5. **Error Handling**: If the text does **not** contain valid meeting information or does not contain time and at least one date/day reference even if it says something like:  کل صبح علی کے ساتھ میری میٹنگ بک کر دو , you shouldn't just assume time but return a JSON object with the following structure:
                {
                    "NO_MEETING_ERROR": "Meeting Info Not Found"
                }

                6. **Important**: Your response **must be only valid JSON** — no explanations, markdown formatting, or extra text.

                Be strict in your detection logic — only return meeting info if **time and at least one date/day reference** is available.""",
            },
            {
                "role": "user",
                "content": f"Conver the message into English if it's any other language and then turn it into json schema: {text}, the current date is {date}, the current time is {time}, and the current day is {day}. so if the date is not given and only day is given you have to calculate accordingly, don't add markdown ``` just return json format, no other text, no explanation, just json., output should be in ENGLISH ONLY, you have to get the date right you already have {date}, {day}, {time} so calculate the date accordingly if it is not mentioned in the text, and give ERROR message if the time has already passed like right now it's {time} and if the text contains anything that is before {time} on the current day which is {day} but if only time is mentioned along with the context of 'tomorrow' or day after tomorrow etc, then you should return the data normally otherwise you have to return the error message."
            }
        ])
    response_text = response.choices[0].message.content.strip()
    print("Response from Groq:", response_text)
    try:
        json_response = json.loads(response_text)
        print(f"Debug Message: Day: {day}, Time: {time}, Date: {date}")
        print(type(json_response))
        return json_response
    except json.JSONDecodeError:
        return {"NO_MEETING_ERROR": "Meeting Info Not Found"}
