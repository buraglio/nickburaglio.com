---
title: 'Wow. The 650 is much'
date: Fri, 30 Dec 2005 10:02:00 +0000
draft: false
tags: [The firehose]
---

Wow. The 650 is much different than the 600. I opted to get a 650 as opposed to waiting for the 700w (Palms first PocketPC based device), I generally never get something I need to rely heavily on that is a first release, or the 700p (palm based, supposedly exclusive to SprintPCS for 6 months after release).  
  
I have had to re-learn a lot of the subtleties of the treo platform. Below is a list of some of the problems I ran into:  
  
1\. My Treo would not sync with my powerbook using the default palm conduits. This was a huge problem for me as I normally use my treo as the master and just do a sync to back it up. I purchased [The Missing Sync](http://markspace.com/missingsync_palmos.php) to try and rectify this problem. I was planning on getting anyway so I could use the cool SD Card mounting feature.  
  
2\. I had many issues using the missing sync initially. Most of this stemmed from me not reading all of the caveats involved. The one that confounded me the longest was the "handheld overwrites device" issue addressed [here](http://www.markspace.com/support/index.php?x=&mod_id=2&id=2571).  
  
3\. My calendars and address book are extremely important to me. I have them in many places so I do not lose them. It was not clear to me just how unorganized they actually were. I had to do some substantial cleaning to get them to look nice again and I am still weeding out double entries in my calendar. This is deeply rooted, probably from me moving around from calendar program to calendar program such as Palm desktop, iCal, sunbird, etc. It is my opinion that there is no good calendar program out there. Some just suck less or in different ways. iCal would probably be my choice as "sucks least" but it's lack of support for publishing to (or is it subscribing to?) SSL webdav servers is just plain sad. There is no good technical excuse that I can think of for not having this capability.  
  
4\. Secure imap support in a "free or cheap" mail client. I used to use chattermail but it would crash my 600. I really liked the way it looked and that it could use the SD card for mail storage. I never purchased it, instead opting to use the demo version then removing it when it locked up my 600. I tried to install it on the SD card since my palm is pretty full with apps, having only a few Meg free. It complained that it needed something installed on the device (I'm assuming it wanted it installed in RAM). I tried to use FileZ to move it and it's components to the internal space and that sent my 650 into a reboot loop. A reboot loop is a nightmare. I eventually got it out of the loop after trying a soft reset and a warm reset. After the warm reset it booted but any time it tried to read from the internal memory it went right back to the reboot loop. I had to do a hard reset to fix the issue. A pain to say the least but a known fix for palm app problems. I found [this article](http://kb.palmone.com/SRVS/CGI-BIN/WEBCGI.EXE?New,Kb=PalmSupportKB,ts=Palm_External2001,Case=obj(887)) useful on this process.  
Back to secure imap. I eventually realized that Versamail, which came with my Verizon Treo 650, had SSL support. I have it installed and working, although it seems more limited than Chattermail. I also cannot seem to get sSMTP working with authentication to my postfix server. I get SSL errors on the postfix box. Still investigating. I also have yet to figure out if Versamail can store mail on the SD card, my belief is that it can not.  
  
5\. Backup solutions. I knew there were many. I wanted a good one that was free. I found 2 that I like a lot so far. [BackupMan](http://www.bitsnbolts.com/backupman.php) is really nice. It's $10 but will work for manual backups without paying. I suggest paying the $10 if for no other reason than to support the author. It will not do automated backups if run from the SD card. [VfsBackup](http://www.planepla.net/vfsbackup.html), not to be confused with [VFSBackup](http://homepage.ntlworld.com/james.screech/VFSBackup.htm), which I have not used but looks curiously similar to BackupMan. These will backup your device to a nice nifty archive on an expansion card. A priceless tool if you rely on your PDA as much as I do.  
  
I am still waiting on my accessories, our shipping and receiving dept is shut down for the holidays. I am assuming I''ll get them Tuesday (01/03/2006).  
  
More to come...