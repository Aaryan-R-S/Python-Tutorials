import re

s = """
Skip to content
Using Gmail with screen readers
Meet akjsk@jhadk.si
New meeting
Join a meeting
Hangouts
1 of 49
Welcome to Netflix StreamFest!
Inbox
Netflix <info@mailer.netflix.com> Unsubscribe
10:06 AM (1 hour ago)
to me
Netflix
Thanks for joining Netflix!
Hi r7o7x7artzclock7
We are so thrilled you're here! You're all ready enjoy unlimited entertainment, absolutely free until 11:59 PM, 6 December.
START WATCHING
Your Account Information:
Email
r7o7x7artzclock7@gmail.com
Service Provider
Netflix Entertainment Services India LLP
We're here to help if you need it. Visit the Help Centre for more info or contact us.
– Your friends at Netflix
VIEW ALL TV PROGRAMMES & FILMS>
Questions? Call 000-800-040-1843
Netflix Entertainment Services India LLP
Communication Settings | Terms of Use | Privacy | Help Centre
This message was emailed to [r7o7x7artzclock7@gmail.com] by Netflix because you signed up for Netflix StreamFest.
SRC: 16663_en-GB_IN
=-sg+@adsv.--
"""

regx = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.([a-zA-Z0-9-.]){2,253}')
checkEmail = regx.finditer(s)

j = 0
for i in checkEmail:
    print(f"Email No. {j+1} :", i)
    j+=1

printEmail = re.finditer(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.([a-zA-Z0-9-.]){2,253}', s)
for i in printEmail:
    start = i.start()
    end = i.end()
    print(f"{s[start:end]}")
