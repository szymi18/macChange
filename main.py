import pyperclip

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
    print("Your mac address after change: ", mac_new)
    pyperclip.copy(mac_new)
    print("Your mac address after change is in on clipboard")

    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("Invalid input")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break
