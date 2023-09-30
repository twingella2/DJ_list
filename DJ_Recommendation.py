import os
import random
from tinytag import TinyTag

def select_songs(song_data, key, genre, num_songs=10):
    # The same as we implemented before ...

def write_playlist(songs, key, genre, path='/Users/twingella/DJ_list'):
    # Enhanced version that includes DJ techniques ...

def get_song_data(dir_path):
    # Motor of our app collecting data about all .mp3 files ...

def analyse_tracks(songs):
    # Analyses tracks for the potential of using beatmatching and drop mixing ...

# specify your desired key and genre
key = '6A'
genre = 'House'

# get data about all songs in the specified directory
dir_path = '/Users/twingella/Desktop/DJ'
song_data = get_song_data(dir_path)

# select songs based on the specified key and genre
selected_songs = select_songs(song_data, key=key, genre=genre, num_songs=10)

# analyse the selected songs for DJ techniques
analysed_songs = analyse_tracks(selected_songs)

# write the analysed songs to a file
file_path = write_playlist(analysed_songs, key=key, genre=genre)
