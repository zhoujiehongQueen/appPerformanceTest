"""
@Time:2020/9/23 13:25
@Author:周洁红
"""
import os,time,csv
class CpuMonitor:
    def __init__(self):
        self.data=[]
        self.counter=10

    def test_process(self,packageName):
        cmd="adb shell dumpsys cpuinfo |findstr "+packageName
        resp=os.popen(cmd)
        result=resp.read().split()[0][:-1]
        self.data.append(result)

    def run(self):
        count=1
        while count<=self.counter:
            print("正在测试第{}次数".format(count))
            self.test_process("chaoka")
            time.sleep(3)
            count+=1

    def save_data(self):
        with open('cpu.csv','w',newline='') as f:
            csv_writer=csv.writer(f)
            csv_writer.writerow(self.data)






#这个文件导入到其他文件时，下面这段代码不运行。如果没有导入到其他文件的可能，就不需要if了
if __name__ == '__main__':
    cpuMonitor=CpuMonitor()
    cpuMonitor.run()
    cpuMonitor.save_data()