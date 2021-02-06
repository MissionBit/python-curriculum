#Example of CONDITIONALS


#You want to make spotify a more enjoyable experience, so yu give users the option to like and dislike songs you suggest

#Spotify functionality
def play_song():
    #Play the next suggested song!

def skip_song():
    #Skip this song!

def add_to_playlist():
    #Add this current song to your playlist!


#Run your suggestions Spotify playlist:

play_song()

#Gather input to see if they like it or not
song_review = input("Like or Dislike the Song")

if(song_review == "Like"):
    #If they liked it, add it to their playlist!
    add_to_playlist()
elif (song_review == "Dislike"):
    #If they disliked it, skip the song
    skip_song()
