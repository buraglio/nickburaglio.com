---
title: 'In the time that I''ve'
date: Sat, 04 Jun 2005 16:53:00 +0000
draft: false
tags: [The firehose]
---

In the time that I've been (what I would describe as) an IT professional, lets say, >5 years and Why can't I find a filtering system that does everythiung I need and want?  
I love the packet mangling, QoS, traffic shaping, whatever you want to call it today. I can't use an internet cnnection without it. I NEED my ssh connections to be fast and not lagging. I WANT my surfing and email checking to be zippy and snappy. I also may want to cvsup or ftp the newest ISO of FreeBSD at the same time.  
I'd LOVE to have the ability to use PF under FreeBSD with it's beautiful syntax and ease of use. It's like the Lamborghini of filtering. Elegant, powerful, fast. I also want to be able to do things like filter or QoS based on pattern matching or block stuff local to certain interfaces via MAC address. I want to be able to NAT OR bridge and have all the functionality in both function. Maybe it's a pipe dream. I really like some of the abilities of netfilter. Blocking via MAC is great for something like an apartment complex on a college campus as is filtering via pattern matching. Linux has all of these features......but then I'd have to use Linux.....  
Some may say that that may not be a bad thing. I don't necessarily disagree.  
Maybe thats why I feel linux is too clunky compared to the seemingly streamlined sleekness of a BSD. All the cool features weighting it down? Maybe.  
Are there holes in my ideas, of course. The smarter of the users could always clone a MAC. Thats a simple workaround for MAC based filtering, BUT, 90% of users aren't going to know how.  
Pattern matching on packets for filtering, yes, I agree that it \*should\* be done by a proxy. After all, that is what a proxy is supposed to do. But look at the [L7 filter project](http://l7-filter.sourceforge.net/). It works pretty well if one understands [what it can and can't do.](http://l7-filter.sourceforge.net/L7-HOWTO-Netfilter#Intro)  
I fully realize that PF is a layer 3 product.......but so many others have broadened their scope to include useful features like this. Maybe this is why PF is so powerful and clean, I don't know. Could it be that it is because it doesn't try to be everything to everyone? Probably. I can always speculate.  
  
I'd love to see an independent PF based add-on project like the [l7 filter](http://l7-filter.sourceforge.net/). Unfortunately, I'm nowhere near at the programming level to even think about attempting it myself.  
If you know of one, please [email me](mailto:nick+blog@buraglio.com?subject=Regarding%20your%20blog%20post%20on%20L7%20PF%20and%20MAC%20filtering).  
  
I know, I can want in one hand and take a dump in the other and see which one fills up first..