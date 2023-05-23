import re

ip_addresses = ['255.255.255.255']

regex = '^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'

for ip_adress in ip_addresses:
    match = re.search(regex, ip_adress)

    if match:
        print(ip_adress)
