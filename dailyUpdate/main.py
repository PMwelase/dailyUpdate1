from datetime import datetime as dt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import weather
import quotes
import loadshedding
import download_calendar
import json
from config.firebase_start import database

# GET TIME
now = dt.now()
today = now.weekday()
today = now.today()

day = dt.today().strftime("%A")



# GET TIME
now = dt.now()
today = now.weekday()

# print(today)
if __name__ == "__main__":
    
    if today < 5:
        user_data = database
        events = download_calendar.get_events_for_a_day()
        dbn_loadshedding = loadshedding.all_affected_hours("Durban")
        jhb_loadshedding = loadshedding.all_affected_hours("Johannesburg")
        cpt_loadshedding = loadshedding.all_affected_hours("Cape Town")
        
        
        from_email='pmwelase023@student.wethinkcode.co.za'
        password="ugfg tfht geck izxr"
        
        subject = f"{day}'s Daily Update"
        
        quote = quotes.get_quote()
    
                
        for k,v in user_data.items():
            name = v['name']
            campus = v['campus']
            to_email = v['email']

            morning_weather = weather.hourly_weather(8, campus)[0]
            afternoon_weather = weather.hourly_weather(12, campus)[0]
            evening_weather = weather.hourly_weather(16, campus)[0]
            rain = weather.hourly_weather(16, campus)[1]
            
            if campus == "Durban":
                campus_shedding = dbn_loadshedding
            elif campus == "Johannesburg":
                campus_shedding = jhb_loadshedding
            elif campus == "Cape Town":
                campus_shedding = cpt_loadshedding
            
            
            body = f"""
            <html>
                <body>
                    <p>Hi {name}, <br><br>
                        <b>Here's how your day is looking: </b><br>
                        <ul>
                            <li>{morning_weather}</li>
                            <li>{afternoon_weather}</li>
                            <li>{evening_weather}</li>
                        </ul>
                            {"<em>Don't forget to bring an umbrella today</em><br><br>" if rain else ""}
                        <b>School Events: </b><br>
                        <ul>
                            {''.join([f"<li>{event['summary']} from <b>{event['start']['dateTime'].split('T')[1][:5]}</b> to <b>{event['end']['dateTime'].split('T')[1][:5]}</b></li>" for event in events if any(attendee['email'] == to_email for attendee in event.get('attendees', []))]) if any(any(attendee['email'] == to_email for attendee in event.get('attendees', [])) for event in events) else "You're not an attendee on any school events today."}
                        </ul>
                        <b>Loadshedding: </b><br>
                        <ul>
                            {f"<l>There'll likely be loadsheding between {campus_shedding[0]}<b></b></l>" if len(campus_shedding) > 0 else "It looks like there'll be no loadshedding. But that may change."}
                        </ul>
                        <em>{quote[0]}</em><br>
                        <b> - {quote[1]}</b><br><br>
                        Warm Regards,<br>Phumelela<br>
                        <p>Click <a href="https://wtc-update.onrender.com/unsubscribe"><em>here</em></a> to unsubscribe.</p>
                    </p>
                </body>
            </html>
            """
        
            message = MIMEMultipart()
            message["From"] = from_email
            message["To"] = to_email
            message["Subject"] = subject
            
            message.attach(MIMEText(body, "html"))
            
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=from_email, password=password)
                connection.sendmail(
                    from_addr=from_email,
                    to_addrs=to_email,
                    msg=message.as_string()
            )

            