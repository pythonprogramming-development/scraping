from instapy import InstaPy

#Turn on VPN or use requests package to create (rotating) proxies

# PASS IN USERNAME, PASSWORD, and TWO HASHTAGS you would like to scrape from

def create_instagram_scraping_session(username, password, hashtag1, hashtag2):
    # 1. session ->
    # create a session variable from the InstaPy initialization
    session = InstaPy(username=username, password=password, headless_browser=False)
    # 2. session.login ->
    #Login into IG with username and password given above.
    session.login()
    # 3. session.set_relationship_bounds ->
    # (from InstaPy Docs:)
    # THIS IS USED TO CHECK THE NUMBER OF 
    # FOLLOWERS AND/OR FOLLOWING A USER HAS AND IF 
    # THESE NUMBERS EITHER EXCEED THE NUMBER SET OR 
    # DOES NOT PASS THE NUMBER SET OR IF THEIR RATIO 
    # DOES NOT REACH DESIRED POTENCY RATIO THEN NO 
    # FURTHER INTERACTION HAPPENS
        # Arguments 
            # potency_ratio: following is higher than follower count
            # delimit_by_numbers: is used to activate & deactivate the usage of max & min values
            # max_followers: maximum of follower count user can have
            # max_following: maximum following count user can have
            # min_followers: minimum follower count user can have
            # min_following: minimum following count user can have
            # min_posts: minimum amount of posts user can have
            # max_posts: maximum amount of posts user can have
    session.set_relationship_bounds(enabled=True,
                    potency_ratio=1.34,
                    delimit_by_numbers=True,
                    max_followers=20000,
                    max_following=4000,
                        min_followers=4000,
                        min_following=800,
                        min_posts=20,
                max_posts=1000)
    # 4. session.like_by_tags ->
    # Establish a liked_photos variable that will return the information liked pictures data
    # created by the session.like_by_tags method, this method will only execute if the post falls
    # within the set_relationship_bounds set above
        # Arguments:
        # amount: Amount of photos set to like for each hashtag passed
    liked_photos = session.like_by_tags([hashtag1, hashtag2], amount=2 )
    # 5. Return liked photos that the method above finds based on the arguments passed
    return "CONTENT: ", liked_photos

    # 6. Now that you have the returned data, you can see what trends are found in the media posted 
    # (such as trends found in captions, content type, etc.)

# create_instagram_scraping_session("Coocoolady","Coocoomane", "fashion", "beauty" )