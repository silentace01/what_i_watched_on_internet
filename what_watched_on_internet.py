#what i watched on internet series and videos
#C:\Users\silentace\Documents\silentace\Python
from os import makedirs


try:
    import os
    main_dir = "C:\\Users\\silentace\\Documents\\silentace\\Python\\data"
    os.mkdir(main_dir) 
    main_dir = "C:\\Users\\silentace\\Documents\\silentace\\Python\\data\\music"
    os.mkdir(main_dir)
    main_dir = "C:\\Users\\silentace\\Documents\\silentace\\Python\\data\\web"
    os.mkdir(main_dir)
    main_dir = "C:\\Users\\silentace\\Documents\\silentace\\Python\\data\\youtube"
    os.makedirs(main_dir)
except Exception as e:
    pass
print("What silentace watched on the INTERNET")
fav_music = "C:\\Users\\silentace\\Documents\\silentace\\Python\\data\\music\\fav_music.log"
wish_music = "C:\\Users\\silentace\\Documents\\silentace\\Python\\data\\music\\wish_music.log"
listend_music ="C:\\Users\\silentace\\Documents\\silentace\\Python\\data\\music\\listend_music.log"
fav_web = "C:\\Users\\silentace\\Documents\\silentace\\Python\\data\\web\\fav_web.log"
wish_web = "C:\\Users\\silentace\\Documents\\silentace\\Python\\data\\web\\wish_web.log"
watched_web ="C:\\Users\\silentace\\Documents\\silentace\\Python\\data\\web\\warched_web.log"
fav_youtube = "C:\\Users\\silentace\\Documents\\silentace\\Python\\data\\youtube\\fav_youtube.log"
wish_youtube = "C:\\Users\\silentace\\Documents\\silentace\\Python\\data\\youtube\\wish_youtube.log"
watched_youtube = "C:\\Users\\silentace\\Documents\\silentace\\Python\\data\\youtube\\watched_youtube.log"
with open (fav_music,'a') as f:
    pass
with open (wish_music,'a') as f:
    pass
with open (listend_music,'a') as f:
    pass
with open (fav_web,'a') as f:
    pass
with open (wish_web,'a') as f:
    pass
with open (watched_web,'a') as f:
    pass
with open (fav_youtube,'a') as f:
    pass
with open (wish_youtube,'a') as f:
    pass
with open (watched_youtube,'a') as f:
    pass
#loop for main function
while True:
    #start loop for geting log or retrive about and exit
    while (True):
        #input for retrive or log
        log_or_retrive = input("1 For Retrive\n2 For Log\n3 For About\n4 For Exit\n")
        #checking it log or retrive 
        if(log_or_retrive=="1") or (log_or_retrive=="2") or(log_or_retrive=="3") or (log_or_retrive=="4"):
            log_or_retrive = int(log_or_retrive)
            break
        else:
            print("Something Went Wrong Try Again!!!!\n")

    #end loop for geting log or retrive about and exit
    # log or retrive only 
    if(log_or_retrive==1) or (log_or_retrive==2):
        #for retrive
        if(log_or_retrive==1):
            while(True):
                #choosing waht type of retrive
                write_type = input("1 For Music\n2 For Web Show\n3 For Youtube\n4 For Back\n")
                #type  casting and loop for only 4 option
                while(True):
                    if(write_type=="1") or (write_type=="2") or (write_type=="3") or (write_type=="4") or (write_type=="5"):
                        write_type = int(write_type)
                        break
                    else:
                        print("Something Went Wrong Try Again!!!!\n")
                        break

                #for music                 
                if(write_type==1):
                    while(True):
                        type_of_data = input("1 For Favourite Music\n2 For Your Wishlist\n3 For Listend\n4 For Back\n")
                        if type_of_data=="1" or type_of_data=="2" or type_of_data=="3" or type_of_data=="4" or type_of_data=="5":
                            type_of_data = int(type_of_data)
                            break
                        #fav Music
                    if type_of_data==1:
                     #open fav muisc and scan for index
                        with open(fav_music) as f:
                            f = f.readlines()
                            f_len = str(len(f)+1)
                        with open(fav_music) as f:
                            f = f.readlines()
                            f_len = str(len(f)+1)
                    #open fav music and write data on it
                        with open(fav_music,'a')as f:
                            #user input for music name
                            music_write = input("Write Favourite Music Name:\n")
                            #caste to capitalize
                            music_write = music_write.capitalize()
                            #write index and music name
                            f = f.write(f_len+": "+music_write+"\n")
                    # wish music write data on it
                    elif type_of_data==2:
                        #create file 
                        with open(wish_music) as f:
                            f = f.readlines()
                            f_len = str(len(f)+1)
                        with open(wish_music,'a')as f:
                            #user input for music name
                            music_write = input("Write Wishlist Music Name:\n")
                            #caste to capitalize
                            music_write = music_write.capitalize()
                            #write index and music name
                            f = f.write(f_len+": "+music_write+"\n")
                    elif type_of_data==3:
                        #create file 
                        with open(listend_music) as f:
                            f = f.readlines()
                            f_len = str(len(f)+1)
                        with open(listend_music,'a')as f:
                            #user input for music name
                            music_write = input("Write Listend Music Name:\n")
                            #caste to capitalize
                            music_write = music_write.capitalize()
                            #write index and music name
                            f = f.write(f_len+": "+music_write+"\n")
                    elif type_of_data==4:
                        break
                #web show
                elif(write_type==2):
                    while(True):
                        type_of_data = input("1 For Favourite Web Show\n2 For Your Wishlist\n3 For Watched\n4 For Back\n")
                        if type_of_data=="1" or type_of_data=="2" or type_of_data=="3" or type_of_data=="4" or type_of_data=="5":
                            type_of_data = int(type_of_data)
                            break
                    if type_of_data==1:
                     #open fav whow and scan for index
                        with open(fav_web) as f:
                            f = f.readlines()
                            f_len = str(len(f)+1)
                        with open(fav_web) as f:
                            f = f.readlines()
                            f_len = str(len(f)+1)
                    #open fav music and write data on it
                        with open(fav_web,'a')as f:
                            #user input for music name
                            web_write = input("Write Favourite Web Show Name:\n")
                            #caste to capitalize
                            web_write = web_write.capitalize()
                            #write index and music name
                            f = f.write(f_len+": "+web_write+"\n")
                    # wish music write data on it
                    elif type_of_data==2:
                        #create file 
                        with open(wish_web) as f:
                            f = f.readlines()
                            f_len = str(len(f)+1)
                        with open(wish_web,'a')as f:
                            #user input for music name
                            web_write = input("Write Wishlist Music Name:\n")
                            #caste to capitalize
                            web_write = web_write.capitalize()
                            #write index and music name
                            f = f.write(f_len+": "+web_write+"\n")
                    elif type_of_data==3:
                        #create file 
                        with open(watched_web) as f:
                            f = f.readlines()
                            f_len = str(len(f)+1)
                        with open(watched_web,'a')as f:
                            #user input for music name
                            web_write = input("Write Listend Music Name:\n")
                            #caste to capitalize
                            web_write = web_write.capitalize()
                            #write index and music name
                            f = f.write(f_len+": "+web_write+"\n")
                    elif type_of_data==4:
                        break
                elif(write_type==3):
                    while(True):
                        type_of_data = input("1 For Favourite Youtube Channel\n2 For Your Watchlist\n3 For Watched\n4 For Back\n")
                        if type_of_data=="1" or type_of_data=="2" or type_of_data=="3" or type_of_data=="4" or type_of_data=="5":
                            type_of_data = int(type_of_data)
                            break
                        #fav Youtube channel
                    if type_of_data==1:
                     #open fav youtube and scan for index
                        with open(fav_youtube) as f:
                            f = f.readlines()
                            f_len = str(len(f)+1)
                        with open(fav_youtube) as f:
                            f = f.readlines()
                            f_len = str(len(f)+1)
                    #open fav youtube and write data on it
                        with open(fav_youtube,'a')as f:
                            #user input for youtube name
                            youtube_write = input("Write Favourite Youtube Channel Name:\n")
                            #caste to capitalize
                            youtube_write = youtube_write.capitalize()
                            #write index and youtube name
                            f = f.write(f_len+": "+youtube_write+"\n")
                    # wish youtube write data on it
                    elif type_of_data==2:
                        #create file 
                        with open(wish_youtube) as f:
                            f = f.readlines()
                            f_len = str(len(f)+1)
                        with open(wish_youtube,'a')as f:
                            #user input for youtube name
                            youtube_write = input("Write Watchlist Videos Name:\n")
                            #caste to capitalize
                            youtube_write = youtube_write.capitalize()
                            #write index and youtube name
                            f = f.write(f_len+": "+youtube_write+"\n")
                    elif type_of_data==3:
                        #create file 
                        with open(watched_youtube) as f:
                            f = f.readlines()
                            f_len = str(len(f)+1)
                        with open(watched_youtube,'a')as f:
                            #user input for youtube name
                            youtube_write = input("Write Watched Youtube Videos Name:\n")
                            #caste to capitalize
                            youtube_write = youtube_write.capitalize()
                            #write index and youtube name
                            f = f.write(f_len+": "+music_write+"\n")
                    elif type_of_data==4:
                        break
                    else:
                        log_or_retrive=type_of_data
                elif(write_type==4):
                    break
        #for log
        elif(log_or_retrive==2):
            while(True):
                #choosing waht type of log
                log_type = input("1 For Music\n2 For Web Show\n3 For Youtube\n4 For Back\n")
                #type  casting and loop for only 4 option
                while(True):
                    if(log_type=="1") or (log_type=="2") or (log_type=="3") or (log_type=="4"):
                        log_type = int(log_type)
                        break
                    else:
                        print("Something Went Wrong Try Again!!!!\n")
                        break
                #for music
                if(log_type==1):
                    while True:
                        type_of_data = input("1 For Favourite Music\n2 For Your Wishlist\n3 For Listend\n4 For Back\n")
                        if type_of_data=="1" or type_of_data=="2" or type_of_data=="3" or type_of_data=="4" or type_of_data=="5":
                            type_of_data = int(type_of_data)
                            break
                    if type_of_data==1:
                        with open(fav_music,'r')as f:
                            f = f.readlines()
                            for item in f:
                                print("Your Favourite Music List")
                                print(item,end="")
                            print("")
                    elif type_of_data==2:
                        with open(wish_music,'r')as f:
                            f = f.readlines()
                            for item in f:
                                print("Your Music Whishlist ")
                                print(item,end="")
                            print("")
                    elif type_of_data==3:
                        with open(listend_music,'r')as f:
                            f = f.readlines()
                            for item in f:
                                print("Your Listend Music List")
                                print(item,end="")
                            print("")
                    elif type_of_data==4:
                        break                
                #for web show
                elif(log_type==2):
                    while True:
                        type_of_data = input("1 For Favourite Web Show\n2 For Your Wishlist\n3 For Watched\n4 For Back\n")
                        if type_of_data=="1" or type_of_data=="2" or type_of_data=="3" or type_of_data=="4" or type_of_data=="5":
                            type_of_data = int(type_of_data)
                            break
                    if type_of_data==1:
                        with open(fav_web,'r')as f:
                            f = f.readlines()
                            for item in f:
                                print("Your Favourite Web Show List")
                                print(item,end="")
                            print("")
                    elif type_of_data==2:
                        with open(wish_web,'r')as f:
                            f = f.readlines()
                            for item in f:
                                print("Your Web Show Whishlist")
                                print(item,end="")
                            print("")
                    elif type_of_data==3:
                        with open(watched_web,'r')as f:
                            f = f.readlines()
                            for item in f:
                                print("Your Watched Web Show List")
                                print(item,end="")
                            print("")
                    elif type_of_data==4:
                        break
                #Youtube
                elif(log_type==3):
                    while True:
                        type_of_data = input("1 For Favourite Youtube Channel\n2 For Your Watchlist\n3 For Watched\n4 For Back\n")
                        if type_of_data=="1" or type_of_data=="2" or type_of_data=="3" or type_of_data=="4" or type_of_data=="5":
                            type_of_data = int(type_of_data)
                            break
                    if type_of_data==1:
                        with open(fav_youtube,'r')as f:
                            f = f.readlines()
                            for item in f:
                                print("Your Favourite Youtube Channel List")
                                print(item,end="")
                            print("")
                    elif type_of_data==2:
                        with open(wish_youtube,'r')as f:
                            f = f.readlines()
                            for item in f:
                                print("Your Whishlist")
                                print(item,end="")
                            print("")
                    elif type_of_data==3:
                        with open(watched_youtube,'r')as f:
                            f = f.readlines()
                            for item in f:
                                print("Your Watched Videos List")
                                print(item,end="")
                            print("")
                    elif type_of_data==4:
                        break
                #for back
                elif(log_type==4):
                    break
        #for log
        else:
            pass
    #about program
    elif(log_or_retrive==3):
        print("\n\nAbout\nAuther: Abhishek\nCode: silentace\n\n")
    #for exit program
    if(log_or_retrive==4):
        print("Thanks For Using ")
        break
