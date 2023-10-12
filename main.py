import pyperclip

class color:
    new = '\033[94m'
    ENDC = '\033[0m'
    WARNING = '\033[91m'
    GREEN = '\033[92m'

while True:
    print("Change your mac address from : to - and - to :")

    def change_mac(mac_address):
        if third_character == ":":
            return mac_address.replace(":", "-")
        elif third_character == "-":
            return mac_address.replace("-", ":")
        #else:
         #   print("Invalid input")



    mac_address = input("Paste your mac address: ")
    third_character = mac_address[2]
    mac_new = change_mac(mac_address)
    print("Your mac address after change: ",color.new +  mac_new + color.ENDC)
    pyperclip.copy(mac_new)
    print("Your mac address after change is in on clipboard")

    while True:
        answer = str(input('Run again? ('+color.GREEN+'y'+color.ENDC+'/'+color.WARNING+' n'+color.ENDC+'): '))
        if answer in ('y', 'n'):
            break
        print("Invalid input")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break
