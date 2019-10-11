---
title: In the time that I’ve
author: buraglio
type: post
date: 2005-06-04T16:53:00+00:00
url: /2005/06/04/in-the-time-that-ive/
blogger_blog:
  - www.nickburaglio.com
blogger_author:
  - Nick Buraglio
blogger_permalink:
  - /2005/06/in-time-that-i.html
categories:
  - The firehose

---
<div>
</div>

In the time that I&#8217;ve been (what I would describe as) an IT professional, lets say, >5 years and Why can&#8217;t I find a filtering system that does everythiung I need and want?  
I love the packet mangling, QoS, traffic shaping, whatever you want to call it today. I can&#8217;t use an internet cnnection without it. I NEED my ssh connections to be fast and not lagging. I WANT my surfing and email checking to be zippy and snappy. I also may want to cvsup or ftp the newest ISO of FreeBSD at the same time.  
I&#8217;d LOVE to have the ability to use PF under FreeBSD with it&#8217;s beautiful syntax and ease of use. It&#8217;s like the Lamborghini of filtering. Elegant, powerful, fast. I also want to be able to do things like filter or QoS based on pattern matching or block stuff local to certain interfaces via MAC address. I want to be able to NAT OR bridge and have all the functionality in both function. Maybe it&#8217;s a pipe dream. I really like some of the abilities of netfilter. Blocking via MAC is great for something like an apartment complex on a college campus as is filtering via pattern matching. Linux has all of these features&#8230;&#8230;but then I&#8217;d have to use Linux&#8230;..  
Some may say that that may not be a bad thing. I don&#8217;t necessarily disagree.  
Maybe thats why I feel linux is too clunky compared to the seemingly streamlined sleekness of a BSD. All the cool features weighting it down? Maybe.  
Are there holes in my ideas, of course. The smarter of the users could always clone a MAC. Thats a simple workaround for MAC based filtering, BUT, 90% of users aren&#8217;t going to know how.  
Pattern matching on packets for filtering, yes, I agree that it \*should\* be done by a proxy. After all, that is what a proxy is supposed to do. But look at the  [L7 filter project][1]. It works pretty well if one understands [what it can and can&#8217;t do.][2]   
I fully realize that PF is a layer 3 product&#8230;&#8230;.but so many others have broadened their scope to include useful features like this. Maybe this is why PF is so powerful and clean, I don&#8217;t know. Could it be that it is because it doesn&#8217;t try to be everything to everyone? Probably. I can always speculate.

I&#8217;d love to see an independent PF based add-on project like the [l7 filter][1]. Unfortunately, I&#8217;m nowhere near at the programming level to even think about attempting it myself.  
If you know of one, please [email me][3].

I know, I can want in one hand and take a dump in the other and see which one fills up first..

<div>
</div>

 [1]: http://l7-filter.sourceforge.net/
 [2]: http://l7-filter.sourceforge.net/L7-HOWTO-Netfilter#Intro
 [3]: mailto:nick+blog@buraglio.com?subject=Regarding%20your%20blog%20post%20on%20L7%20PF%20and%20MAC%20filtering