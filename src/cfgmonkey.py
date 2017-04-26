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
import time

VERSION = '1.0'
REPO_ACTIONS = ['initialize', 'archive']
CONFIG_ACTIONS = ['set', 'list', 'check']
CONFIG_SETTINGS = ['scale', 'sysctl', 'device', 'all'] 
REPO_PATH_DEFAULT='/usr/lpp/mmfs/samples/config-monkey'
REPO_ARCHIVE_PATH_DEFAULT='/tmp/config-monkey-archive.bundle'
REPO_URL='https://github.com/tucbill/config-monkey'

def get_args():
    parser = argparse.ArgumentParser(description=('Example config monkey tools (version %s)' % VERSION))
    subparsers = parser.add_subparsers(help='commands')
  
    repo_parser = subparsers.add_parser('repo', help='repository management actions',
                                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    repo_parser.add_argument('repo_action',
                             help='Management actions on the repository, valid options are ' 
                             'initialize: initialize the local repository from remote using "git clone", \n'
                             'archive: create an archive of the repository for backup using "git bundle"')
    repo_parser.add_argument('--repo-path', 
                             help='Path to git repository where configuration definitions are stored',
			     default=REPO_PATH_DEFAULT)
    repo_parser.add_argument('--archive-file', 
			     help='Path to archive file that is created using "git bundle" command',
                             default=REPO_ARCHIVE_PATH_DEFAULT)

    config_parser = subparsers.add_parser('config', help='configuration actions',
                                          formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    config_parser.add_argument('config_action',
                               help='Configuration action, valid options are %s' % CONFIG_ACTIONS)
    config_parser.add_argument('--profile', required=True,
                               help='Name of profile containing configuration specifications. '
                               'The profile maps to a git branch containing all of the specification files '
                               'and artifacts.')
    config_parser.add_argument('--repo-path', 
                               help='Path to git repository where configuration definitions are stored',
			       default=REPO_PATH_DEFAULT)
    config_parser.add_argument('--settings', 
                               help='Specify which settings to apply, valid options are %s.  Pass a comma '
                               'separated list to specify more than one setting, for example "scale,device"' %
			       CONFIG_SETTINGS,
                               default='all')
    config_parser.add_argument('--node-class', required=True,
                               help='The node class specifying the set of nodes to configure, check or list')
    return parser.parse_args()

def check_args(args):
    # if repo_action exists:
    # - verify repo_action in REPO_ACTIONS
    # repo initialize
    # - does repo-path parent exist and is it writeable?
    # - archive-file should not be passed as an argument
    # repo archive
    # - does repo-path parent exist and is it writeable?
    # - does archive-file path exist and is it writeable?
    # if config-action exists:
    # - verify config-action in CONFIG_ACTIONS
    # config list
    # - repo-path should not be passed as an argument
    # - profile should not be passed as an argument
    # - settings is a valid subset of CONFIG_SETTINGS
    # - node-class is a valid Spectrum Scale node class
    # config check
    # - repo-path is a valid repository
    # - profile is a valid branch name in the repository
    # - settings is a valid subset of CONFIG_SETTINGS
    # - node-class is a valid Spectrum Scale node class
    # config set
    # - repo-path is a valid repository
    # - profile is a valid branch name in the repository
    # - settings is a valid subset of CONFIG_SETTINGS
    # - node-class is a valid Spectrum Scale node class
    if hasattr(args, 'repo_action'):
        if args.repo_action not in REPO_ACTIONS:
            print('Invalid repository action requested: "%s" not in %s' %
	         (args.repo_action, REPO_ACTIONS))
            return False
    elif hasattr(args, 'config_action'):
        if args.config_action not in CONFIG_ACTIONS:
            print('Invalid config action requested: "%s" not in %s' %
                 (args.config_action, CONFIG_ACTIONS))
            return False
    return True

def initialize_repo(args):
   # clone the config tool repo to the args.repo_path
   return True

def main(args):
    print 'Starting at %s' % time.asctime()
    if not check_args(args):
       print 'Exiting because of invalid arguments at %s' % time.asctime()
    if hasattr(args, 'repo_action')  and args.repo_action == 'initialize':
        print('Initialize repository at "%s"' % args.repo_path)
	initialize_repo(args)
    elif hasattr(args, 'config_action'):
        if args.config_action == 'set':
            print('Config set...')
        if args.config_action == 'check':
            print('Config check...')
        if args.config_action == 'list':
            print('Config list...')

if __name__ == '__main__':
    main(get_args())

