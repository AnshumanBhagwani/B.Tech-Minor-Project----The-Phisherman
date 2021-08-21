#!/usr/bin/env python

import optparse
import requests
from urllib.parse import urlparse


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest = "url", help = "The URL that needs to be checked or cloned")
    parser.add_option("-f", "--function", dest = "func", help = "choose the functionality of the tool:- \n 1 = make a phishing clone \n 2 = check a link for anomaly")
    (options, arguements) = parser.parse_args()
    if not options.url:
        parser.error("[-] Please specify the url, use --help for more info.")
    if not options.func:
        parser.error("[-] Please specify the function the tool has to perform, use --help for more info")
    return options


def make_file_from_url(url):
    filename = url.split("//")[1].split(".")[0]
    res = requests.get(url)
    with open(f'{filename}.html', 'wb') as the_file:
        the_file.write(res.content)


options = get_args()
url = options.url
func = options.func
if func == "1":
    print("[+] creating the clone file named : " + options.url.split("//")[1].split(".")[0] + ".html")
    make_file_from_url(url)


#upsc.gov.in



#host an open network
#broadcast a message in the network containing the link
#host the link on your system
#redirect to the original site after getting info to avoid suspicion
#inject keylogger while you're at it
