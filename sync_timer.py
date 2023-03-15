import time
import datetime

def count_until(secs):
    print(f'counting until {secs}')
    time.sleep(secs)

def main():
    print('calling multiple counters')
    print(datetime.datetime.now())
    for i in range(10):
        count_until(i)
        print(datetime.datetime.now())

    print('game is finished, thanks for joining!')
    print(datetime.datetime.now())

if __name__ == '__main__':
    main()