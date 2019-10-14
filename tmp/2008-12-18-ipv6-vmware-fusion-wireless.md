---
title: IPv6, Vmware Fusion, Wireless
author: buraglio
type: post
date: 2008-12-18T00:12:00+00:00
url: /2008/12/18/ipv6-vmware-fusion-wireless/
blogger_blog:
  - www.nickburaglio.com
blogger_author:
  - Nick Buraglio
blogger_permalink:
  - /2008/12/ipv6-vmware-fusion-wireless.html
dsq_thread_id:
  - 2320633598
categories:
  - The firehose

---
I&#8217;ve been revisiting IPv6 a lot again lately, and one thing I wanted to do was to get my home network back running IPv6 again after having it off for a while. IPv6 isn&#8217;t that hard to understand, configure, route or use, it&#8217;s just different and I need to know it well for my job so this is a good excuse to play around and re-read some of the books I bought years ago on the subject.   
Since my lovely provider, Comcast, has no plan to deploy v6 yet I turned to one of the several [IPv6 Tunnel Brokers][1]. I had used the [Hurricane Electric Tunnel Broker][2] service a lot when first pawing at v6 years ago, and my tunnel info was still there.   
OK, Tunnel up. Reverse DNS delegated and working. Router Advertisements flying all over the network and [modified EUI-64][3] addresses all looking good.   
`<br /># ifconfig                                                                                           <br />lo0: flags=8049<up> mtu 33208<br />        groups: lo<br />        inet 127.0.0.1 netmask 0xff000000<br />        inet6 ::1 prefixlen 128<br />        inet6 fe80::1%lo0 prefixlen 64 scopeid 0x5<br />vic0: flags=8843</up><up> mtu 1500<br />        lladdr 00:0c:29:38:49:eb<br />        groups: egress<br />        media: Ethernet autoselect<br />        status: active<br />        inet6 fe80::20c:29ff:fe38:49eb%vic0 prefixlen 64 scopeid 0x1<br />        inet6 2001:470:1f07:447:20c:29ff:fe38:49eb prefixlen 64 pltime 604786 vltime 2591986<br />        inet 192.168.209.11 netmask 0xffffffc0 broadcast 192.168.209.63<br /></up>`

**inet6 2001:470:1f07:447:20c:29ff:fe38:49eb prefixlen 64 pltime 604786 vltime 2591986** being the important string in there.

&#8230;..Flash back like 12 months. In an effort to be a little more conscious of money as well as environment, and out of good old fashioned cheapness, I took down my nice rack of servers, powered them all off, saved up my pennies and got a really nice [24&#8243; iMac][4], packed to the hilt with RAM and disk with the idea of using one of my copies of [vmware fusion][5] to run my [FreeBSD][6], [OpenBSD][7] and [pfSense][8] stuff on. 

OK, time for the fun&#8230;..geting some v6 stuff to work through my network, over wireless, using vmware fusion with the gust OS in bridge mode&#8230;.uuuumm, nope.   
Hmmmm, why could this be? It&#8217;s just a network interface, right? Wrong. After troubleshooting this for a while and seeing nothing in packet dumps from anything outside of the box I decided to hit up my the smartest place I know to look, [Google][9] (yes, I used [http://ipv6.google.com][10]).  
Low and behold, I found [this post][11].

Apparently wireless interfaces are a problem, and as so tersely stated more than once in that thread &#8220;VMware policy is to not comment on unannounced products, features, or timelines&#8221;.  
Crud. Well, I&#8217;m running vmware fusion 1.1.4 still&#8230;.maybe I&#8217;ll see if it&#8217;s supported in 2.0, but not tonight. That would make life too easy so I&#8217;m not counting on it. 

[ad]

 [1]: http://www.google.com/url?sa=t&source=web&ct=res&cd=1&url=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FList_of_IPv6_tunnel_brokers&ei=ZuNJScryGpzaMPvBpewE&usg=AFQjCNFs8wXSQavbjyi6SKBC-LsOuqJs9g&sig2=slUWlxyTaEd7m1GDmDMjKg
 [2]: http://www.tunnelbroker.com/
 [3]: http://www.tcpipguide.com/free/t_IPv6InterfaceIdentifiersandPhysicalAddressMapping-2.htm
 [4]: http://www.apple.com/imac/specs/
 [5]: http://vmware.com/products/fusion/
 [6]: http://www.freebsd.org/
 [7]: http://www.openbsd.org/
 [8]: http://www.pfsense.org/
 [9]: http://www.google.com/
 [10]: http://ipv6.google.com/
 [11]: http://communities.vmware.com/thread/139716