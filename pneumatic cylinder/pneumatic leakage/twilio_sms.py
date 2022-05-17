from twilio.rest import Client
sid = '#######'
token = '########'
# input details from your twilio  account
def notify(message):
    try:
        client = Client(sid,token)
        client.messages.create(messaging_service_sid = '#####',
                               body = message,
                               to = ['##########'])
    except Exception as e:
        print(e)
        pass
if __name__ == '__main__':
    notify('')