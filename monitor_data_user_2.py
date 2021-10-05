"""SỬ DỤNG WINDOW TASK SCHEDULE CHẠY ĐỊNH KÌ 10 PHÚT 1 LẦN"""
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
import os, time, sys, shutil
from program_var import *
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
def main(sleep):
    path = r"C:\Users\tvpduy\py_logistic\data_user"
    print(path)
    list_dir = os.listdir(path)
    ini_count = len(list_dir)
    print(f"Listening...at {time.strftime('%a %d %b %Y %H:%M:%S')} (Ctrl + C for shutdown) ")
    while True:
        try:
            time.sleep(sleep)
            current_count = monitor(path)
            if current_count > ini_count:
                ini_count = current_count
                raise Exception('Thêm dữ liệu')
            if current_count < ini_count:
                ini_count = current_count
                raise Exception('Xóa dữ liệu')    
            print(f"Listening...at {time.strftime('%a %d %b %Y %H:%M:%S')} (Ctrl + C for shutdown) ")
        except Exception as ex:
            if ex.args[0] == 'Thêm dữ liệu':
                print (ex,'-Nhập dữ liệu đi !!!')
            if ex.args[0] == 'Xóa dữ liệu':
                print (ex,'-Lưu trữ dữ liệu đi !!!')
            pass
#--------------------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------------------#

def monitor(path):
    return len(os.listdir(path))

#--------------------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------------------#
def get_last_path_root():
    """
        LẤY ĐƯỜNG DẪN NGUỒN TỚI CHƯƠNG TRÌNH - LẦN SỬ DỤNG GẦN NHẤT
        MÁY TÍNH CHẠY SCRIPT MONITOR NÀY PHẢI LÀ VAI TRÒ QUẢN TRỊ / MÁY CHỦ
    """
    global PATH_HOME,USER_NAME,PROGRAM_USER_DATA_FOLDER, PROGRAM_USER_DATA_SUBFOLDER_PATH
    PATH_HOME = os.path.expanduser('~')
    USER_NAME = os.getlogin()    
    PROGRAM_USER_DATA_SUBFOLDER_PATH = f"{PATH_HOME}\\{PROGRAM_USER_DATA_FOLDER}"
    print()

#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':    
    try:
        # main(5)
        get_last_path_root()
    except KeyboardInterrupt:
        quit()
