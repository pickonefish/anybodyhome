from component import Component
from decorator import Decorator
import os
import subprocess


class ImHereComponent(Component):

    def operation(self, result):
        try:
            stream = os.popen('cat /etc/hostname')
            output = stream.readlines()
            
            result['hostname'] = """{}""".format("".join(output))
        except Exception:
            result['hostname'] = Exception


class ImHereAndOutputDateDecorator(Decorator):
    def operation(self, result) -> str:
        try:

            stream = os.popen('timedatectl show')
            output = stream.readlines()
            result['timedatectl'] = """{}""".format("".join(output)) 

            stream = os.popen('TZ=Asia/Taipei date +"%Y-%m-%d %H:%M:%S"')
            output = stream.readlines()
            result['detected_timestamp'] = """{}""".format("".join(output)) 
        except Exception:
            result['timedatectl'] = Exception
        
        self.component.operation(result)


class ImHereAndCheckSmtpAvailableDecorator(Decorator):
    def operation(self, result) -> str:
        try:
            stream = os.popen('curl smtp://mail.example.com --mail-from myself@example.com --mail-rcptreceiver@example.com --upload-file email.txt ')
            output = stream.readlines()

            result['smtp'] = """{}""".format("".join(output)) 
        except Exception:
            result['smtp'] = Exception
 
        self.component.operation(result)


class ImHereAndTelnetAvailableDecorator(Decorator):
    def operation(self, result) -> str:
        try:
            stream = os.popen('TZ=Asia/Taipei date +"%Y-%m-%d %H:%M:%S"')
            output = stream.readlines()
            result['db01'] = """{}""".format("".join(output )) 
        except Exception as e:
            result['db01'] = str(e)
 
        self.component.operation(result)


