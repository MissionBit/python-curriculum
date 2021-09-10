# Real Life Example of CONDITIONALS. No coding, just explain

# You want to make spotify a more enjoyable experience, so you give users the option to like and
# dislike songs you suggest

# `pass` below is a statement that Python ignores. It is needed inside these functions because they
# do not have any code in them otherwise. Empty functions are not allowed in Python, and so we put
# the `pass` statement inside the function to avoid the error.

# Spotify functionality
def play_song():
    # Play the next suggested song!
    pass


def skip_song():
    # Skip this song!
    pass


def add_to_playlist():
    # Add this current song to your playlist!
    pass


# Run your suggestions Spotify playlist:
play_song()

# Gather input to see if they like it or not
song_review = input("Like or Dislike the Song")

if (song_review == "Like"):
    # If they liked it, add it to their playlist!
    add_to_playlist()
elif (song_review == "Dislike"):
    # If they disliked it, skip the song
    skip_song()
