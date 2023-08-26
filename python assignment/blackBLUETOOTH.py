# code to block disable bluetooth
import wmi


def Disabling_Bluetooth():
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
        print("Error:", str(ex))


if __name__ == "__main__":
    Disabling_Bluetooth()
