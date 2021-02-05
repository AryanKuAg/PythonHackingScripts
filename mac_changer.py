#!/usr/bin/env python3

import subprocess
import optparse


def parsed_values():
    parse = optparse.OptionParser()
    parse.add_option('-i', '--interface', dest='interface', help='Interface to change its MAC Address')
    parse.add_option('-m', '--mac', dest='my_mac', help='Your own mac address that you wanna set to')
    (options, arguments) = parse.parse_args()
    if not options.interface:
        parse.error('[-] Please specify an interface!!')
    elif not options.my_mac:
        parse.error('[-] Please specify a mac address!!')
    return options


def process_working(interface, new_man):
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_man])
    subprocess.call(['ifconfig', interface, "up"])

    print('[+] The interface ' + interface + 'mac changes to ' + new_man)


options = parsed_values()
process_working(options.interface, options.my_mac)