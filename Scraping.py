from instagramy import Instagram 


# Connecting the profile 
user = Instagram("geeks_for_geeks") 

# printing the basic details like 
# followers, following, bio 
print(user.is_verified()) 
print(user.popularity()) 
print(user.get_biography()) 

# return list of dicts 
posts = user.get_posts_details() 

print('\n\nLikes', 'Comments') 
for post in posts: 
	likes = post["likes"] 
	comments = post["comment"] 
	print(likes,comments)


from instagramy import Instalysis 

# Instagram user_id of ipl teams 
teams = ["chennaiipl", "mumbaiindians", 
		"royalchallengersbangalore", "kkriders", 
		"delhicapitals", "sunrisershyd", 
		"kxipofficial"] 

data = Instalysis(teams) 

# return the dataframe 
data_frame = data.analyis() 


def get_likes_list(username):
    api.login()
    api.searchUsername(username)
    result = api.LastJson
    username_id = result['user']['pk'] # Get user ID
    user_posts = api.getUserFeed(username_id) # Get user feed
    result = api.LastJson
    media_id = result['items'][0]['id'] # Get most recent post
    api.getMediaLikers(media_id) # Get users who liked
    users = api.LastJson['users']
    for user in users: # Push users to list
        users_list.append({'pk':user['pk'], 'username':user['username']})
