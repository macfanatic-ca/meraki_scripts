#!/usr/bin/python

import sys

hexlist = []
for domain in sys.argv[1:]:
    for part in domain.split("."):
        hexlist.append("%02x" % len(part))
        for c in part:
            hexlist.append(c.encode("hex"))
    hexlist.append("00")

print "".join([(":%s" % (x) if i and not i % 1 else x) \
               for i, x in enumerate(hexlist)])
