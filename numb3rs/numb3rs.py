import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if matches:
        return all(check_number(matches.group(i)) for i in range(1, 5))
    return False

def check_number(n):
    try:
        n = int(n)
        if 0 <= n <= 255:
            return True
        return False
    except ValueError:
        return False

if __name__ == "__main__":
    main()
