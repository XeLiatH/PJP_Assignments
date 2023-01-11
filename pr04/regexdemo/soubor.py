import re

MAIL = re.compile(r'[^"@]+@[^"]+')

def main():
    with open("ctvrtek.txt", encoding="utf-8") as ifile:
        mails = MAIL.findall(ifile.read())
    
    print(mails)

if __name__ == '__main__':
    main()