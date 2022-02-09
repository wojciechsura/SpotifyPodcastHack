from pathlib import Path
import os, shutil, zipfile

# Configurable
# On Mac / Linux remember to change all "\\"s  to "/"s

user_name = "<your user name>"
path_to_spotify = "C:\\Users\\" + user_name + "\\AppData\\Roaming\\Spotify\\Apps\\"
temp_path = "C:\\Temp\\"

# Defines (don't change)

path_to_xpui = path_to_spotify + "xpui.spa"
path_to_xpui_backup = path_to_spotify + "xpui.spa.old"
temp_xpui_path = temp_path + "xpui\\"
path_to_xpui_js = temp_xpui_path + "xpui.js"
path_to_new_xpui = temp_path + "xpui.zip"

# Functions

def clear_folder(path):
    
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            return False

    return True

# Executing hack

print("Backing up xpui file...\r\n")
shutil.copy(path_to_xpui, path_to_xpui_backup)

print("Opening xpui file...\r\n");
xpui = zipfile.ZipFile(path_to_xpui, 'r')

print("Removing contents of existing temporary folder...")
if Path(temp_xpui_path).exists():
    if (not clear_folder(temp_xpui_path)):
        print("Failed to clear temporary path. You may need to do it manually before executing the script again.")
        exit()

print("Creating temporary folder...\r\n")
Path(temp_xpui_path).mkdir(parents=True, exist_ok=True)

print("Unzipping contents of xpui file...")
xpui.extractall(temp_xpui_path)
xpui.close()

print("Opening xpui.js...")
xpuijs = open(path_to_xpui_js, "rb")
xpuijs_contents = xpuijs.read()
xpuijs.close()

print("Finding and removing shows and episodes...")
xpuijs_contents = xpuijs_contents.replace(b"types:\"album,playlist,artist,show,station,episode\"", b"types:\"album,playlist,artist,station\"")
xpuijs_contents = xpuijs_contents.replace(b"types:\"artist,album,show,playlist,station,collection,track\"", b"types:\"artist,album,playlist,station,collection,track\"")
xpuijs_contents = xpuijs_contents.replace(b"additional_types:\"track,episode\"", b"additional_types:\"track\"")
xpuijs_contents = xpuijs_contents.replace(b"types:\"album,playlist,artist,show\"", b"types:\"album,playlist,artist\"")

print("Saving modified xpui.js...")
xpuijs = open(path_to_xpui_js, "wb")
xpuijs.write(xpuijs_contents)
xpuijs.close()

print("Zipping modified contents of xpui.spa again...")
shutil.make_archive(path_to_new_xpui, "zip", temp_xpui_path, )

print("Replacing xpui.spa with modified file")
os.remove(path_to_xpui)
shutil.move(path_to_new_xpui + ".zip", path_to_xpui)

print("Cleaning up...")
clear_folder(temp_xpui_path)
os.removedirs(temp_xpui_path)