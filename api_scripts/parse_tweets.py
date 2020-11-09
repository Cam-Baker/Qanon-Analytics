import json
import sys
import re

def print_tweet(json_list):
	data_list = json.loads(json_list)
	tweet_id = data_list['id']
	tweet_created_at = data_list['created_at']
	tweet_text = data_list['text'].replace("\n"," ").replace('"',"'")
	tweet_text = re.sub(' +',' ',tweet_text)
	tweet_hashtags = []
	tweet_urls = []
	for i in data_list['entities']['hashtags']:
		tweet_hashtags.append(i['text'])
	for i in data_list['entities']['urls']:
		#print(i['expanded_url'])
		tweet_urls.append(i['expanded_url'])
	user_id = data_list['user']['id_str']
	user_sn = data_list['user']['screen_name']
	user_location = data_list['user']['location']
	user_followers = data_list['user']['followers_count']
	user_friends = data_list['user']['friends_count']
	user_created = data_list['user']['created_at']
	user_verified = data_list['user']['verified']
	tweet_geo = data_list['geo']
	tweet_coord = data_list['coordinates']
	tweet_lang = data_list['lang']
	print('%s,%s,"%s","%s","%s",%s,%s,"%s",%s,%s,%s,%s,%s,%s,%s'%(str(tweet_id),str(tweet_created_at),str(tweet_text),','.join(tweet_hashtags),','.join(tweet_urls),str(user_id),str(user_sn),str(user_location),str(user_followers),str(user_friends),str(user_created),str(user_verified),str(tweet_geo),str(tweet_coord),tweet_lang))

with open(sys.argv[1]) as json_file:
	print("tweet_id,tweet_created_at,tweet_text,tweet_hashtags,tweet_urls,user_id,user_name,user_location,num_followers,num_following,user_creation_date,user_verified,tweet_location,tweet_coordinates,language")
	for line in json_file.readlines():
		if "errors" not in line and len(line.strip()) > 0:
			#print(line)
			print_tweet(line.strip())
