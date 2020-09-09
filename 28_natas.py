import requests
from urllib.parse import unquote

username = "natas28"
password = "JWwR438wkgTsNKBbcJoowyysdM82YjeF"
search = "a"

for x in range(26):
    content = {'query': "aaaaaaaaa" + search}
    r = requests.post('http://natas28.natas.labs.overthewire.org/index.php', 
        auth = (username, password),
        data = content,
        allow_redirects=False
        )
    
    decoded = unquote(r.headers['Location'])
    print("[+] last: {} \toutput: {}".format(search, decoded[60:]))
    prev = ord(search)
    search = chr(prev + 1)



# r = requests.post('http://natas28.natas.labs.overthewire.org/index.php', 
#         auth = (username, password),
#         data = content,
#         allow_redirects=False
#         )
# 
# print(r.status_code)
# print(r.headers['Location'][18:])
