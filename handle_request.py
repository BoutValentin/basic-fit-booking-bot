import json

def handle_request(conn, method, path, payload = "", headers = {}):
    conn.request(method, path, payload, headers)
    res = conn.getresponse()
    data = res.read()
    try:
        data_dic = json.loads(data)
    except ValueError:
        data_dic = None
    return (res, data, data_dic)
