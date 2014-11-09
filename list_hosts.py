#!/usr/bin/python

import boto.ec2
import argparse
import json

# Sample call: python list_hosts.py --region=us-east-1

def connect(region):
    return boto.ec2.connect_to_region(region)

def get_ec2_instances(conn):
    instances = []
    reservations = conn.get_all_reservations()
    for reservation in reservations:
        instance = reservation.instances[0]
        tags = instance.tags
        instances.append( (instance.ip_address, instance.state, tags['Name'] or '') )
    return instances

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='List EC2 hosts')
    parser.add_argument('--region')
    parser.add_argument('--filter')

    args = parser.parse_args()
    conn = connect(args.region)
    instances = get_ec2_instances(conn)
    if args.filter:
        instances = [i for i in instances if any(args.filter in i[c] for c in range(len(i)))]
    if len(instances) == 1:
        print instances[0][0] # Only print the IP
    else:
        for instance in instances:
            print '{} {} {}'.format(instance[0], instance[1], instance[2])

