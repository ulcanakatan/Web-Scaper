import urllib.request
import os
from urllib.error import HTTPError


path = "/home/kali/Desktop/"
ext = ".png"
url = input('URL>> ')
mod = input('Module Name>> ')
sub = input('Sub Name>> ')
modpath = path + mod + '/'
fullpath = path + mod + '/' + sub + '/'
done = 0

make = input('create folders ?> (y/n) \n')
if make == 'y' or make == 'yes':
    loop = 1
    while loop == 1:
        try:
            os.mkdir(modpath)
            os.mkdir(fullpath)
        except OSError:
            print("Creation of the directory failed")
        else:
            print("Successfully created the directory")
else:
    print('Reset :(')

get = input('Download files ?> (y/n) \n')

if get == 'y' or get == 'yes':
    run = True
    count = 1
    while run:
        print('start')
        fnum = str()
        if len(str(count)) == 1:
            fnum = '00000' + str(count)
        elif len(str(count)) == 2:
            fnum = '0000' + str(count)
        elif len(str(count)) == 3:
            fnum = '000' + str(count)
        else:
            print('error print size dont make sense')

        try:
            conn = urllib.request.urlopen(url + fnum + ext)
            code = conn.getcode()
        except urllib.error.HTTPError:
            print('Done!')
            break

        os.chdir(fullpath)
        urllib.request.urlretrieve(url + fnum + ext, sub + str(count) + ext)
        print(str(count) + 'downloaded')
        count = count + 1


else:
    print('Reset :(')


def newsetup():
    url2 = input('URL>> ')
    sub2 = input('Sub Name>> ')
    fullpath2 = path + mod + '/' + sub2 + '/'
    make2 = input('create folders ?> (y/n) \n')
    if make2 == 'y' or make2 == 'yes':
        try:
            os.mkdir(fullpath2)
        except OSError:
            print("Creation of the directory failed")
        else:
            print("Successfully created the directory")
    else:
        print('reset dude :(')

    get2 = input('Download files ?> (y/n) \n')

    if get2 == 'y' or get2 == 'yes':
        run2 = True
        count2 = 1
        while run2:
            print('start')
            fnum2 = str()
            if len(str(count2)) == 1:
                fnum2 = '00000' + str(count2)
            elif len(str(count2)) == 2:
                fnum2 = '0000' + str(count2)
            elif len(str(count2)) == 3:
                fnum2 = '000' + str(count2)
            else:
                print('error print size dont make sense')

            try:
                conn2 = urllib.request.urlopen(url2 + fnum2 + ext)
                code2 = conn2.getcode()
            except urllib.error.HTTPError:
                print('Done!')
                break

            os.chdir(fullpath2)
            urllib.request.urlretrieve(url2 + fnum2 + ext, sub2 + str(count2) + ext)
            print(str(count2) + 'downloaded')
            count2 = count2 + 1

    else:
        print('Reset :(')


def options():
    print('- new for new sub')
    print('- start to download')


def command():
    cmd = input('>>> ')
    while cmd != 'exit':

        if cmd == '--help':
            options()
            break

        elif cmd == 'new':
            newsetup()
            break
    if cmd == 'exit':
        print('Thanks for using the tool <3')


while True:
    command()
