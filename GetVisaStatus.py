import mechanize
from bs4 import BeautifulSoup
import sys
import re

if len(sys.argv) == 3:
    if re.search(r'^IRL[0-9]{8}$', sys.argv[1]):
        irl = sys.argv[1]
    if re.search(r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', sys.argv[2]):
        email = sys.argv[2]

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'default':
        irl = "IRL46653452"
        email = "sc.santy.sayantan@gmail.com"

else:
    print("No inputs given")
    exit(0)

br = mechanize.Browser()
response = br.open("https://www.vfsvisaonline.com/IrelandOnlineTracking/pages/OnlineTracking.aspx")

br.form = br.forms()[0]
#print(br.form)

br["ctl00$ContentMain$txtgwfNumber"] = irl
br["ctl00$ContentMain$txtLastName"] = email

response = br.submit()
soup = BeautifulSoup(response.read(), "html5lib")

print(soup.find(id="ContentMain_lblTrackingMessage").text)
