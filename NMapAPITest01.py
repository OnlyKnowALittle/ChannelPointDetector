#NMap_Test
import nmap

#
nm = nmap.PortScanner()

print("--Scan of Home Net 127.0.0.1--")
(nm.scan('127.0.0.1', '22-443'))
print("--Scan Info--")
print(nm.scaninfo())
print("--All Hosts Connected--")
print(nm.all_hosts())

#Tried to write a scan network function from - https://pypi.org/project/python-nmap/ -
'''
def netstat():
    nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    for host, status in hosts_list():
        print('{0}:{1}'.host)
'''
#netstat()
