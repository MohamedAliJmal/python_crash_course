def make_album(name,album_title,nb_songs=None):
    if nb_songs==None:
        return {"name":name,"album":album_title}
    else:
        return {"name":name,"album":album_title,"nb_songs":nb_songs}

active_flag=True
while active_flag:
    print("(enter 'q' at any time to quit)")
    name=input("name of the artist\n")
    if name=="q":
        active_flag=False
    else:
        album=input("album\'s name\n")
        if album=="q":
            active_flag=False
        else:
            nb_songs=input("number of songs\n")
            if nb_songs=="q":
                active_flag=False
            else:
                print(make_album(name.title(),album.title(),nb_songs.title()))
