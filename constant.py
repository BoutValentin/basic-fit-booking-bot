# An header value
SET_COOKIE = 'Set-Cookie'

# The user agent we use to not being rejected by the basic fit API
USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36'

# The origin header value
ORIGIN = "https://my.basic-fit.com"

# The default header to use to request the API
DEF_HEADERS = {
    'Host': 'my.basic-fit.com',
    'origin': 'https://my.basic-fit.com',
    'mbf-rct-app-api-2-caller': 'true',
    'mbfloginheadvform': 'jk#Bea201',
    'User-Agent':  USER_AGENT,
    'Content-Type': 'application/json',

}

# Path useful in our application
PATH = {
    'front_login': '/login',
    'api_login': '/authentication/login',
    'api_op_bo': '/door-policy/get-open-reservation',
    'api_avail': '/door-policy/get-availability',
    'api_books': '/door-policy/book-door-policy'
}

# Message Return when booking succeed
BOOKING_MSG = 'Booked'

# Date format
O_DATE_FORMAT = "%Y-%m-%d"
DATE_FORMAT = O_DATE_FORMAT + "T%H:%M:%S.%f"

