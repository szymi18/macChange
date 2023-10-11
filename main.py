print("Change yout mac address from : to -")

def change_mac(mac_address):
    if third_character == ":":
        return mac_address.replace(":", "-")
    else:
        return mac_address.replace("-", ":")

mac_address = input("Paste your mac address: ")
third_character = mac_address[2]
mac_new = change_mac(mac_address)
print("Your mac address after change: ", mac_new)
