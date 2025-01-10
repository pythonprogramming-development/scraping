# from instagramy import Instagram 
# from instagramy import Instalysis 

# # Connecting the profile 
# user = Instagram("angular_development") 

# # printing the basic details like 
# # followers, following, bio 
# print(user.is_verified()) 
# print(user.popularity()) 
# print(user.get_biography()) 

# # return list of dicts 
# posts = user.get_posts_details() 

# print('\n\nLikes', 'Comments') 
# for post in posts: 
# 	likes = post["likes"] 
# 	comments = post["comment"] 
# 	print(likes,comments)


# Instagram user_id of ipl teams 
# teams = ["chennaiipl", "mumbaiindians", 
# 		"royalchallengersbangalore", "kkriders", 
# 		"delhicapitals", "sunrisershyd", 
# 		"kxipofficial"] 

# data = Instalysis(teams) 

# # return the dataframe 
# data_frame = data.analyis() 


# def get_likes_list(username):
#     api.login()
#     api.searchUsername(username)
#     result = api.LastJson
#     username_id = result['user']['pk'] # Get user ID
#     user_posts = api.getUserFeed(username_id) # Get user feed
#     result = api.LastJson
#     media_id = result['items'][0]['id'] # Get most recent post
#     api.getMediaLikers(media_id) # Get users who liked
#     users = api.LastJson['users']
#     for user in users: # Push users to list
#         users_list.append({'pk':user['pk'], 'username':user['username']})
from instagramy import InstagramUser
import requests
from urllib.parse import unquote

def validate_session_id(session_id):
    url = "https://www.instagram.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Cookie": f"sessionid={session_id}"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(f"Invalid session ID: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"Error validating session ID: {e}")
        return False

# Replace with your session ID
encoded_session_id = "12763350476%3A4uHfyCOqKJQYJK%3A3%3AAYfIshhxdznBm-A4tqLzp6l_dJChI7pmTu71f35TPIU"
session_id = unquote(encoded_session_id)

if validate_session_id(session_id):
    print("Session ID is valid.", session_id)
    
    # Connecting the profile
    try:
        user = InstagramUser("google", sessionid='12763350476:4uHfyCOqKJQYJK:3:AYfIshhxdznBm-A4tqLzp6l_dJChI7pmTu71f35TPIU')
    except Exception as e:
        print(f"Error connecting to Instagram profile: {e}")
        user = None

    if user:
        # Printing the basic details like followers, following, bio
        try:
            print("Verified:", user.is_verified())
            print("Popularity:", user.popularity())
            print("Biography:", user.get_biography())
        except Exception as e:
            print(f"Error fetching user details: {e}")

        # Return list of dicts
        try:
            posts = user.get_posts_details()
            print('\n\nLikes', 'Comments')
            for post in posts:
                likes = post.get("likes", "N/A")
                comments = post.get("comment", "N/A")
                print(likes, comments)
        except Exception as e:
            print(f"Error fetching posts details: {e}")
else:
    print("Session ID is invalid.")