# SpotifyPodcastHack
A Python script, which removes podcasts from Windows installation of Spotify.

# Disclaimer
This script modifies your Spotify installation, and it is possible, that it will make it non-usable. You use it on your own risk.

# Usage
Downlad the script and configure. On Windows you need to replace your user name, so that script can reach proper path:

```python
# Configurable
# On Mac / Linux remember to change all "\\"s  to "/"s

user_name = "<your user name>"
path_to_spotify = "C:\\Users\\" + user_name + "\\AppData\\Roaming\\Spotify\\Apps\\"
temp_path = "C:\\Temp\\"
```

Then run the script.

Note: the script won't remove podcasts only from the home page, but also - most likely - from search results and other parts of the application. In the end, this is a hack, not a mod or plugin or update or anything like it.

# What it does?

In a nutshell, unzips a file from Spotify installation, then removes certain strings from a single file, zips everything again and puts back in the Spotify folder.

# Compatibility

Script is tested on Windows. It *should* work on Linux/Mac as well (with appropriate privileges), but was not tested. Give me a shout if you can confirm/deny it working on other systems.

# Undo

Script backs up contents of xpui.spa file to xpui.spa.old. If you want to restore previous behavior, simply overwrite the xpui.spa file with the backup and everything should be back to normal. Or obviously, you can simply reinstall Spotify.
