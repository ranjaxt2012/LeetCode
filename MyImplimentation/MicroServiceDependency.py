from collections import deque

ServiceList = {"a": {1, 2, 3},
               "b": {4, 5, 6},
               "c": {1, 5, 3}
               }


def GetServiceRegistryByServer(ServiceList):
    ServiceListByServer = {}
    for ServiceName in ServiceList:

        for ServerName in ServiceList[ServiceName]:
            if ServiceListByServer.has_key(ServerName):
                EXISTING_VALUES = ServiceListByServer[ServerName]
                EXISTING_VALUES.append(ServiceName)
                ServiceListByServer[ServerName] = EXISTING_VALUES
            else:
                ServiceListByServer[ServerName] = [ServiceName]

    return ServiceListByServer


def RebootServer(ServiceListByServer):
    if len(ServiceListByServer) == 0:
        return
    else:
        ServiceUnderReboot = []
        ServerRebooted = []
        ServerRebooting = deque()
        ServerRebootingNumber = 0

        COUNT = len(ServiceListByServer)
        for ServerName in ServiceListByServer:
            if ServerName not in ServerRebooted:
                print("Trying to reboot " + str(ServerName))
                COUNT -= 1

                if ServerRebootingNumber == 0 and ServerName not in ServerRebooted:
                    print ("Rebooting Server ", ServerName)
                    ServerRebooting.append(ServerName)
                    ServerRebootingNumber += 1
                    print ("Service under reboot " + str(ServiceListByServer[ServerName]))
                    for S in ServiceListByServer[ServerName]:
                        ServiceUnderReboot.append(S)
                    ServerRebooted.append(ServerName)


                elif ServerRebootingNumber == 1 and ServerName not in ServerRebooted:
                    Server_Ready_Restart = True
                    for S in str(ServiceListByServer[ServerName]):
                        if S in ServiceUnderReboot:
                            print ("Service (" + S + ") Under Reboot..." +
                                   " Server Number (" + str(ServerName) + ") can not be restarted")
                            Server_Ready_Restart = False
                    if Server_Ready_Restart:
                        print ("Rebooting Server ", ServerName)
                        ServerRebooting.append(ServerName)
                        ServerRebootingNumber += 1
                        print ("Service under reboot " + str(ServiceListByServer[ServerName]))
                        for S in ServiceListByServer[ServerName]:
                            ServiceUnderReboot.append(S)
                        ServerRebooted.append(ServerName)

                elif ServerRebootingNumber > 1:
                    ServerCompletedRebooting = ServerRebooting.popleft()
                    print ("Server Completed Rebooting " + str(ServerCompletedRebooting))
                    for S in ServiceListByServer[ServerCompletedRebooting]:
                        ServiceUnderReboot.remove(S)
                    print ("Removed Services from ServiceUnderReboot List..." +
                           str(ServiceListByServer[ServerCompletedRebooting]))

    if COUNT == 0:
        print ("Servers Rebooted In This Round... " + str(ServerRebooted) + "\n")
        for S in ServerRebooted:
            if S in ServiceListByServer:
                ServiceListByServer.pop(S)
        RebootServer(ServiceListByServer)


ServiceListByServer = GetServiceRegistryByServer(ServiceList)
RebootServer(ServiceListByServer)
