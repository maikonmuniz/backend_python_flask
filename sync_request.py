import requests as req
import datetime

url = 'http://localhost:5000/message'
data = {
	"message": "Olá tudo bem? Que saudades de vc!",
	"zipcode": "13207500"
}

def call_api(i):
    print(f'calling{i}')
    print(datetime.datetime.now())
    res = req.post(url, json=data)
    print(datetime.datetime.now())
    return res.json()

def main():
    print(datetime.datetime.now())
    print('calling multiple APIs')
    for i in range(5):
        res = call_api(i)
        print(f'api call finished...{i} -> {res}')
    print('finished calling multiple APIs')
    print(datetime.datetime.now())

if __name__ == '__main__':
    main()