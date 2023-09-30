
import os
from dotenv import load_dotenv
import librosa
import numpy as np
from tkinter import *

def generate_playlist():
    moods = ['Happy', 'Sad', 'Excited', 'Relaxed']
    bpm_ranges = ['80-100', '100-120', '120-140', '140-160']
    
    song_list = ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5']
    artist_list = ['Artist 1', 'Artist 2', 'Artist 3', 'Artist 4', 'Artist 5']
    
    bpm = random.choice(bpm_ranges)
    
    print(f'Generated playlist for mood: {mood_var.get()} and BPM: {bpm}')
    
    for i in range(5):
        print(f'Song {i+1}: {song_list[i]} by {artist_list[i]}')
        
        if i < 4:
            print(f'Transition from Song {i+1} to Song {i+2}: ')
            print('    Play with the faders and crossfade from Song {} to Song {}'.format(i+1, i+2))
        print('\n')

load_dotenv('.env_sample')

TARGET_MUSIC_DIRECTORY = os.getenv('TARGET_MUSIC_DIRECTORY')

# Fetch list of mp3 files in the target directory
mp3_files = [file for file in os.listdir(TARGET_MUSIC_DIRECTORY) if file.endswith('.mp3')]
print('Mp3 Files in the directory:', mp3_files)

# Load the first mp3 file
y, sr = librosa.load(os.path.join(TARGET_MUSIC_DIRECTORY, mp3_files[0]))

# Calculate the tempo (BPM)
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

# Calculate the key and mode
chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
key = np.argmax(chroma.mean(axis=1))

if key < 6:
   mode = 'Major'
else:
   mode = 'Minor'

print(f'Tempo of the song {mp3_files[0]}: {tempo}')
print(f'The key of the song {mp3_files[0]} is {key} in {mode} mode')

root = Tk()
root.geometry('300x200')

mood_var = StringVar(root)
mood_var.set('Happy')  # default value

mood_options = OptionMenu(root, mood_var, 'Happy', 'Sad', 'Excited', 'Relaxed')
mood_options.pack()

bpm_var = StringVar(root)
bpm_var.set('80-100')  # default value

bpm_options = OptionMenu(root, bpm_var, '80-100', '100-120', '120-140', '140-160')
bpm_options.pack()

generate_button = Button(root, text='Generate Playlist', command=generate_playlist)
generate_button.pack()

root.mainloop()
