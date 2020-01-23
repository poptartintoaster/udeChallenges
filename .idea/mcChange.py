#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

interface = raw_input("interface > ")
new_mac = raw_input("new Mac > ")

print("[+} Changing Mac address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig" , interface, "down"])
subprocess.call(["ifconfig" , interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig" , interface, "up"])



