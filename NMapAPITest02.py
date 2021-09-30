#NMap_Test
import nmap

#Range of ports to be scanned
begin = 75
end = 80

#Our target
target = '127.0.0.1'

#Make a PortScanner object
scanner = nmap.PortScanner()

for i in range(begin,end+5):
    #scan the target port
    res = scanner.scan(target,str(i))
    res = res['scan'][target]['tcp'][i]['state']

    print(f'port {i} is {res}.')














'''
print("--Scan of Home Net 127.0.0.1--")
(nm.scan('127.0.0.1', '22-443'))
print("--Scan Info--")
print(nm.scaninfo())
print("--All Hosts Connected--")
print(nm.all_hosts())
'''