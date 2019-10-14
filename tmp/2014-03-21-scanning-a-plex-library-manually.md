---
title: Scanning a Plex library manually
author: buraglio
type: post
date: 2014-03-22T00:09:48+00:00
url: /2014/03/21/scanning-a-plex-library-manually/
themeblvd_title:
  - Manually scan a Plex library from the console
themeblvd_keywords:
  - plex, plex media server, console, terminal, centos, linux, CLI, media server, PMS, scanner, buraglio, nick buraglio
themeblvd_description:
  - Manually scan a Plex library from the console when running plex media server under linux.
themeblvd_noindex:
  - 'true'
dsq_thread_id:
  - 2478211736
categories:
  - The firehose

---
I recently had a weird problem with my plex media server in that it would crash upon trying to scan my library.  After a great deal of debugging, I finally found what the problem was (a file that was named in such a way that it caused the scanner to crash).  [<img class="alignright size-full wp-image-640" alt="prom-scan" src="http://www.nickburaglio.com/wp-content/uploads/2014/03/prom-scan.jpg" width="450" height="270" />][1]In order to debug this problem, though, I came across some great under-the-hood tools within plex (which is all python, very cool).  After reading <a href="https://plexapp.zendesk.com/hc/en-us/articles/201242707-Plex-Media-Scanner-via-Command-Line" target="_blank">this link</a>, I moved all of my Movies out of the main folder.  At that point I moved the files back in, one letter at a time. My Plex server is a <a title="Why plex is everything iTunes should be and how to Install it on CentOS 6.5" href="http://www.nickburaglio.com/2014/01/18/why-plex-is-everything-itunes-should-be-and-how-to-install-it-on-centos-6-5/" target="_blank">CentOS 6.5</a> VM that mounts a <a href="http://www.forwardingplane.net/2014/03/replace-zfs-raidz1-disk/" target="_blank">ZFS NAS</a>.
  
I moved the files one starting letter at at time

<pre>mv -v /path/to/src/A* /path/to/dest/</pre>

Once that had finished moving I ran the scanner manually using the following command:

<pre>sudo su - plex -c "export LD_LIBRARY_PATH=/usr/lib/plexmediaserver; \\
/usr/lib/plexmediaserver/Plex\ Media\ Scanner -h"</pre>

Thankfully, the <a href="https://plex.tv/" target="_blank">plex platform</a> is really well documented and has a great community around it, so searching for the errors I was seeing led me down the right path to solving the issue.  I&#8217;m still not sure what caused the file names to become corrupt or unhappy, but I suspect that it had to do with the <a href="http://www.forwardingplane.net/2014/03/replace-zfs-raidz1-disk/" target="_blank">disk failure I had in my ZFS raid</a>.

 [1]: http://www.nickburaglio.com/wp-content/uploads/2014/03/prom-scan.jpg