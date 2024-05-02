# code to block usb ports
import winreg


def Disabling_usb_ports():
    try:
        key = winreg.HKEY_LOCAL_MACHINE  # assigning top-level registry key
        # path for USBSTOR service's registry key
        sub_key = r""
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
        print("Error occured dueing disabling the usb ports:", str(e))


if __name__ == "__main__":
    Disabling_usb_ports()
