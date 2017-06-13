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
# Starter script to demonstrate configuration automation in Spectrum Scale
# cluster environment

import argparse
import sys
import time

CFGMONKEY_VERSION = '1.0'

CONFIG_ACTIONS = ['set', 'show', 'check']
CONFIG_SETTINGS = ['scale', 'sysctl', 'device', 'all']

REPO_ACTIONS = ['initialize', 'archive']
REPO_PATH_DEFAULT = '/usr/lpp/mmfs/samples/config-monkey'
REPO_ARCHIVE_PATH_DEFAULT = '/tmp/config-monkey-archive.bundle'
REPO_URL = 'https://github.com/tucbill/config-monkey'

VERSION_ACTIONS = ['list', 'create', 'diff', 'update', 'delete']


def get_args():
    parser = argparse.ArgumentParser(
        description=(
            'Example config monkey tools (version %s).' %
            CFGMONKEY_VERSION))
    subparsers = parser.add_subparsers(help='commands')

    repo_parser = subparsers.add_parser(
        'repo',
        help='Repository management actions.')
    repo_parser.add_argument(
        'repo_action', help='Management actions on the repository, valid '
        'options are "initialize": initialize the local repository from the '
        'remote repository using "git clone" command; "archive": create an '
        'archive of the local repository for backup using "git bundle" '
        'command.')
    repo_parser.add_argument(
        '--repo-path',
        help='Path to git repository where configuration definitions are '
        'stored.  The default value is %s.' % REPO_PATH_DEFAULT,
        default=REPO_PATH_DEFAULT)
    repo_parser.add_argument(
        '--archive-file',
        help='Path to archive file that is created using "git bundle" '
        'command.  The default value is %s.' % REPO_ARCHIVE_PATH_DEFAULT,
        default=REPO_ARCHIVE_PATH_DEFAULT)

    config_parser = subparsers.add_parser(
        'config',
        help='Configuration management actions.')
    config_parser.add_argument(
        'config_action',
        help='Configuration action, valid options are %s' %
        CONFIG_ACTIONS)
    config_parser.add_argument(
        '--spec',
        help='Version of the configuration specifications to be used.  '
        'The version name maps to a git branch containing all of '
        'the specification files and artifacts.  Configuration versions are '
        'typically used to organize settings by storage type, for example '
        'ESS, FPO, Mestor, etc.')
    config_parser.add_argument(
        '--repo-path',
        help='Path to local git repository where configuration definitions '
        'are stored.  The default value is %s' % REPO_PATH_DEFAULT,
        default=REPO_PATH_DEFAULT)
    config_parser.add_argument(
        '--settings',
        help='Specify which settings to apply, valid options are %s.  Pass a '
        'comma separated list to specify more than one setting, for example '
        '"scale,device".  The default value is "all".' % CONFIG_SETTINGS,
        default='all')
    config_parser.add_argument(
        '--node-class',
        required=True,
        help='The node class specifying the set of nodes to configure, check '
        'or show.')

    version_parser = subparsers.add_parser(
        'version',
        help='Version management actions.')
    version_parser.add_argument(
        'version_action',
        help='Version management action, valid options are %s.  For "list" '
        'list the configuration sets defined in the local repository.' %
        VERSION_ACTIONS)
    version_parser.add_argument(
        '--repo-path',
        help='Path to local git repository where configuration definitions '
        'are stored.  The default value is %s' % REPO_PATH_DEFAULT,
        default=REPO_PATH_DEFAULT)
    version_parser.add_argument(
        '--spec',
        help='Version name of the configuration specifications to be used.  '
        'The version name maps to a git branch containing all of '
        'the specification files and artifacts.  Configuration versions are '
        'typically used to organize settings by storage type, for example '
        'ESS, FPO, Mestor, etc.')
    version_parser.add_argument(
        '--spec2',
        help='The version name to compare against in difference operations')
    version_parser.add_argument(
        '--current_version',
        help='Compare the specified repository version against current '
        'settings on the specified nodes')
    version_parser.add_argument(
        '--node-class',
        help='The node class specifying the set of nodes to use for diff '
        'operation.')
    version_parser.add_argument(
        '--comment',
        help='The commit comment used to document version updates')

    return parser.parse_args()


def args_check(args):
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
    # config show
    # - repo-path should not be passed as an argument
    # - spec should not be passed as an argument
    # - settings is a valid subset of CONFIG_SETTINGS
    # - node-class is a valid Spectrum Scale node class
    # config check
    # - repo-path is a valid repository
    # - spec is a valid branch name in the repository
    # - settings is a valid subset of CONFIG_SETTINGS
    # - node-class is a valid Spectrum Scale node class
    # config set
    # - repo-path is a valid repository
    # - spec is a valid branch name in the repository
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


def repo_initialize(args):
    # clone the config tool repo to the args.repo_path
    print('Repository initialized at "%s"' % args.repo_path)
    return True


def repo_archive(args):
    print('Archive repository complete.  Created %s' %
          args.archive_file)
    return True


def version_list(args):
    print('Available specifications in local repository: fpo, ess')


def config_set(args):
    print('Set configuration using specification set "%s", for settings "%s" '
          'on node class "%s"' % (args.spec, args.settings, args.node_class))


def config_check(args):
    pass


def main(args):
    print 'Starting at %s' % time.asctime()
    if not args_check(args):
        print 'Exiting because of invalid arguments at %s' % time.asctime()
    if hasattr(args, 'repo_action'):
        if args.repo_action == 'initialize':
            repo_initialize(args)
        elif args.repo_action == 'archive':
            repo_archive(args)
    elif hasattr(args, 'config_action'):
        if args.config_action == 'set':
            config_set(args)
        if args.config_action == 'check':
            print('Config check...')
        if args.config_action == 'show':
            print('Config show...')
    elif hassattr(agrs, 'version_action'):
        if args.version_action == 'list':
            version_list(args)

if __name__ == '__main__':
    main(get_args())
