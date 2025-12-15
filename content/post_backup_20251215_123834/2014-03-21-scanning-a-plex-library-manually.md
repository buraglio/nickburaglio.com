---
id: 637
title: 'Scanning a Plex library manually'
date: '2014-03-21T18:09:48+00:00'
author: buraglio
layout: post
guid: 'http://www.nickburaglio.com/?p=637'
permalink: /2014/03/21/scanning-a-plex-library-manually/
themeblvd_title:
    - 'Manually scan a Plex library from the console'
themeblvd_keywords:
    - 'plex, plex media server, console, terminal, centos, linux, CLI, media server, PMS, scanner, buraglio, nick buraglio'
themeblvd_description:
    - 'Manually scan a Plex library from the console when running plex media server under linux.'
themeblvd_noindex:
    - 'true'
dsq_thread_id:
    - '2478211736'
post_views:
    - '1021'
categories:
    - 'The firehose'
---

I recently had a weird problem with my plex media server in that it would crash upon trying to scan my library. After a great deal of debugging, I finally found what the problem was (a file that was named in such a way that it caused the scanner to crash). [![prom-scan](http://www.nickburaglio.com/wp-content/uploads/2014/03/prom-scan.jpg)](http://www.nickburaglio.com/wp-content/uploads/2014/03/prom-scan.jpg)In order to debug this problem, though, I came across some great under-the-hood tools within plex (which is all python, very cool). After reading [this link](https://plexapp.zendesk.com/hc/en-us/articles/201242707-Plex-Media-Scanner-via-Command-Line), I moved all of my Movies out of the main folder. At that point I moved the files back in, one letter at a time. My Plex server is a [CentOS 6.5](http://www.nickburaglio.com/2014/01/18/why-plex-is-everything-itunes-should-be-and-how-to-install-it-on-centos-6-5/ "Why plex is everything iTunes should be and how to Install it on CentOS 6.5") VM that mounts a [ZFS NAS](http://www.forwardingplane.net/2014/03/replace-zfs-raidz1-disk/).  
I moved the files one starting letter at at time

```
mv -v /path/to/src/A* /path/to/dest/
```

Once that had finished moving I ran the scanner manually using the following command:

```
sudo su - plex -c "export LD_LIBRARY_PATH=/usr/lib/plexmediaserver; \\
/usr/lib/plexmediaserver/Plex\ Media\ Scanner -h"
```

Thankfully, the [plex platform](https://plex.tv/) is really well documented and has a great community around it, so searching for the errors I was seeing led me down the right path to solving the issue. I’m still not sure what caused the file names to become corrupt or unhappy, but I suspect that it had to do with the [disk failure I had in my ZFS raid](http://www.forwardingplane.net/2014/03/replace-zfs-raidz1-disk/).