import os
import platform
import wmi
import netifaces
import psutil

system = os.name
version = platform.version()

data = "_"

def dataSys():
    if os.name == "nt":
        return "Windows"
def versionOfSystem():
    data = version.split('.')
    return data[0]
def checkWindowsSecurityCenter():
    c = wmi.WMI()
    securityCenter = c.Win32_Service(Name="wscsvc")[0]
    if securityCenter.State == "Running":
        return "true"
    else:
        return "false"
def getNetworkInterface():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        data = "".join("Интерфейс:"+ str(interface))
        addresses = netifaces.ifaddresses(interface)
        for address_family in addresses:
            if address_family == netifaces.AF_INET:
                data += "".join("\n  IPv4 адреса:")
                for entry in addresses[address_family]:
                    data += "".join(("    Адрес:", entry['addr']))
                    data += "".join(("    Маска подсети:", entry['netmask']))
                    data += "".join(("    Шлюз:", entry.get('broadcast')))
            elif address_family == netifaces.AF_INET6:
                data += "".join("\n  IPv6 адреса:")
                for entry in addresses[address_family]:
                    data += "".join(("    Адрес:", entry['addr']))
                    data += "".join(("    Маска подсети:", entry['netmask']))
                    data += "".join(("    Шлюз:", entry.get('broadcast')))
            elif address_family == netifaces.AF_LINK:
                data += "".join(("\n  MAC адрес:", addresses[address_family][0]['addr']))
    return data
def getActiveUser():
    all_processes = psutil.process_iter(attrs=['username'])
    active_users = set()
    for process in all_processes:
        username = process.info.get('username')
        if username and '\\' in username:
            domain, user = username.split('\\', 1)
            active_users.add(user)
    for user in active_users:
        return user
def getCpuUsage():
    cpu_usage = psutil.cpu_percent(interval=1)
    data = str(format(cpu_usage))
    return data