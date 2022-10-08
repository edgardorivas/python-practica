from urllib import request


import requests
from requests.structures import CaseInsensitiveDict

def mensaje():
    url = "https://graph.facebook.com/v14.0/109968801877696/messages"
    datos = CaseInsensitiveDict()
    datos["Authorization"] ='Bearer EAAGegupCQI0BAIXD4ZCI4MQ243OWOASlQdgKWhYFO6NZA6SKxwkXM4u98xinOxaaAyQNiUZAR7mOkz1JOH0TQuJPsDOglyfK6VXZBVVhovWqkBIAcYdrJ3Enckox5O2JhsT3hngPMZCWVF7Od67MzNqesyFmo9kQDOFrTewLZCs2ULmLsxKl1catZAZAFnRSOUZCWogkd8t41rwZDZD' 
    datos["Content-Type"] ='application/json'

    cuerpo= """
        { "messaging_product": "whatsapp", 
        "to": "584120434039",
        "type": "text",
        "text": { "body": "hello_world" } 
        } 
    """
    respuesta = requests.post(url,headers=datos , data=cuerpo)
    print(respuesta.status_code)

mensaje()