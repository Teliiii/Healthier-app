import datetime
import os.path
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI


import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]



client = OpenAI (
    api_key=os.getenv("OPENAI_API_KEY")
)

def main():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
      creds = flow.run_local_server(port=8000)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)
      # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # Start time: Today
    week_later = (datetime.datetime.utcnow() + datetime.timedelta(days=7)).isoformat() + "Z"  # End time: 7 days from now

    events_result = service.events().list(
        calendarId="primary",
        timeMin=now,
        timeMax=week_later,  # Fetch events for the next 7 days
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    events = events_result.get("items", [])

    if not events:
        print("No events found for the upcoming week.")
        return

    list = []
    for event in events:
        event_name = event.get("summary", "No Title")
        start_time = event["start"].get("dateTime", event["start"].get("date"))
        end_time = event["end"].get("dateTime", event["end"].get("date"))
        list.append(f"start: {event_name}, {start_time} end:  {end_time}")
        print(f"start: {event_name}, {start_time} end:  {end_time}")

    events_string = json.dumps(list)

    example_event = {
      "summary": "name",  
      "description" : "description goes here", 
      "colorId" : 6, #color goes here 
      "start" : {
        "dateTime" : "2025-03-24T17:00:00", # date
        "timeZone" : "America/Los_Angeles"
      },
      "end" : {
        "dateTime" : "2025-03-24T19:00:00", 
        "timeZone" : "America/Los_Angeles"
      },
      "recurrence": [
        "RRULE:FREQ=DAILY;COUNT=7" #depends on the frequency that the user wants
      ]

    }

    prompt = "create a json file. based on workout frequency, type of workout (hypertrophy, aerobic, strength), and avoid times of day that are busy"

    chat_completion = client.chat.completions.create (
        model = "gpt-4o",
        response_format = {"type":"json_object"},
        messages = (
            {"role":"system","content": "provide output in valid json. The data should seem like this: " + json.dumps(example_event) +  "and omit the following times: " + events_string + ". If they are there, don't postpone by an entire day but rather find another time during the day. it does not have to be the same day every day repeating. Don't make the time before 7:00 or after 22:00"},
            {"role": "user", "content": prompt}
        )
    )

    data = chat_completion.choices[0].message.content

    event = json.loads(data)

    print(event)

    event = service.events().insert(calendarId='primary', body=event).execute()

    print(f"Event created {event.get('htmlLink')}")
    # Prints the start and name of the next 10 events

  except HttpError as error:
    print(f"An error occurred: {error}")

if __name__ == "__main__":
  main()