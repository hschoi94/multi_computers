import os 
import platform
import shutil

_script_root_path = os.path.abspath(os.path.dirname(__file__)) 
_script_path = os.path.join(_script_root_path,"script")
_info_path = os.path.join(_script_root_path,"env")

_linux = "Linux"
_windows = "Windows"
_macos = "MAC"

if os.path.exists(_info_path) is False:
    os.mkdir(_info_path)

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

def file_read(file_path):
    with open(file_path,"r") as file:
        text = file.readlines()
    return text

def script_exec(script_path,result_path):
    cmds = file_read(script_path)
    cmd_w_log = lambda cmd:os.system(cmd+" > "+result_path)
    for cmd in cmds:
        cmd_w_log(cmd)


def get_gpu_info():
    if get_os_type() == _linux:
        gpu_script_path = os.path.join(_script_root_path,"nvidia_device.sh")
        result_path = os.path.join(_info_path,"gpu_info.info")
        if os.path.exists(result_path) is False:
            script_exec(gpu_script_path,result_path)
        info = file_read(result_path)
    else:
        info = "not used"
    return info

def get_info(work_path,command):
    pwd = os.getcwd()
    if get_os_type() in [_linux,_macos]:
        os.chdir(work_path)
        result_path = os.path.join(_info_path,"get.info")
        cmd_w_log = lambda cmd:os.system(cmd+" > "+result_path)
        if os.path.exists(result_path):
            shutil.rm(result_path)

        cmd_w_log(svn_command)

        info = file_read(result_path)
        os.chdir(pwd)
    else:
        info = "not used"
    return info

def get_disk_info():
    if get_os_type() == _linux:
        gpu_script_path = os.path.join(_script_root_path,"disk_info.sh")
        result_path = os.path.join(_info_path,"disk.info")
        if os.path.exists(result_path) is False:
            script_exec(gpu_script_path,result_path)
        info = file_read(result_path)
    else:
        info = "not used"
    return info


if __name__=="__main__":
    cmd_test = "echo hello"
    print(get_os_type())
    print(get_disk_info())
    #os.system(cmd_test)

