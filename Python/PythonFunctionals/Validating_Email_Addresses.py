
import re

def fun(s):
    # return True if s is a valid email, else return False
    reg="^([a-z,A-Z,0-9,_,-])+@([a-z,A-Z,0-9])+\.([a-z]){1,3}$"
    return bool( re.match(reg,s))



def filter_mail(emails):
    return list(filter(fun,emails))

if __name__ == '__main__':
    emails=['bri@an-23@hackerrank.com', 'britts_54@hackerrank.com']
    filtered_emails= filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)