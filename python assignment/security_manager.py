# code for:
# i. Blocking USB Ports and Disabling Bluetooth.
# ii. Disabling Command Prompt.
# iii. Blocking Website Access


import winreg  # interacts with windows registry
import wmi  # interacts with windows management instrumentation


def Disabling_usb_ports():
    try:
        key = winreg.HKEY_LOCAL_MACHINE  # assigning top-level registry key
        # path for USBSTOR service's registry key
        sub_key = r"SYSTEM\CurrentControlSet\Services\USBSTOR"
        # opening the key with write access to change the key
        # with block to close the key after changing the values
        with winreg.OpenKey(key, sub_key, 0, winreg.KEY_SET_VALUE) as r_key:
            # getting the access to write using the 0 parameter.
            # assigning key to reg_key
            # Disable USB storage
            winreg.SetValueEx(r_key, "Start", 0, winreg.REG_DWORD, 4)
            # disabling the usb by setting the value as 4

        print("USB ports successfully disabled !!!")
    except Exception as e:
        print("Error occured during disabling the usb ports:", str(e))


def Disabling_Bluetooth():  # method to disable bluetooth
    try:
        abc = wmi.WMI()
        for it in abc.Win32_PnPEntity():  # using Win32_PnpEntity() to search for bluetooth device
            if "Bluetooth" in it.Description:
                it.Disable()  # disabling the bluetooth
                print("Bluetooth disabled.")
                break
        else:
            print("Bluetooth device not found.")
    except Exception as ex:
        print("Error while disabling the bluetooth:", str(ex))


def block_fb_website(website):  # method to block the website
    try:
        path_of_hosts_file = r'C:\Windows\System32\drivers\etc\hosts'
        redirect_ip = '127.0.0.1'

        with open(path_of_hosts_file, 'a') as file:  # opening host_path to append
            file.write(f'\n{redirect_ip} {website}')  # blocking the website

        print(f'{website} blocked.')
    except Exception as exp:
        print('Error occured while blocking the website:', str(exp))


def Restricting_CMD():  # method to restrict the cmd
    try:
        Key = winreg.HKEY_CURRENT_USER
        sub_key = r"Software\Policies\Microsoft\Windows\System"
        with winreg.OpenKey(Key, sub_key, 0, winreg.KEY_SET_VALUE) as reg_key:
            # Disable Command Prompt
            # setting the value's data to the DWORD 2 to disable the cmd

            winreg.SetValueEx(reg_key, "DisableCMD", 0, winreg.REG_DWORD, 2)

        print("Command Prompt restricted.")
    except Exception as exp:
        print("Error:", str(exp))


def main():
    # Disable USB Ports:
    Disabling_usb_ports()

    # Disable Bluetooth :
    Disabling_Bluetooth()

    # Block Website:
    website_to_block = "facebook.com"
    block_fb_website(website_to_block)

    # Restrict Command Prompt:
    Restricting_CMD()


if __name__ == "__main__":
    main()
