#!/usr/bin/env python

# Licensed Materials - Property of IBM
#
# "Restricted Materials of IBM"
#
# (C) COPYRIGHT IBM Corp. 2016   All Rights Reserved
#
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with IBM Corp.

# config-monkey.py
# Starter script to demonstrate configuration automation in Spectrum Scale cluster environment

import argparse
import sys

VERSION = '1.0'
REPO_ACTIONS = ['initialize']
CONFIG_ACTIONS = ['set', 'list', 'check']

def get_args():
    parser = argparse.ArgumentParser(description=('Example config monkey tools (version %s)' % VERSION))
    subparsers = parser.add_subparsers(help='commands')
  
    repo_parser = subparsers.add_parser('repo', help='repository commands')
    repo_parser.add_argument('repo_action',
                             help='initialize the configuration repository')
    repo_parser.add_argument('--repo-path', required=True,
                             help='Path to git repository where configuration definitions are stored')

    config_parser = subparsers.add_parser('config', help='configuration commands')
    config_parser.add_argument('cmd_action',
                               help='Tool action, valid optoions are %s' % CONFIG_ACTIONS)

    config_parser.add_argument('--profile_name',         
                               help='Name of profile to name or ip address of gpfs node to send REST'
                               'requests to')
    config_parser.add_argument('--repo-path', required=True,
                               help='Path to git repository where configuration definitions are stored')
    config_parser.add_argument('--resource',   dest='resource',
                        help='resource type from %s' % [1,2,3])
    config_parser.add_argument('--filesystem', dest='filesystem',
                        help='filesystem for ops that require parameter')
    config_parser.add_argument('--fileset',    dest='fileset',
                        help='fileset for ops that require parameter')
    return parser.parse_args()

def check_args(args):
    # verify that args are valid
    # 1. args.cmd_object in  CMD_OBJECTS
    # 2. git checkout -b profile_name is successfull
    # 3. etc.
    return True

def initialize_repo(args):
   # clone the config tool repo to the args.repo_path
   return True

def main(args):
    print 'Starting with args %s' % args
    check_args(args)
    if hasattr(args, 'repo_action')  and args.repo_action == 'initialize':
        print('Initialize repository at "%s"' % args.repo_path)
	initialize_repo(args)
    elif hasattr(args, 'cmd_action'):
        if args.cmd_action == 'set':
            print('Config set...')
        if args.cmd_action == 'check':
            print('Config check...')
        if args.cmd_action == 'list':
            print('Config list...')

if __name__ == '__main__':
    main(get_args())

