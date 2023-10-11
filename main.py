print("Change yout mac address from : to -")

def change_mac(mac_address):
    return mac_address.replace(":","-")

mac_address = input("Paste your mac address: ")
mac_new = change_mac(mac_address)
print("Your mac address after change: ", mac_new)