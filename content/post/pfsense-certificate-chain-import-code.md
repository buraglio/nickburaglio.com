---
title: 'pfSense certificate chain import code'
date: Mon, 11 Aug 2008 12:58:00 +0000
draft: false
tags: [The firehose]
---

I updated some code to make importing certificate chains work under pfSense. It's been a long time coming and the code is probably messy since I'm not a programmer but, for anyone that needs this, it should work.  
  
There are 4 files that need touched:  
captiveportal.inc  
system.inc  
services\_captiveportal.php  
system\_advanced.php  
  
All are contained in the tar file [here](http://www.buraglio.com/nick/projects/scripts/php/pfsense-certchain-working.tgz).  
  
These were all written under 1.2, so using them on other versions may cause unforseen weirdness.  
  
**BACK UP YOUR EXISTING FILES BEFORE USING MINE!**  
  
Please, remember that these are currently unsupported by the pfsense team, feel free to email me and I'll do my best to help but I do have a day job and somewhat of a life, so I'll answer as I get time. Use at your own risk, I'm not a developer so these may not be optimal code, insert other random disclaimer here.  
  
[Post on the pfSense forum](http://forum.pfsense.org/index.php/topic,10888.msg60575.html#msg60575)