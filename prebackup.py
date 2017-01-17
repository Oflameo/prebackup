#!/usr/bin/python
#Copyright (C) 2017 Johnathan Lewis <me@johnathan-lewis.com>

import os
mtab = '/etc/mtab'
tracked_mountpoints = ['/mnt/backups, /mnt/forwardups']
mtab_mountpoints = []
backupcmd = "echo 'backup happening'"

with open(mtab) as infile:
    for line in infile:
        tl = line.split()
        if len(tl) > 1:
            mtab_mountpoints.append(tl[1])

if set(tracked_mountpoints) <= set(mtab_mountpoints):
    os.system(backupcmd)
else:
    print 'Your backup has failed! One of following mountpoints isn\'t mounted.'
    print tracked_mountpoints
