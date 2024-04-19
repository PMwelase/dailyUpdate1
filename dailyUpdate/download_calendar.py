from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from datetime import datetime as dt
import datetime

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
calendar_id = "c_965b5696a1903c71011a25a8eb71e97b3d847410f8ee919764cd46e585d1c528@group.calendar.google.com"

creds = Credentials.from_authorized_user_file("credentials.json", SCOPES)
date = dt.now().date()
# date = date+datetime.timedelta(days = 1)

def get_events_for_a_day():
    service = build("calendar", "v3", credentials=creds)
    date = dt.now().date()
    # date = date+datetime.timedelta(days = 3)

    events_result = (service.events().list(
        calendarId = "c_965b5696a1903c71011a25a8eb71e97b3d847410f8ee919764cd46e585d1c528@group.calendar.google.com",
        timeMin = date.isoformat()+ "T00:00:00Z",
        timeMax = date.isoformat()+ "T23:59:59Z",
        singleEvents = True,
        orderBy = "startTime",
        )
    .execute()
    )
    
    return events_result.get("items")


if __name__ == "__main__":
    events = get_events_for_a_day(date, calendar_id)
    for item in events:
        print(item['summary'])
        print(item['start']['dateTime'].split("T")[1][:5])
        print("to")
        print(item['end']['dateTime'].split("T")[1][:5])
        print("\n\n\n\n")
