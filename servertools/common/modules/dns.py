""" Class that manages dns lookup """
import sys
from datetime import datetime

from dns.resolver import NoAnswer, query

from servertools.common.misc_functions import askforhost

def dns_scan(remote_server=""):
    """ Makes a DNS scan of the given host """
    print(remote_server)
    if remote_server == "":
        remote_server = askforhost()

    print("-" * 60)
    print("DNS results for the domain: ", remote_server)
    print("-" * 60)

    mx_results = query(remote_server, "MX")
    print("")
    print("MX Results: ")
    for mx_result in mx_results:
        print("     Host: ", mx_result.exchange, " has preference ", mx_result.preference)

    ns_results = query(remote_server, "NS")
    print("")
    print("NS Results: ")
    for ns_result in ns_results:
        print("     ", ns_result)

    a_results = query(remote_server, "A")
    print("")
    print("A Results: ")
    for a_result in a_results:
        print("     ", a_result)

    print("")
    print("AAA Results: ")
    try:
        aaa_results = query(remote_server, "AAAA")
        for aaa_result in aaa_results:
            print("	 ", aaa_result)
    except NoAnswer:
        print("	 None")

    soa_results = query(remote_server, "SOA")
    print("")
    print("SOA Results: ")
    for soa_result in soa_results:
        print("     ", soa_result)

    print("")
    print("TXT Results: ")
    try:
        txt_results = query(remote_server, "TXT")
        for txt_result in txt_results:
            print("	 ", txt_result)
    except NoAnswer:
        print("	 None")
