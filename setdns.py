import subprocess
import sys

class DNS:

  def get_server(interface):
  
      # List Features
      command = ['networksetup', '-getdnsservers', interface]
      process = subprocess.run(command, capture_output=True)
      result  = process.stdout.decode("utf-8").rstrip()

      if result == "There aren't any DNS Servers set on %s." % interface:
        return "empty"
      else:
        return result
  
  def set_server(interface, server):
  
      # List Features
      command = ['networksetup', '-setdnsservers', interface, server]
      process = subprocess.run(command, capture_output=True)
      result  = process.stdout.decode("utf-8").rstrip()

  def clear_server(interfaces):
  
    for interface in interfaces:
      command = ['networksetup', '-setdnsservers', interface, '"Empty"']
      process = subprocess.run(command, capture_output=True)
      result  = process.stdout.decode("utf-8").rstrip()

  def flip_server(interfaces, dns_servers):
    for interface in interfaces:
      current_setting = DNS.get_server(interface) 
      if current_setting == "empty":
        print("DNS empty on %s, setting to %s." % (interface, dns_servers[0]))
        DNS.set_server(interface, dns_servers[0])
      elif current_setting == dns_servers[0]:
        print("Switching DNS on %s to %s." % (interface, dns_servers[1]))
        DNS.set_server(interface, dns_servers[1])
      elif current_setting == dns_servers[1]:
        print("Switching DNS on %s to %s." % (interface, dns_servers[0]))
        DNS.set_server(interface, dns_servers[0])
      else:
        print("Something weird happened.")

  def usage():
    print("usage:  setdns.py clear or setdns.py flip")

def main(command, interfaces, dns_servers):
  if command == "flip": 
    DNS.flip_server(interfaces, dns_servers)
  elif command == "clear":
    DNS.clear_server(interfaces)
  else:
    print("Something weird happened.")

if __name__ == "__main__":
  args        = sys.argv
  dns_servers = ["8.8.8.8", "8.8.4.4"]
  interfaces  = [ "Wi-Fi", "Home-Dock" ]

  if len(args) != 2:
    DNS.usage()
  else:
    if args[1] == "clear" or args[1] == "flip":
      main(args[1], interfaces, dns_servers)
    else:
      DNS.usage()