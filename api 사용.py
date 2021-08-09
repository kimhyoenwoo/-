Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib.request
from urllib.parse import urlencode, quote_plus, unquote
import xml.etree.ElementTree as ET

decode_key = unquote('사용자키')
print(decode_key)

url = 'http://openapitraffic.daejeon.go.kr/api/rest/busRouteInfo/getStaionByRouteAll'

req = urllib.request
addrlist =[]
for i in range(1,5):
  queryParams = '?' + urlencode({quote_plus('ServiceKey') : decode_key
                              ,quote_plus('reqPage') :i})

  # print(queryParams)
  body = req.urlopen(url+queryParams)
  req.get_method = lambda:'GET'
  response_body = body.read()
  result = response_body.decode('utf-8')

  tree = ET.ElementTree(ET.fromstring(result))
  note = tree.getroot()

  for num in note.iter('BUS_STOP_ID'):
    text = num.text
    addrlist.append(text)
    # bus_stop = '\t'.join(addrlist)
    # print(bus_stop[99])
    print('\t'.join(addrlist))

    #32까지 돌아가고 멈춤 