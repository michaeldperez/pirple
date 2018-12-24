favorite_song = {
    "Title" : "AnyTime (Extended Mix)",
    "Album" : "SPRS031",
    "Artist" : "Don Diablo",
    "Genre" : "Future House",
    "ReleaseDate" : "2014-08-04",
    "Label" : "Spinnin' Records (SPRS)",
    "Country" : "Netherlands",
    "VideoLink" : "https://youtu.be/qzNQLKgaLi0",
    "DurationInSeconds" : 247,
    "DurationInMinutes" : 4.57
}

for key, value in favorite_song.items():
    print("{} : {}".format(key, value))

def keyguess(key, value):
    global favorite_song
    if key in favorite_song and value == favorite_song[key]:
        return True
    else:
        return False