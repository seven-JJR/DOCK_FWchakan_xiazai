from Dock_ui import Ui_MainWindow #从UI的PY文件到导入Ui_MainWindow ，只有这里是必须的格式，其余根据需要导入
from PyQt5 import QtCore, QtGui, QtWidgets#这里是必须的，为了运行if main

from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtWidgets import QMessageBox
import threading
import requests
import re
import  json
from PyQt5.QtCore import pyqtSignal
import urllib.request

dock_list=['ThinkPad Hybrid USB-C and USB-A Dock',
'ThinkPad USB-C Dock Gen 2',
'ThinkPad Thunderbolt 3 Dock Gen 2',
'ThinkPad Universal Thunderbolt 4 Dock',
'ThinkPad Universal Thunderbolt 4 Smart Dock',
'ThinkPad Universal USB-C Dock',
'ThinkPad Universal USB-C Smart Dock',
'Lenovo USB-C Universal Business Dock',
'Thinkpad Universal USB-C Dock v2',
'Lenovo USB Travel Hub Gen2']
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
#---------------这一部分是UI逻辑分离固定格式
class MainWindow(QMainWindow, Ui_MainWindow):
    mysignal = pyqtSignal(str)# 代表信号以字符串方式发送, 只能定义在这里，不能定义在类外部或者init里面
    mysignal1 = pyqtSignal(str)
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
#---------------这一部分是UI逻辑分离固定格式
        self.comboBox.addItems(dock_list)
        self.pushButton.clicked.connect(self.dock_FW_check_xc)# 连接先吃，用线程去对应function, 避免UI主线程卡死
        self.pushButton_2.clicked.connect(self.dock_FW_download_xc)  # 连接先吃，用线程去对应function, 避免UI主线程卡死
        self.mysignal1.connect(self.downlaod_prompt)
        self.mysignal.connect(self.version_prompt)#发送信号要执行的函数，如果一个button连接线程函数后，线程函数又连接另一个函数，这时候另一个函数中的过程就不允许QMessage BOX执行，会卡死，所以用信号执行
        #QMessage BOX 也可以直接在线程函数里面执行
    def version_prompt(self):
        QMessageBox.information(MainWindow, '提示', f'当前Dock/Hub官网最新FW版本是:{version_value}')
    def downlaod_prompt(self):
        QMessageBox.information(MainWindow, '提示', "下载完成")
    def dock_FW_check_xc(self):
        tr_1 = threading.Thread(target=self.dock_FW_check)
        tr_1.setDaemon(True)
        tr_1.start()

    def dock_FW_download_xc(self):
        tr_1 = threading.Thread(target=self.dock_FW_download)
        tr_1.setDaemon(True)
        tr_1.start()

    def dock_FW_check(self):
        global version_value# 全局变量是在某个函数内定义的值想要在其他地方被用，就用global，而不是说随便在哪里定义一个global ，所有代码都可以用
        if self.comboBox.currentText()=='ThinkPad Hybrid USB-C and USB-A Dock':
            res = requests.get(url="https://pcsupport.lenovo.com/us/en/downloads/DS504448", headers=headers)
            version= re.findall('''"TypeString":"TXT README".*Size''', res.text)#返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            version_1="{"+version[0].replace(''',"Size''','')+"}"  #转为字典形式的字符串, 去除除字典外的其余格式例如URL字眼
            version_dict=json.loads(version_1)#转为字典
            version_value=version_dict["Version"]#获取版本值
            self.mysignal.emit('x')#发送信号
        elif self.comboBox.currentText()=='ThinkPad USB-C Dock Gen 2':
            res = requests.get(url="https://pcsupport.lenovo.com/us/en/downloads/DS539092", headers=headers)
            version = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            version_1 = "{" + version[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如URL字眼
            version_dict = json.loads(version_1)  # 转为字典
            version_value = version_dict["Version"]  # 获取版本值
            self.mysignal.emit('x')  # 发送信号
        elif self.comboBox.currentText() == 'ThinkPad Thunderbolt 3 Dock Gen 2':
            res = requests.get(url="https://pcsupport.lenovo.com/us/en/downloads/DS505188", headers=headers)
            version = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            version_1 = "{" + version[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如URL字眼
            version_dict = json.loads(version_1)  # 转为字典
            version_value = version_dict["Version"]  # 获取版本值
            self.mysignal.emit('x')  # 发送信号
        elif self.comboBox.currentText() == 'ThinkPad Universal Thunderbolt 4 Dock':
            res = requests.get(url="https://support.lenovo.com/us/en/downloads/ds554336", headers=headers)
            version = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            version_1 = "{" + version[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如URL字眼
            version_dict = json.loads(version_1)  # 转为字典
            version_value = version_dict["Version"]  # 获取版本值
            self.mysignal.emit('x')  # 发送信号
        elif self.comboBox.currentText() == 'ThinkPad Universal Thunderbolt 4 Smart Dock':
            res = requests.get(url="https://support.lenovo.com/us/en/downloads/ds555864", headers=headers)
            version = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            version_1 = "{" + version[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如URL字眼
            version_dict = json.loads(version_1)  # 转为字典
            version_value = version_dict["Version"]  # 获取版本值
            self.mysignal.emit('x')  # 发送信号
        elif self.comboBox.currentText() == 'ThinkPad Universal USB-C Dock':
            res = requests.get(url="https://pcsupport.lenovo.com/us/en/downloads/ds548947", headers=headers)
            version = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            version_1 = "{" + version[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如URL字眼
            version_dict = json.loads(version_1)  # 转为字典
            version_value = version_dict["Version"]  # 获取版本值
            self.mysignal.emit('x')  # 发送信号
        elif self.comboBox.currentText() == 'ThinkPad Universal USB-C Smart Dock':
            res = requests.get(url="https://support.lenovo.com/us/en/downloads/ds554802", headers=headers)
            version = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            version_1 = "{" + version[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如URL字眼
            version_dict = json.loads(version_1)  # 转为字典
            version_value = version_dict["Version"]  # 获取版本值
            self.mysignal.emit('x')  # 发送信号
        elif self.comboBox.currentText() == 'Lenovo USB-C Universal Business Dock':
            res = requests.get(url="https://support.lenovo.com/us/en/downloads/DS559021", headers=headers)
            version = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            version_1 = "{" + version[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如URL字眼
            version_dict = json.loads(version_1)  # 转为字典
            version_value = version_dict["Version"]  # 获取版本值
            self.mysignal.emit('x')  # 发送信号
        elif self.comboBox.currentText() == 'Thinkpad Universal USB-C Dock v2':
            res = requests.get(url="https://support.lenovo.com/us/en/downloads/DS563328", headers=headers)
            version = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            version_1 = "{" + version[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如URL字眼
            version_dict = json.loads(version_1)  # 转为字典
            version_value = version_dict["Version"]  # 获取版本值
            self.mysignal.emit('x')  # 发送信号
        elif self.comboBox.currentText() == 'Lenovo USB Travel Hub Gen2':
            res = requests.get(url="https://pcsupport.lenovo.com/us/en/downloads/ds550428", headers=headers)
            version = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            version_1 = "{" + version[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如URL字眼
            version_dict = json.loads(version_1)  # 转为字典
            version_value = version_dict["Version"]  # 获取版本值
            self.mysignal.emit('x')  # 发送信号
    def dock_FW_download(self):
        if self.comboBox.currentText()=='ThinkPad Hybrid USB-C and USB-A Dock':
            res = requests.get(url="https://pcsupport.lenovo.com/us/en/downloads/DS504448", headers=headers)
            download_url= re.findall('''"TypeString":"TXT README".*Size''', res.text)#返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            download_url_1="{"+download_url[0].replace(''',"Size''','')+"}"  #转为字典形式的字符串, 去除除字典外的其余格式例如Size字眼
            downloadu_url_dict=json.loads(download_url_1)#转为字典
            download_url_value=downloadu_url_dict["URL"]#获取完整下载地址
            url=download_url_value.replace("txt","exe")#因为txt和exe下载地址完全一样只有后缀不一样，前面获取的txt下载地址改为exe就行了
            urllib.request.urlretrieve(url,url[43:])# urllib.request.urlretrieve(url,文件名自定义）, 这里取下载的原始名字
            self.mysignal1.emit('x')#发送信号
        elif self.comboBox.currentText()=='ThinkPad USB-C Dock Gen 2':
            res = requests.get(url="https://pcsupport.lenovo.com/us/en/downloads/DS539092", headers=headers)
            download_url = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            download_url_1 = "{" + download_url[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如Size字眼
            downloadu_url_dict = json.loads(download_url_1)  # 转为字典
            download_url_value = downloadu_url_dict["URL"]  # 获取完整下载地址
            url = download_url_value.replace("txt", "exe")# 因为txt和exe下载地址完全一样只有后缀不一样，前面获取的txt下载地址改为exe就行了
            urllib.request.urlretrieve(url, url[43:])  # urllib.request.urlretrieve(url,文件名自定义）, 这里取下载的原始名字
            self.mysignal1.emit('x')  # 发送信号
        elif self.comboBox.currentText() == 'ThinkPad Thunderbolt 3 Dock Gen 2':
            res = requests.get(url="https://pcsupport.lenovo.com/us/en/downloads/DS505188", headers=headers)
            download_url = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            download_url_1 = "{" + download_url[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如Size字眼
            downloadu_url_dict = json.loads(download_url_1)  # 转为字典
            download_url_value = downloadu_url_dict["URL"]  # 获取完整下载地址
            url = download_url_value.replace("txt", "exe") # 因为txt和exe下载地址完全一样只有后缀不一样，前面获取的txt下载地址改为exe就行了
            urllib.request.urlretrieve(url, url[43:])  # urllib.request.urlretrieve(url,文件名自定义）, 这里取下载的原始名字
            self.mysignal1.emit('x')  # 发送信号
        elif self.comboBox.currentText() == 'ThinkPad Universal Thunderbolt 4 Dock':
            res = requests.get(url="https://support.lenovo.com/us/en/downloads/ds554336", headers=headers)
            download_url = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            download_url_1 = "{" + download_url[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如Size字眼
            downloadu_url_dict = json.loads(download_url_1)  # 转为字典
            download_url_value = downloadu_url_dict["URL"]  # 获取完整下载地址
            url = download_url_value.replace("txt", "exe")  # 因为txt和exe下载地址完全一样只有后缀不一样，前面获取的txt下载地址改为exe就行了
            urllib.request.urlretrieve(url, url[43:])  # urllib.request.urlretrieve(url,文件名自定义）, 这里取下载的原始名字
            self.mysignal1.emit('x')  # 发送信号
        elif self.comboBox.currentText() == 'ThinkPad Universal Thunderbolt 4 Smart Dock':
            res = requests.get(url="https://support.lenovo.com/us/en/downloads/ds555864", headers=headers)
            download_url = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            download_url_1 = "{" + download_url[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如Size字眼
            downloadu_url_dict = json.loads(download_url_1)  # 转为字典
            download_url_value = downloadu_url_dict["URL"]  # 获取完整下载地址
            url = download_url_value.replace("txt", "exe")  # 因为txt和exe下载地址完全一样只有后缀不一样，前面获取的txt下载地址改为exe就行了
            urllib.request.urlretrieve(url, url[43:])  # urllib.request.urlretrieve(url,文件名自定义）, 这里取下载的原始名字
            self.mysignal1.emit('x')  # 发送信号
        elif self.comboBox.currentText() == 'ThinkPad Universal USB-C Dock':
            res = requests.get(url="https://pcsupport.lenovo.com/us/en/downloads/ds548947", headers=headers)
            download_url = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            download_url_1 = "{" + download_url[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如Size字眼
            downloadu_url_dict = json.loads(download_url_1)  # 转为字典
            download_url_value = downloadu_url_dict["URL"]  # 获取完整下载地址
            url = download_url_value.replace("txt", "exe")  # 因为txt和exe下载地址完全一样只有后缀不一样，前面获取的txt下载地址改为exe就行了
            urllib.request.urlretrieve(url, url[43:])  # urllib.request.urlretrieve(url,文件名自定义）, 这里取下载的原始名字
            self.mysignal1.emit('x')  # 发送信号
        elif self.comboBox.currentText() == 'ThinkPad Universal USB-C Smart Dock':
            res = requests.get(url="https://support.lenovo.com/us/en/downloads/ds554802", headers=headers)
            download_url = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            download_url_1 = "{" + download_url[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如Size字眼
            downloadu_url_dict = json.loads(download_url_1)  # 转为字典
            download_url_value = downloadu_url_dict["URL"]  # 获取完整下载地址
            url = download_url_value.replace("txt", "exe")  # 因为txt和exe下载地址完全一样只有后缀不一样，前面获取的txt下载地址改为exe就行了
            urllib.request.urlretrieve(url, url[43:])  # urllib.request.urlretrieve(url,文件名自定义）, 这里取下载的原始名字
            self.mysignal1.emit('x')  # 发送信号
        elif self.comboBox.currentText() == 'Lenovo USB-C Universal Business Dock':
            res = requests.get(url="https://support.lenovo.com/us/en/downloads/DS559021", headers=headers)
            download_url = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            download_url_1 = "{" + download_url[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如Size字眼
            downloadu_url_dict = json.loads(download_url_1)  # 转为字典
            download_url_value = downloadu_url_dict["URL"]  # 获取完整下载地址
            url =  download_url_value.replace("txt", "exe")  # 因为txt和exe下载地址完全一样只有后缀不一样，前面获取的txt下载地址改为exe就行了
            urllib.request.urlretrieve(url, url[43:])  # urllib.request.urlretrieve(url,文件名自定义）, 这里取下载的原始名字
            self.mysignal1.emit('x')  # 发送信号
        elif self.comboBox.currentText() == 'Thinkpad Universal USB-C Dock v2':
            res = requests.get(url="https://support.lenovo.com/us/en/downloads/DS563328", headers=headers)
            download_url = re.findall('''"TypeString":"TXT README".*Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            download_url_1 = "{" + download_url[0].replace(''',"Size''', '') + "}"  # 转为字典形式的字符串, 去除除字典外的其余格式例如Size字眼
            downloadu_url_dict = json.loads(download_url_1)  # 转为字典
            download_url_value = downloadu_url_dict["URL"]  # 获取完整下载地址
            url = download_url_value.replace("txt", "exe")  # 因为txt和exe下载地址完全一样只有后缀不一样，前面获取的txt下载地址改为exe就行了
            urllib.request.urlretrieve(url, url[43:])  # urllib.request.urlretrieve(url,文件名自定义）, 这里取下载的原始名字
            self.mysignal1.emit('x')  # 发送信号
        elif self.comboBox.currentText() == 'Lenovo USB Travel Hub Gen2':
            res = requests.get(url="https://pcsupport.lenovo.com/us/en/downloads/ds550428", headers=headers)
            download_url = re.findall('''"TypeString":"EXE".*?Size''',res.text)  # 返回列表，长度为1.因为被查找的目标中含有双引号，所以这里用‘’‘   ’‘’ 才不出错
            download_url_1 = "{" + download_url[0].replace(''',"Size''', '') + "}"   # 转为字典形式的字符串, 去除除字典外的其余格式例如Size字眼
            downloadu_url_dict = json.loads(download_url_1)  # 转为字典
            download_url_value = downloadu_url_dict["URL"]  # 获取完整下载地址
            urllib.request.urlretrieve(download_url_value, download_url_value[45:])  # urllib.request.urlretrieve(url,文件名自定义）, 这里取下载的原始名字
            self.mysignal1.emit('x')  # 发送信号

if __name__ == '__main__':
    import sys
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应分辨率
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())