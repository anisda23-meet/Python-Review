def create_youtube_video(title,description):
	youtubevideo = {"Title" : title , "Description" : description , "Likes" : 0 , "Dislikes" : 0 , "comments" : {}}
	return youtubevideo
def like(youtubevideo):
	if "Likes" in youtubevideo:
		youtubevideo["Likes"] = youtubevideo["Likes"] + 1
	return youtubevideo
def dislike(youtubevideo):
	if "Dislikes" in youtubevideo:
		youtubevideo["Dislikes"] = youtubevideo["Dislikes"] + 1
	return youtubevideo
def add_comment(youtubevideo,username,comment_text):
	youtubevideo["comments"][username] = comment_text
	return youtubevideo

c = create_youtube_video("aa","ggg")
c = like(c)
c = dislike(c)
c = add_comment(c,"anis","fank you nameer")
print(c)