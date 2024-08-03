import requests 
import pandas as pd
import os
token="EAADhUm2JZBoABALViwGM5RFyXK49DnEHfL2PuahvexhWgMqaZAsw99oUSp5hOMwQIg3bXSqG6N3ZBUPGYpxOrpE2GT6mAvidPZB1SZC15P6x7B7vK6gVVi7Ak4ixb2tnedpsOrRiU7cqeQGvUj6Gy9FJZAOVEYRG1AsULZAGO0O5QfZABAyXT4Px"
try:
    token = os.environ['FB_TOKEN']
except:
    print ("Set FB_TOKEN variable")
    #sys.exit(-1)
    exit

fb_pageid="100094163389097"
fb_postid="110868105395302"
commentlst = []
datelst = []

url = "https://graph.facebook.com/v2.12/"+ fb_pageid +"_"+ fb_postid +"/comments?limit=100&access_token="+token

while(True):
    posts = requests.get(url)
    posts_json = posts.json()
    for x1 in posts_json['data']:
        commentlst.append(x1.get('message').encode('utf-8').strip())
        datelst.append(x1.get('created_time'))
    next_page = ""
    try:
        next_page = posts_json['paging']['next']
        url = next_page
    except:
        break
    if not next_page: break

print ("\nGenerating JSON File")

df = pd.DataFrame({'comment': commentlst, 'dates': datelst})
df['dates'] = pd.to_datetime(df['dates'])
df['day_of_week'] = df['dates'].dt.day_name
df['year'] = df['dates'].dt.year
df['month'] = df['dates'].dt.month
df['count'] = 1 

df.to_json('comment_data.json')