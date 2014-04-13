import requests
import pprint as p
import contextio as c
import string
from PIL import Image, ImageEnhance, ImageFilter
import random

CONSUMER_KEY = 'xrmwwe7e'
CONSUMER_SECRET = 'iLkQIPm9M9dedwLH'

context_io = c.ContextIO(
    consumer_key=CONSUMER_KEY, 
    consumer_secret=CONSUMER_SECRET
)

params = {
    'id': '53499105064ba30834b4b0c0'
}
account = c.Account(context_io, params)

params2 = {
    'include_body': '1',
    'body_type': 'text/plain',
    'sort_order': 'desc',
    'limit': '15'
}

threads = account.get_threads(limit=1)
threads[0].get(include_body=1)
messages = threads[0].messages
#p.pprint(messages)
x = 0
mood=[]
length=[]
keywords=[]

for eachmessage in messages:
    message = eachmessage.get_body(type='text/plain')
    listInMessage =message[0]
    content = listInMessage['content']
    #p.pprint(content)
    content2 = content.encode('utf-8')
    #p.ppritn(parsedContent)
    parsedContent = content2.translate(string.maketrans("\n\t\r", "   "))
    index = parsedContent.find("Sat")
    if index != -1:
        parsedContent = parsedContent[:index-4]
    #p.pprint(parsedContent)
    length.append(len(parsedContent))
    params3 = {'apikey': 'd8894db2dd60aed653e7bd91ea854ce91f46ec85', 'text': parsedContent, 'outputMode': 'json'}
    analyzedString = requests.get('http://access.alchemyapi.com/calls/text/TextGetTextSentiment',params=params3).json()
    analyzedkeywords = requests.get('http://access.alchemyapi.com/calls/text/TextGetRankedKeywords',params=params3).json()
    keywordslist = analyzedkeywords['keywords']
    keywords.append(len(keywordslist))
    if analyzedString['docSentiment']['type'] == 'neutral':
        mood.append(0)     
    else:
       # p.pprint(analyzedString['docSentiment']['score'])
        mood.append(float(analyzedString['docSentiment']['score']))
    x = x +1
 #   p.pprint(keywords)    
 #   p.pprint(mood)
 #   p.pprint(length)

keyiter =0
#p.pprint(keywords)    
#p.pprint(mood)
#p.pprint(length)

for eachkey in keywords:
    keywords[keyiter]=float(eachkey)/float((length[keyiter]))
    keyiter = keyiter+1
#p.pprint(keywords)    
#p.pprint(mood)
#p.pprint(length)
   #i p.pprint(analyzedString)
#emailList = requests.get('https://api.context.io/2.0/accounts/53499105064ba30834b4b0c0/messages?body_type=text%2Fplain&include_body=1&limit=15&sort_order=desc')
#iemailList = requests.get('https://api.context.io/2.0/accounts/53499105064ba30834b4b0c0/messages')
#print(emailList)

img = raw_input("Enter name of image file: ")
imagefile = Image.open(img)
imagefile.show()

for i in mood:
  i = i + 1
  
average = float(sum(mood) / len(mood))

if average > 1.3:
  r = float(average*127.5)
  g = float((255-r)/2)
  b = float((255-r)/2)
  
elif average >= 0.6:
  g = float(average*127.5)
  r = float((255-g)/2)
  b = float((255-g)/2)
  
else:
  b = float(average*127.5)
  r = float((255-b)/2)
  g = float((255-b)/2)

color = '#%02x%02x%02x' % (r, g, b)
overlay = Image.new(imagefile.mode, imagefile.size, color)

imagefile = Image.blend(imagefile, overlay, 0.5)

averageLength = float(sum(length) / len(length))

if averageLength <= 50:
  radius = 1
  
elif averageLength <= 125:
  radius = random.randint(2,3)
  
elif averageLength <= 225:
  radius = random.randint(4,5)
  
elif averageLength <= 400:
  radius = random.randint(6,7)
  
elif averageLength <= 550:
  radius = 8
  
elif averageLength <= 750:
  radius = 9
  
else:
  radius = 10

imagefile = imagefile.filter(ImageFilter.GaussianBlur(radius))

enhancer = ImageEnhance.Brightness(imagefile)

averageFactor = float(sum(keywords) / len(keywords))

factor = float(averageFactor*10+1)



finalimg = enhancer.enhance(factor)

finalimg.show()


