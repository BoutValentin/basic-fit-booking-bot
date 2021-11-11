import re
def check_args(lst):
    if len(lst) < 3:
        print("[!] You need to provide the booking hour in parameters and the duration")
        exit(1)

    if re.fullmatch("\d\dh(00|15|30|45)", lst[1]) is None:
        print("[!] You need to provide an argument of form \d\dh(00|15|30|45) for the hours")
        exit(1)

    if re.fullmatch("(30|60|90)", lst[2]) is None:
        print("[!] You need to provide an argument of form (30|60|90) for the training duration")
        exit(1)

