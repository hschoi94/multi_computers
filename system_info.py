import os 
import platform

def get_os_type():
    mac_os = ["Darwin","macOS"]
    windows = ["windows","Windows"]
    linux = ["Linux", "linux", "Ubuntu", "ubuntu"]
    
    os_dict = {
        "MAC":mac_os,
        "Windows":windows,
        "Linux":linux
    }
    
    os_keys = os_dict.keys()
        
    os_name = platform.system()
    
    os_type = ""
    
    for os_key in os_keys:
        if os_name in os_dict[os_key]:
            os_type = os_key
            break
    return os_type

cmd_test = "echo hello"
print(get_os_type())
#os.system(cmd_test)

