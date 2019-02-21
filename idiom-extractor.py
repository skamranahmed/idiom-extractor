import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

source = requests.get('https://www.englishclub.com/ref/idiom-of-the-day.php').text

soup = BeautifulSoup(source,'lxml')

# content = soup.find('main', id="ec-main")

# print(content.prettify())


headline = soup.find('h1').text

idiom = soup.find('h2').text

meaning = soup.find_all('p')[1].text

example = soup.find('div',class_='example')
for_example = example.h3.text
sentence1 = example.find_all('li')[0].text
sentence2 = example.find_all('li')[1].text


# print(example)
# print(for_example)

# title = soup.title.text
def message():
        print(headline + '\n') 
        print(idiom+'\n')
        print("Meaning :")
        print(meaning + '\n')
        print(for_example)
        sentences = example.find_all('li')
        for sentence in sentences:
            print("-> "+sentence.text)
            print()



# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'Your_Account_SID'
auth_token = 'Your_auth_token'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body=headline+"\n\n"+idiom+"\n\nMeaning\n\n"+meaning+"\n\n"+for_example+"\n\n"+sentence1+"\n\n"+sentence2,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+91XXXXXXXXXX'
                          )

print(message.sid)
