#!/usr/bin/env python

from subprocess import call
import sys
import argparse
import urllib
import os

def get_data_from_file(file_name):
    with open(file_name) as f:
        return f.readlines()

def run_chrome(company_list, queries):
    if os.name=="nt":
        call_chrome = ["start","chrome"]
    else:
        call_chrome = ["google-chrome"]
    for i in company_list:
        for j in queries:
            # Add "" to company. replace spaces by + . 
            name_str = urllib.quote_plus('"'+i+'"')
            query_str = j.replace(" ", "+")
            query =  name_str + "+" + query_str
            call(call_chrome + ["https://www.google.co.uk/#q="+query])

def main():
    """
       usage: check_startup.py [-h] [-list companies_line_separated_list] [-one company]
    """
    # Get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", help="File with campany names, line separated.")
    parser.add_argument("--one", help="One company name.")
    parser.add_argument("--queries", help="Queries to do.")
    args = parser.parse_args()
    # Where are the queries ?
    if args.queries:
        queries_file = args.queries
    else:
        queries_file = "queries.txt"
    # Get queries
    queries = get_data_from_file(queries_file)
    # one company or a list ? - get company list
    if args.one:
        company_list = [args.one]
    elif args.list:
        company_list = get_data_from_file(args.list)
    else:
        company_list = get_data_from_file("companies.txt")
    # Run all in browser
    run_chrome(company_list, queries)

if __name__ == "__main__":
    main()
