---
title: I’m a mac user, I
author: buraglio
type: post
date: 2006-01-12T22:32:00+00:00
url: /2006/01/12/im-a-mac-user-i/
blogger_blog:
  - www.nickburaglio.com
blogger_author:
  - Nick Buraglio
blogger_permalink:
  - /2006/01/i-mac-user-i.html
categories:
  - The firehose

---
<div>
</div>

I&#8217;m a mac user, I have been for years. I have a (although somewhat outdated) knowledge of hardware and I&#8217;d like to think I know my way around a Unix system. So when I had a problem with my 20gig ipod I figured if it wasn&#8217;t hardware I could fix it. Well, it was hardware. My wife got it for me in Feb. of 2004 for my birthday. She got it at best buy, and knowing how I am rough on stuff, she bought the extended warranty from them, giving it coverage till 2/2008. OK, they sent it off and supposedly replaced the drive. Great. I pick it up and take it home. What a big surprise, it&#8217;s formatted as a windows ipod. No problem, it should still work. No dice.  
Lovely messages in the logs:  
**  
Error with partition Bad file descriptor  
Erase complete.</p> 

Jan 12 07:43:57 Mackie diskarbitrationd[37]: unable to mount /dev/disk1s2 (status code 0x00000047).  
2006-01-12 07:44:24.161 iPod Updater Extreme[500] Can&#8217;t read checkpoint data  
2006-01-12 07:44:31.198 iPod Updater Extreme[500] Can&#8217;t read checkpoint data  
2006-01-12 07:44:34.811 iPod Updater Extreme[500] Can&#8217;t read checkpoint data  
2006-01-12 07:44:38.326 iPod Updater Extreme[500] Can&#8217;t read checkpoint data  
2006-01-12 07:44:41.870 iPod Updater Extreme[500] Can&#8217;t read checkpoint data  
2006-01-12 07:44:45.443 iPod Updater Extreme[500] Can&#8217;t read checkpoint data  
</b>

I can&#8217;t find much on these errors while googling around. Damnit. What a pain. It is also making a terrible clicky clack while plugged in. I drag the old XP machine out of the closet and plug it into the PCI firewire card. explorer.exe crashes. OK, I can accept that. This machine is terribly unmaintained. I take it into work and my boss plugs it into his firewire port on his laptop. Same behavior. ::sigh:: I have to take it \*back\* to best buy. Work and training end and I head off to Best buy.

The Geek Squad guy was nice, not terribly personable (although I wasn&#8217;t either when I did that kind of PC repair work). He plugged it into a windows PC using a USB cable and it worked flawlessly. WTF?!? OK. I had my powerbook there. I plugged it into my powerbook with his USB cable and it worked. DAMN! OK, I want to restore it as a Mac formatted disk so if needed I can boot from it. No deal, it needs a firewire cable to do so. I plug it into the PB with a FW cable and it fails miserably. By this point I am super frustrated. Maybe it&#8217;s the firewire Dock cable. They say it&#8217;s not broken and 5 minutes of me arguing that I can&#8217;t use it because I

A. **DON&#8217;T have a USB cable**

and

B. **DON&#8217;T Want it formatted FAT32**

ensues. As far as I&#8217;m concerned if I can&#8217;t **use** it it&#8217;s worthless to me. It&#8217;s an apple product, I should be able to use it as I have for 2 years without issue.

He was not really sympathetic, he&#8217;s not a mac user and doesn&#8217;t really seem to understand that all I want is for it to be **THE SAME** as when it was shipped off. Finally after talking to a manager he agrees to send it back with the firewire cable and have it formatted HFS+ and test the cable. OK, another few weeks without it. We&#8217;ll see if it works when it comes back. Theoretically, if it gets sent off one more time I should get it replaced with a new one. We&#8217;ll see, I&#8217;d be willing to bet they fight that tooth and nail.

<div>
</div>