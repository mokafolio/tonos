import subprocess
import fileinput

#config
hostname = "tonos"
soundcloud_key = None

#install pip
# subprocess.call("sudo apt install python3-pip", shell=True)

#install mopidy
#https://docs.mopidy.com/en/latest/installation/debian/
# subprocess.call("wget -q -O - https://apt.mopidy.com/mopidy.gpg | sudo apt-key add -", shell=True)
# subprocess.call("sudo wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/buster.list", shell=True)
# subprocess.call("sudo apt update", shell=True)
# subprocess.call("sudo apt install mopidy", shell=True)

# #install extensions
# subprocess.call("sudo apt install mopidy-mpd", shell=True)
# subprocess.call("sudo apt install mopidy-soundcloud", shell=True)

#adjust mopidy config

#change hostname
if hostname:
    with open("/etc/hostname", "w") as f:
        f.write(hostname)

    with fileinput.input(files=("/etc/hosts"), inplace=True) as f:
        for line in f:
            if "127.0.1.1" in line:
                print("127.0.1.1       " + hostname)
            else:
                print(line)
