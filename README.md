# setdns
Python scrip to manipulate dns servers on osx.

## Setup
Update dns_servers and interfaces to match system settings and desired servers.

## Usage
* setdns.py clear
  - This will clear dns servers from all interfaces.
* setdns.py flip
  - This will set dns to the first server if unset or flip between them if already set.
