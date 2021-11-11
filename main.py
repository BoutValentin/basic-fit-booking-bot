import http.client
import json
import datetime
import sys
import time
from dotenv import load_dotenv
import os
import ssl
from constant import *
from check_arguments import check_args
from cookies import create_dic_cookies_from_headers, create_cookies_from_dic, create_cookies_from_set_cookies_headers
from handle_request import handle_request
from find_matching_date import create_tomorrow, find_matching_date

load_dotenv() # We load the .env file

check_args(sys.argv) # We check if all arguments are correctly given

ssl._create_default_https_context = ssl._create_unverified_context # We create an ssl context for our request

conn = http.client.HTTPSConnection("my.basic-fit.com") # We create a connextion object to handle our request

# STEP 1: Retrieve some default-cookie by searching in the set-cookies headers: We do that by performing a default request
print("[*] Connecting to my.basic-fit.com as a frontend...")

# We retrieve the response from header
res_first_connec = handle_request(conn, "GET", "login", '', {'User-Agent': USER_AGENT})[0]

# We create our 'storage' string to build the cookies headers values.
dic_cookies_fst_rqs = create_dic_cookies_from_headers(res_first_connec.getheaders())
cookies = create_cookies_from_dic(dic_cookies_fst_rqs)

# STEP 2: We login 
print("[*] Login to the basic fit account...")

payload = json.dumps({
  "email": os.environ.get("BASIC_FIT_EMAIL"),
  "password": os.environ.get("BASIC_FIT_PWD"),
  "cardNumber": ""
})
headers = {
  **DEF_HEADERS,
  'referer': 'https://my.basic-fit.com/login',
  'Cookie': cookies
}
(res, data, data_dic) = handle_request(conn, "POST", PATH['api_login'], payload, headers)

# We retrieve again the cookie from set-cookie
second_request_cookies = create_dic_cookies_from_headers(res.getheaders())
merge_cookies_dic = {**dic_cookies_fst_rqs, **second_request_cookies}
merge_cookies = create_cookies_from_dic(merge_cookies_dic)

club = data_dic['member']['favorite_club']

# Check if any booking already exists
print("[*] Check if a booking is already set...")
headers_open_booking = {
        **headers,
        'Cookie': merge_cookies,
        'referer': "https://my.basic-fit.com/gym-time-booking",
        'Connection': 'keep-alive'
}

json_open_booking = handle_request(conn, "GET", PATH['api_op_bo'], '', headers_open_booking)[2] 

if len(json_open_booking['data']) > 0:
    print('[!] A booking already exist, we do not overpass this')
    exit(1)

print("[*] No booking exist")
print("[*] Trying to use your favorite club for booking: " + club['name']) 

(tomorrow, tomorrow_date_hour, tomorrow_str) = create_tomorrow(sys.argv[1])

print("[*] Getting The availability for the date " + tomorrow_str)

# Get available booking
payload = json.dumps({
    "dateTime": tomorrow_str,
    "clubId": club['id']
})

final_headers = {**headers, 
    'Cookie': merge_cookies,
    'referer': 'https://my.basic-fit.com/gym-time-booking' 
}

dts = handle_request(conn, "POST", PATH['api_avail'], payload, final_headers)[2]

matching_date = find_matching_date(dts, tomorrow_date_hour)

if matching_date is None:
    print("[!] No date can be found for you. Please try to provide a good hour.")
    exit(1)

# Elseway we send a booking request with the time wanted
print("[*] Trying to book a reservation")

payload = json.dumps({
    "doorPolicy": matching_date,
    "duration": sys.argv[2],
    "clubOfChoice": club
})

dic_booking = handle_request(conn, "POST", PATH['api_books'], payload, final_headers)[2]

if dic_booking['message'].upper() != "Booked".upper():
    print("[!] Error during the booking: ")
    print(dic_booking)
    exit(1)

print("[*] Booking done for: " + tomorrow_str + " for " + sys.argv[2] + " minutes.")

