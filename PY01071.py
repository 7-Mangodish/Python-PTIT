from math import*

if __name__ == '__main__':
    s= input()
    if s[-3:].lower() == '.py':
        print('yes')
    else:
        print('no')