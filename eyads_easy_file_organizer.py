# made by the one and only eyad
import os as file_control
from time import sleep as timeout

keywords = []
required_folders = []
required_files = []

print("EEFO: Eyad's Easy File Organizer")
timeout(1)

images = [".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp", ".heic", ".heif"]
video = [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm", ".mpeg", ".mpg"]
audio = [".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a", ".wma", ".alac"]
text = [".txt", ".rtf", ".md", ".markdown", ".log"]
special_text = [".csv", ".tsv", ".json", ".xml", ".yaml", ".yml"]
config_text = [".ini", ".cfg", ".conf", ".toml"]
markup = [".html", ".htm", ".css", ".js", ".jsx", ".tsx", ".php"]

directory = input("Enter the folder directory to organize -: ")
print("")

filetype_or_keyword = int(input("Do you want to organize by file extensions (type 1) or by keywords? (type 2) -: "))
if filetype_or_keyword == 2:
    keyword_amount = int(input("How many keywords to search for? -: "))
    i = 0
    while i != keyword_amount:
        keywords_enter = input(f"Enter keyword {i+1} -: ")
        keywords.append(keywords_enter)
        i += 1

    i = 0
    print("Organizer: Creating folders...")
    file_control.mkdir(f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER")
    while i != keyword_amount:
        file_control.mkdir(f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER\\{keywords[i]}")
        i += 1

    print("Organizer: Created folders!")
    i = 0
    print("Organizer: Sorting files...")
    files = file_control.listdir(directory)
    while i != len(files):
        for kw in keywords:
            if kw in files[i]:
                file_control.rename(
                    f"{directory}\\{files[i]}",
                    f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER\\{keywords[keywords.index(kw)]}\\{files[i]}"
                )
                break
        i += 1

    print("Organizer: Files Sorted!")
    print("Organizer: Finishing... ")
    i = 0
    buffer_files = file_control.listdir(f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER")
    while i != len(buffer_files):
        file_control.rename(
            f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER\\{buffer_files[i]}",
            f"{directory}\\{buffer_files[i]}"
        )
        i += 1

    file_control.rmdir(f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER")
    print("Organizer: Finished! Your files are now neat and clean!")

elif filetype_or_keyword == 1:
    i = 0
    sub_i = 0
    filetype = ""
    read_cache = []
    start_read_Cache = False
    print("Organizer: Searching for file formats...")
    files = file_control.listdir(directory)
    while i != len(files):
        while sub_i != len(files[i]):
            if files[i][sub_i] == ".":
                start_read_Cache = True
            if start_read_Cache:
                read_cache.append(files[i][sub_i])
            sub_i += 1

        filetype = ''.join(read_cache)

        if filetype in images:
            if "Images" not in required_folders:
                required_folders.append("Images")
                required_files.append("img" + files[i])
            else:
                required_files.append("img" + files[i])

        elif filetype in video:
            if "Video" not in required_folders:
                required_folders.append("Video")
                required_files.append("vid" + files[i])
            else:
                required_files.append("vid" + files[i])

        elif filetype in text:
            if "Text" not in required_folders:
                required_folders.append("Text")
                required_files.append("txt" + files[i])
            else:
                required_files.append("txt" + files[i])

        elif filetype in audio:
            if "Audio" not in required_folders:
                required_folders.append("Audio")
                required_files.append("aud" + files[i])
            else:
                required_files.append("aud" + files[i])

        elif filetype in special_text:
            if "Special Text" not in required_folders:
                required_folders.append("Special Text")
                required_files.append("sxt" + files[i])
            else:
                required_files.append("sxt" + files[i])

        elif filetype in config_text:
            if "Configuration Text" not in required_folders:
                required_folders.append("Configuration Text")
                required_files.append("cnf" + files[i])
            else:
                required_files.append("cnf" + files[i])

        elif filetype in markup:
            if "Markup" not in required_folders:
                required_folders.append("Markup")
                required_files.append("mrk" + files[i])
            else:
                required_files.append("mrk" + files[i])
        else:
            if "Micellaneous" not in required_folders:
                required_folders.append("Micellaneous")
                required_files.append("mcl" + files[i])
            else:
                required_files.append("mcl" + files[i])


        sub_i = 0
        i += 1
        filetype = ""
        start_read_Cache = False
        read_cache = []

    print(f"Organizer: Found {len(required_folders)} file format groups!")
    print("Organizer: Creating Folders.. ")
    file_control.mkdir(f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER")
    i = 0
    while i != len(required_folders):
        file_control.mkdir(f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER\\{required_folders[i]}")
        i += 1
    print("Organizer: Created folders!")
    print("Organizer: Sorting files...")
    i = 0
    while i != len(required_files):
        if ''.join(required_files[0:3]) == "img":
            file_control.rename(f"{directory}\\{required_files[i][3:]}", f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER\\Images\\{required_files[i][3:]}")
        elif ''.join(required_files[0:3]) == "vid":
            file_control.rename(f"{directory}\\{required_files[i][3:]}", f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER\\Videos\\{required_files[i][3:]}")
        elif ''.join(required_files[0:3]) == "txt":
            file_control.rename(f"{directory}\\{required_files[i][3:]}", f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER\\Text\\{required_files[i][3:]}")
        elif ''.join(required_files[0:3]) == "aud":
            file_control.rename(f"{directory}\\{required_files[i][3:]}", f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER\\Audio\\{required_files[i][3:]}")
        elif ''.join(required_files[0:3]) == "sxt":
            file_control.rename(f"{directory}\\{required_files[i][3:]}", f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER\\Special Text\\{required_files[i][3:]}")
        elif ''.join(required_files[0:3]) == "cnf":
            file_control.rename(f"{directory}\\{required_files[i][3:]}", f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER\\Configuration Text\\{required_files[i][3:]}")
        elif ''.join(required_files[0:3]) == "mrk":
            file_control.rename(f"{directory}\\{required_files[i][3:]}", f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER\\Markup\\{required_files[i][3:]}")
        elif ''.join(required_files[0:3]) == "mcl":
            file_control.rename(f"{directory}\\{required_files[i][3:]}", f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER\\Micellaneous\\{required_files[i][3:]}")

        i += 1
        # add more here

    print("Organizer: Sorted Files!")
    print("Organizer: Finishing...")
    buffer_files = file_control.listdir(f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER")
    i = 0
    while i != len(buffer_files):
        file_control.rename(f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER\\{buffer_files[i]}", f"{directory}\\{buffer_files[i]}")
        i += 1
    file_control.rmdir(f"C:\\Users\\{file_control.getlogin()}\\EEFO_BUFFER")
    print("Organizer: Finished! Your files are now neat and clean!")
else:
    print("Please type 1 to organize by file types or 2 by keywords.")

timeout(1.5)
print("Thank you for choosing EEFO! :D")
timeout(2)
input("Press enter to exit the program: ")
