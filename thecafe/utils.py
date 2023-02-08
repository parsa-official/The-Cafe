from kavenegar import *

def reservation_submit_sms(phone_number, name, time, date, people):
    try:
        api = KavenegarAPI('place your kavenegar api key here')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f"{name} عزیز \nبرای ساعت {time} در تاریخ {date} برای {people} نفر میز رزرو شد \nبا تشکر از شما \nThe Cafe"
            

        
        }   
        response = api.sms_send(params)
        print (str(response))
    except APIException as e: 
        print (str(e))
    except HTTPException as e: 
        print (str(e))
