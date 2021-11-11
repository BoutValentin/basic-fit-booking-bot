from constant import SET_COOKIE

def create_dic_cookies_from_headers(lst):
    dic = {}
    for index, tuple in enumerate(lst):
        if tuple[0].upper() == SET_COOKIE.upper(): 
            dic[tuple[1].split('=')[0].lower()] = tuple[1].split(';')[0] + ';'
    return dic

def create_cookies_from_dic(dic):
    cookies = ''
    for index,item in enumerate(dic.items()):
        if index != 0: cookies += " "
        cookies += item[1]
    return cookies[:-1]

def create_cookies_from_set_cookies_headers(lst):
    cookies = ''
    for index,tuple in enumerate(lst):
        if tuple[0].upper() == SET_COOKIE.upper():
            cookies += tuple[1].split(';')[0] + '; '
    return cookies

