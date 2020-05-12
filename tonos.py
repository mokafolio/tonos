import subprocess
import fileinput
import sys

#config
hostname = "tonos" #if you don't want to change this, set it to None
soundcloud_key = "3-35204-28629142-4hrn1FMFg3HZBWii"

#helper functions
def replace_line(_path, _start, _change):
    with fileinput.input(files=(_path), inplace=True) as f:
        for line in f:
            if _start in line:
                print(_start + _change)
            else:
                sys.stdout.write(line)

def append_to_file(_path, _str):
    with open(_path, "a") as f:
        f.write(_str)

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
subprocess.call("sudo apt install snapserver", shell=True)
subprocess.call("sudo apt install mopidy-soundcloud", shell=True)
subprocess.call("sudo apt install mopidy-spotify", shell=True)
subprocess.call("sudo apt install mopidy-youtube", shell=True)

#adjust mopidy config to allow access from local ips for both http and mpd
append_to_file("/etc/mopidy/mopidy.conf", "\n[mpd]\nhostname = ::\n\n[http]\nhostname = ::\n")

#enable soundcloud
if soundcloud_key != None:
    append_to_file("/etc/mopidy/mopidy.conf", "\n[soundcloud]\auth_token = " + soundcloud_key + "\n")

#make mopidy run as a service
subprocess.call("sudo dpkg-reconfigure mopidy", shell=True)

#change hostname
if hostname:
    with open("/etc/hostname", "w") as f:
        f.write(hostname)

    replace_line("/etc/hosts", "127.0.1.1", "       " + hostname)

#install iris frontend
subprocess.call("sudo python3 -m pip install Mopidy-Iris", shell=True)
