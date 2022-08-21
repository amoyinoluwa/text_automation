from twilio.rest import Client
import os, time, schedule, random
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_NUMBER']
target_number = os.environ['TARGET_NUMBER']
MOTIVATIONAL_QUOTES = ['Write it on your heart that every day is the best day in the year.',
                        'Smile in the mirror. Do that every morning and you’ll start to see a big difference in your life.',
                        'Morning comes whether you set the alarm or not.'
                        ]
def message():
    client = Client(account_sid, auth_token)
    client.messages.create(to=target_number,
                                    from_=twilio_number,
                                    body="Good day"+MOTIVATIONAL_QUOTES[random.randint(0, len(MOTIVATIONAL_QUOTES)-1)]
    )

schedule.every(10).minutes.do(message)
while True:
    schedule.run_pending()
    time.sleep(1)