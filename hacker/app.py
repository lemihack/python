import requests
import hashlib
import sys


def query(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError('Error Fetching')
    return res

def getleakCount(hashes,hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5 = sha1password[:5]
    tail = sha1password[5:]
    response = query(first5)
    
    return getleakCount(response,tail)



def main(args):
    for password in args:
        count = pwned_api(password)
        if count:
            print(f"{password} is already hacked {count} times. ");
        else:
            print(f"{password} is secure")




main(sys.argv[1:])