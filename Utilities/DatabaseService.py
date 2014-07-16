__author__ = 'phagen'


import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import win32api
import win32evtlogutil
from Utilities import ParsePhoneBook


class FloorMapSvc (win32serviceutil.ServiceFramework):

    _svc_name_ = "FloorMapSvc"
    _svc_display_name_ = "Floor Map Service"

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.setevent(self.hWaitStop)

    def SvcDoRun(self):
        self.timeout = 120000

        while 1:
            #Wait for service stop signal, if timeout, loop again
            rc = win32event.waitforsingleobject(self.hWaitStop, self.timeout)
            #Check to see if self.hWaitStop Happened
            if rc == win32event.WAIT_OBJECT_0:
                servicemanager.LogInfoMsg("FloorMapSvc Stop")
                break
            else:
                ParsePhoneBook.parse()

def ctrlHandler(ctrlType):
    return True

if __name__ == "__main__":
    win32api.SetConsoleCtrlHandler(ctrlHandler,True)
    win32serviceutil.HandleCommandLine(FloorMapSvc)


