import requests
from requests.structures import CaseInsensitiveDict

def wasapp():
    url = "https://graph.facebook.com/v14.0/109968801877696/messages"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer EAAGegupCQI0BAITneQyBdtuT7Gp4Hgoz1WidlwT9ijtAuUBiOS9fZB3eRu6NqZBkVV9mTbzUNUbqKPnenGHmnfbPEQZCovQdPs8VZAEzmwMBFZCP4ZAFZAUDuH5Q1xnCWWKjLy26ziiiOeUlhpZBRXBlj6KRQcTvWhDZACjPxYVhUyWclrauilNx5nZBst4tSgpjWvYtZCjmLrYnwZDZD"
    headers["Content-Type"] = "application/json"

    data = '{ "messaging_product": "whatsapp", "to": "584120434039", "type": "template", "template": { "name": "hello_world", "language": { "code": "en_US" } } }'


    resp = requests.post(url, headers=headers, data=data)

    print(resp.status_code)


wasapp()