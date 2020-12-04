# simple algorithm
# make a "classify" map of all the songs and their genres => O(# Songs)
# iterate through each user and their track list O(# Users * # User Songs)
# create a genre_map for each user with {genre: 0 to start}
# increment each genre by 1 every time a song is within that genre # O(1)
# get max value of genre_map with max(genre_map.values) # less than O(# User Songs)
# iterate thru dict again and if the genre_map[genre] == max_val, append the genre

# TC -> O(# Users * # Songs), # SC -> O(# Users + # Songs)

from collections import defaultdict
def favGenres(userSongs, songGenres):
    classify = {}

    for genre in songGenres:
        all_songs = songGenres[genre]

        for song in all_songs:
            classify[song] = genre

    master = {}
    for user in userSongs:
        master[user] = []
        # for this user want to have {genre: count}
        genre_map = defaultdict(int)
        user_tracks = userSongs[user]

        for song in user_tracks:
            classified = classify[song]
            genre_map[classified] += 1

        max_val = max(genre_map.values())

        for genre in genre_map:
            if genre_map[genre] == max_val:
                master[user].append(genre)
    print(master)
    return master



favGenres(userSongs = {
       "David": ["song1", "song2", "song3", "song4", "song8"],
       "Emma":  ["song5", "song6", "song7"]
    },

songGenres = {
       "Rock":    ["song1", "song3"],
       "Dubstep": ["song7"],
       "Techno":  ["song2", "song4"],
       "Pop":     ["song5", "song6"],
       "Jazz":    ["song8", "song9"]
    }
)
