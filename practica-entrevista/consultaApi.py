import requests

def main():
    datos = 'https://jsonplaceholder.typicode.com/posts'
    data = llamadaApi(datos)

def llamadaApi(datos):
    respuesta = requests.get(datos)

    respuesta2=requests.post(datos,{
    'title': 'foo',
    'body': 'bar',
    'userId': 1,})

    respuesta = respuesta.json()
    respuesta2 = respuesta2.json()

    print(respuesta)
    print(respuesta2)


if __name__=='__main__':
    main()