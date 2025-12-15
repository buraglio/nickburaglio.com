---
id: 219
title: 'System sending mail on submission port over ssl'
date: '2008-12-28T13:04:00+00:00'
author: buraglio
layout: post
guid: 'http://new.nickburaglio.com/2008/12/28/system-sending-mail-on-submission-port-over-ssl/'
permalink: /2008/12/28/system-sending-mail-on-submission-port-over-ssl/
dsq_thread_id:
    - '2154280496'
post_views:
    - '325'
categories:
    - 'The firehose'
---

I have a few cron jobs that run on my home mac machines and I like to get the notifications generated from the MAILTO parameter. Well, a while ago (I believe after the comcast acquisition of insightbb), this stopped working. I did a little debugging and it is my belief that [port 25 is being blocked outbound from the comcast network](http://www.pdxtc.com/wpblog/technology-articles/cant-send-mail-using-comcast/). [Many people speculate](http://www.google.com/search?q=comcast+blocking+port+25&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-US:official&client=firefox-a)this, and as a network engineer I think it is actually a good idea. First, port 25 isn’t *\***really**\** the port that you should be using for host to mail relay. I was always taught that the [submission port](http://www.faqs.org/rfcs/rfc2476.html) was best practice per [RFC 2476 ](http://www.faqs.org/rfcs/rfc2476.html). In practice, many folks don’t use this port simply because since as far back as I can remember documentation has always pointed end users at port 25. 
So, long story short, something I wanted to do for a long time was to set up a special account under my [google apps](http://www.google.com/apps/intl/en/business/index.html) that can be used to relay and record this data, as well as be used for things like an email wild card for my domain. 
I was about to embark on hacking up the postfix installs then I came across [this macosxhints article](http://www.macosxhints.com/article.php?story=20081217161612647). 
It’s a very handy walk through of doing exactly what I wanted to do, relay mail on port 587, over ssl through my ISP to an externally hosted email account. 
Very handy.