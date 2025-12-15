---
id: 400
title: 'MacOS Tiger had/has some issues'
date: '2005-06-17T12:43:00+00:00'
author: buraglio
layout: post
guid: 'http://new.nickburaglio.com/2005/06/17/macos-tiger-hadhas-some-issues/'
permalink: /2005/06/17/macos-tiger-hadhas-some-issues/
post_views:
    - '265'
categories:
    - 'The firehose'
---

<div></div>MacOS Tiger had/has some issues with the Cisco VPN client. It was a widely public fact. I experienced it first hand. But, being that I have admin access on our VPN concentrator I was able to get the newest clients to \*kinda\* work. There were still a lot of issues with the “compatible client”. Now that Cisco has released the client version 4.6.04 (0061) it’s much better, but sleeping and waking the machine with the client connected yields funkyness, yeah, I know you shouldn’t do that anyway, but some do. I forget to disconnect sometimes myself. The best way I’ve found to get it to work again is to kill the client, reload the kernel extension and restart the client. Some of this requires Command line work and most people don’t really enjoy that (personally I’m quite at home on the CLI). To alleviate this, I wrote some simple applescripts that will help automate the reload of the CiscoVPN kernel extension.

Both are fairly simple, the first one requires that your sudoers file 
be set up to not require a password to execute sudo. It will simply 
kill the vpnclient, reload the kext and restart the vpn client. 
The second one does the same thing but will open terminal.app and 
require you to authenticate. It then delays for 10 seconds (to give 
you time to type your pass) and restarts the vpn client. 
They are available [ here](http://buraglio.com/nick/projects/scripts/applescript/).

<div></div>