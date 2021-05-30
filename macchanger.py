#! /usr/bin/python

import subprocess
import optparse

def macchanger ( interface , new_mac ):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


parse = optparse.OptionParser()
parse.add_option("-i", "--interface", dest="interface", help="set interface using this flag")
parse.add_option("-m", "--mac", dest="mac_address", help="set the new mac address")
(options, arguments) = parse.parse_args()

interface = options.interface
new_mac = options.mac_address

print("changing the mac address to " + new_mac)

macchanger(options.interface , options.mac_address)


#this part is a insecure way since user can pause any commands following a : and  it gets executed so use the list method
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac , shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)


