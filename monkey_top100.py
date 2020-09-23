"""
@Time:2020/9/18 11:39
@Author:周洁红
"""
'''
monkey+Python测试步骤：
1.获取apk包的路径
2.根据路径安装apk
3.获取每个apk包名
4.调用monkey进行操作
5.获取并分析日志
6.检查日志并判断是否存在 anr或crash等关键字，并标识结果
7.卸载apk
'''
import os
import re
class MonkeyTop100:
    # 获取apk包的路径
    def get_app_path(self):
        path=[]
        for filename in os.listdir(r'C:\resource\app'):
            path.append('C:/resource/app/'+filename)

        return path

    # 根据路径安装apk
    def install_apk(self,apk_path):
        print("正在安装……")
        cmd="adb install "+apk_path
        res=os.popen(cmd)
        return 'Success' in res.read()

    # 获取每个apk包名
    def get_package_name(self,apk_path):
        cmd="aapt dump badging "+apk_path
        res=os.popen(cmd)
        content=res.buffer.read().decode(encoding='utf8')
        result=re.findall("name='(.*?)'",content)
        return result[0]

    # 调用monkey进行操作
    def monkey_op(self,packageName):
        print("正在测试……")
        cmd="adb shell monkey -p "+packageName+" --monitor-native-crashes --pct-touch 50 --pct-motion 50 --pct-syskeys 0 --throttle 300 -v -v -v 1000> C:/resource/app/log.txt"
        res=os.popen(cmd)
        if 'crash' in res.read().lower():
            return 'fail'
        else:
            return 'pass'

    # 卸载apk
    def uninstall_apk(self,packageName):
        print("正在卸载……")
        cmd="adb uninstall "+packageName
        res=os.popen(cmd)
        print(res.read())


if __name__ == '__main__':
    app=MonkeyTop100()
    result_dic={}
    for apk_path in app.get_app_path():#找到每一个apk的path
        if app.install_apk(apk_path):
            package_name=app.get_package_name(apk_path)
            result=app.monkey_op(package_name)
            result_dic[package_name]=result
            app.uninstall_apk(package_name)
        else:
            print("安装失败！")

    print(result_dic)