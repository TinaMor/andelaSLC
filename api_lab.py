from __future__ import print_function
from googleapiclient.discovery import build
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()
GPLUS = build('plus', 'v1', credentials = credentials)

POSTS = '''
    User: %s
    Date: %s
    Post: %s
    URL: %s
'''

items = GPLUS.activities().search(query='andela').execute().get('items', [])

for data in items:
	post = ' '.join(data['title'].strip().split())
	if post:
		print(POSTS % (data['actor']['displayName'], data['published'], post, data['url']))