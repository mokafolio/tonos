import subprocess
import fileinput
import sys

#config
hostname = "tonos" #if you don't want to change this, set it to None
soundcloud_key = None

#helper functions
def replace_line(_file, _start, _change):
    with fileinput.input(files=(_file), inplace=True) as f:
        for line in f:
            if _start in line:
                print(_start + _change)
            else:
                sys.stdout.write(line)

#install pip
subprocess.call("sudo apt install python3-pip", shell=True)

#install mopidy
#https://docs.mopidy.com/en/latest/installation/debian/
subprocess.call("wget -q -O - https://apt.mopidy.com/mopidy.gpg | sudo apt-key add -", shell=True)
subprocess.call("sudo wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/buster.list", shell=True)
subprocess.call("sudo apt update", shell=True)
subprocess.call("sudo apt install mopidy", shell=True)

#install extensions
subprocess.call("sudo apt install mopidy-mpd", shell=True)
subprocess.call("sudo apt install mopidy-soundcloud", shell=True)

#adjust mopidy config

#change hostname
if hostname:
    with open("/etc/hostname", "w") as f:
        f.write(hostname)

    replace_line("/etc/hosts", "127.0.1.1", "       " + hostname)
