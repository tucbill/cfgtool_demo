import json

PROFILE_PATH = '/usr/lpp/mmfs/profiles'
GIT_ROOT = '/Users/billowen/git/config-monkey'
NCMAP_PATH = 'specs/spectrum-scale/mmconfig-profiles/node_class_map.json'


def invert_ncmap(ncmap):
    profile_map = {}
    for d in ncmap['specs']:
        for nc in d['node_classes']:
            profile_map[nc] = d['name']
    profile_map = {nc: d['name'] for d in ncmap['specs'] 
                   for nc in d['node_classes']}
    return profile_map


def main():
    nodeclass = 'fponodes'

    with open('%s/%s' % (GIT_ROOT, NCMAP_PATH), 'r') as f:
        ncmap = json.load(f)

    print ncmap
    # inv_map = {v: k for k, v in ncmap.items()}
    profile_map = invert_ncmap(ncmap)
    profile_name = profile_map[nodeclass]

    with open('%s/%s' % (PROFILE_PATH, profile_name), 'r') as f:
        print f.readline()

if __name__ == '__main__':
    main()
