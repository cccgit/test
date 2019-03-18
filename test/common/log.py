#config:utf-8
import logging
from datetime import datetime
import threading
import os
import readConfig

class Log:
    def __init__(self):
        global logPath, resultPath, proDir

        proDir = readConfig.root_dir

        resultPath = os.path.join(proDir, "result")
        #如果result文件不存在创建一个
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)

        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        self.logger = logging.getLogger() #创建一个logger
        self.logger.setLevel(logging.INFO)

        #创建一个handler,用于写入日志文件
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        #定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
class MyLog:
    log = None
    mutex = threading.lock()

    def __init__(self):
        pass
    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log

