import base64
import os
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Base64coder!!")
print(ascii_banner)
# options encode - decode
option = int(input('''
1. Encode
2. Decode
 ''' ))
# encode
if option == 1:
    coded_string = input("Insert the code... \n") 
    b = coded_string.encode("UTF-8")
    e = base64.b64encode(b)
    print("The code is: "+e)
    os.system('pause')
# decode
elif option == 2:
    coded_string = input("Insert the code... \n") 
    r = base64.b64decode(coded_string)
    print("The decode is: "+r)
    os.system('pause')
else :
    print("Invalid option ")
