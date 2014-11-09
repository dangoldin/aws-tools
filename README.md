aws-tools
=========

A set of utilities to make working with AWS easier.

To get started, clone the repository and install the requirements file.

```sh
pip install -r requirements
```

The following tools are currently availaible:

1. list_hosts.py - This script will connect to your AWS account and pull each of instances. You can also filter it down based on the IP address, public hostname, and the name. If the filter results in a single instance being returned, it will just be the public IP address to make it easier to connect to. For example:
```sh
ssh `./list_hosts.py --region=us-east-1 --filter="My Server"`
```