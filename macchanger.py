#! /usr/bin/python

import subprocess
import optparse
import re

def macchanger ( interface , new_mac ):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_arguments():
    parse = optparse.OptionParser()
    parse.add_option("-i", "--interface", dest="interface", help="set interface using this flag")
    parse.add_option("-m", "--mac", dest="mac_address", help="set the new mac address")
    (options , arguments) = parse.parse_args()
    print("changing the mac address of " + options.interface + " to " + options.mac_address)
    if not options.interface:
         parse.error("give a interface")
    elif not options.mac_address:
         parse.error("give a valid mac address")
    return options

def get_macaddress(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    print(ifconfig_result)
    result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if result:
        return result.group(0)
    else:
        print("not found")


options = get_arguments()
current_mac = get_macaddress(options.interface)
print("current mac = " + str(current_mac))

macchanger(options.interface , options.mac_address)
current_mac = get_macaddress(options.interface)
if current_mac == options.mac_address:
    print("mac changed sucessfullu")
else:
    print("mac address not changed ")

#this part is a insecure way since user can pause any commands following a : and  it gets executed so use the list method
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac , shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)


