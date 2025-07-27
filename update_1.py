# made by the one and only eyad
import os as file_control
from time import sleep as timeout

keywords = []

print("EEFO: Eyad's Easy File Organizer")
timeout(1)

directory = input("Enter the folder directory to organize -: ")
print("")

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

timeout(1.5)
print("Thank you for choosing EEFO! :D")
input("")
