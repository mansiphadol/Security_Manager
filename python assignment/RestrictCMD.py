# code to restrict the cmd
import winreg


def Restricting_CMD():
    try:
        Key = winreg.HKEY_CURRENT_USER
        sub_key = r""
        with winreg.OpenKey(Key, sub_key, 0, winreg.KEY_SET_VALUE) as reg_key:
            # Disable Command Prompt
            # setting the value's data to the DWORD 2 to disable the cmd

            winreg.SetValueEx(reg_key, "DisableCMD", 0, winreg.REG_DWORD, 2)

        print("Command Prompt restricted.")
    except Exception as exp:
        print("Error:", str(exp))


if __name__ == "__main__":
    Restricting_CMD()
