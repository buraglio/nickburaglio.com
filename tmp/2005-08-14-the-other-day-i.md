---
title: The other day I
author: buraglio
type: post
date: 2005-08-14T12:18:00+00:00
url: /2005/08/14/the-other-day-i/
blogger_blog:
  - www.nickburaglio.com
blogger_author:
  - Nick Buraglio
blogger_permalink:
  - /2005/08/other-day-i.html
dsq_thread_id:
  - 4046551027
categories:
  - The firehose

---
<div>
</div>

The other day I came across [pfsense][1] while looking for stuff I could use on my openbsd based version of basically the same thing. I was intrigued by this because it was using altq as well as pf, which was the main reason that I was working on a similar product under openbsd. Upon actually installing it on a Soekris I was even more impressed. I installed it on a [NET4801][2] with a wireless and crypto card and have been using it as my internet gateway for a few days. I am VERY impressed by the ease of use. The GUI looks to be mostly based on the [M0n0wall][3] but there are some major differences. There are wizards that help those that don&#8217;t know about traffic shaping set up some hfsc based QoS. There are many other &#8220;under the hood&#8221; enhancements like the fact that it&#8217;s based on FreeBSD 6-BETA2 (at the time of this writing) and not FreeBSD 4.10 (or maybe 4.11) like the M0n0wall. Most importantly for me, it uses pf + altq (from the OpenBSD project) which in my opinion is more robust and useful than iptables, ipfw(2) or even ipf. I&#8217;m hoping to either help out a bit with this project, take the gui and xml (and php) based stuff and port it to openbsd, or both. There are many, many more improvements, enhancements and features beyond the scope of this writing and this is a VERY useful project, please check it out and support them.

<div>
</div>

 [1]: http://www.pfsense.org/
 [2]: http://www.soekris.com/
 [3]: http://m0n0.ch/wall