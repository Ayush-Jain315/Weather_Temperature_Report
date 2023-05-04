import requests
import json
import win32com.client as wincom
speak=wincom.Dispatch("SAPI.SpVoice")
flag=False

while True:
    speak.speak('Enter the name of city')
    city=input('Enter the name of city : ')
    url=f'https://api.weatherapi.com/v1/current.json?key=51221d0d252f4fdbb15155744232803&q={city}--header%20%27Content-Type:%20appl'
    r=requests.get(url)
    st=(r.text)
    print(st)
    dic=json.loads(st)
    a=dic['current']['temp_c']
    l=dic['current']['last_updated']
    text=f'temperature of {city} is {a} degree celsius as updated on {l[11:]}'
    speak.speak(text)
    print(a)
    text2='if you want to exit type quit if you want to check again type recheck'
    speak.speak(text2)
    print(text2)
    while True:
        s=input('Type here : ')
        if s=='quit':
            flag=True
            break
        elif s=='recheck':
             break
        else:
            speak.speak('You Typed Wrong Input Enter again')
            print('Please Enter again')
            pass
    if flag:
        break