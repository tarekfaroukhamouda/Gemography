import requests
import pandas
users={}
users_used=[]
r=requests.get("https://api.github.com/search/repositories?q=created:>2021-08-01&sort=stars&order=desc")
d=pandas.read_json(r.content)
for language in d['items']:
    if language['language'] in users:
        users[language['language']]+=1
        users[str(language['language'])+"_"+'users_used']+=","+str(language['owner']['login'])
    else: 
        users[language['language']]=1
        users[str(language['language'])+"_"+'users_used']=str(language['owner']['login'])

print(users)