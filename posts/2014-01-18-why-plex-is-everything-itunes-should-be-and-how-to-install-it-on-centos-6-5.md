---
title: Why plex is everything iTunes should be and how to Install it on CentOS 6.5
author: buraglio
type: post
date: 2014-01-18T16:55:48+00:00
url: /2014/01/18/why-plex-is-everything-itunes-should-be-and-how-to-install-it-on-centos-6-5/
themeblvd_title:
  - Why plex is everythign iTunes should be and how to Install Plex Media Server on CentOS 6.5
themeblvd_keywords:
  - plex, movies, centos, myplex, film, itunes, media, iphone, ipad, android, watch movies
themeblvd_description:
  - 'Why you will love Plex and how to Install Plex Media Server on CentOS 6.5. Plex is everything iTunes should be. '
themeblvd_noindex:
  - 'true'
dsq_thread_id:
  - 2156144363
categories:
  - The firehose

---
If you&#8217;re not familiar with <a href="https://plex.tv/" target="_blank">Plex</a>, you should be. It&#8217;s one of the most flexible, well supported, useful pieces of entertainment software ever written. Oh, and it&#8217;s open source. That&#8217;s right, it&#8217;s free. And it&#8217;s cross platform. And it will run on just about any device. It&#8217;s quite amazing, actually. Plex also supports a myriad of <a href="https://plex.tv/features" target="_blank">plugins  and features</a> such as Channels, DLNA and cloud sync as well as the notion of clipping existing videos such as youtube content for display on your television or other devices. This alone makes the package worth setting up. However, it also does some really amazing indexing of your media if it is named correctly.  As an example, I love horror movies, so naturally I have quite a few of them on DVD. Some of them are obscure. With Plex, this is not an issue as long as the movie exists in IMDB (or a few other sources for more obscure or foreign films).  If it does it will pull down all of the metadata on it and display it. Very, very slick:

<p style="text-align: center;">
  <a href="http://www.nickburaglio.com/wp-content/uploads/2014/01/Screen-Shot-2014-01-18-at-9.29.35-AM.png"><img class="aligncenter  wp-image-616" alt="Plex Cemetery Man Image" src="http://www.nickburaglio.com/wp-content/uploads/2014/01/Screen-Shot-2014-01-18-at-9.29.35-AM-1024x398.png" width="553" height="215" /></a>
</p>

<p style="text-align: center;">
  <p>
    Obviously plex is a very versatile application. It has two parts, the client and the server. Personally I have not used the client since the inception of myplex, I pretty much just use a web interface, with the exception of my ipad and iphone, which have a dedicated client. You can also share your plex using myplex, and if you have a plexpass, watched status can be localized to each user. For example, if you share your library with a family member that may no longer be living in your household (say, a college student) when they watch a film it will not show as watched under your particular plex instance unless you have watched it* but will for theirs. This is a nice feature if you&#8217;re watching TV series or other multi-part shows.  It also allows for media sync when you cannot stream your media.
  </p>
  
  <p>
    Plex is all of the things that iTunes should be.
  </p>
  
  <p>
    <span style="line-height: 1.5em;">As a breif bit of history, a few years ago I decided that it would be a good idea to digitize my fairly good sized DVD collection like I had done with CDs, records and cassettes for music years before. I had enough disk to hold it and wanted to clear space on some bookshelves.  I bought some rubbermaid tubs and after a long process and some intimate time with </span><a style="line-height: 1.5em;" href="http://handbrake.fr/" target="_blank">Handbrake</a><span style="line-height: 1.5em;">, I put all of my DVDs in my storage closet in my basement.  Once that digital library was all set up, and since most Blu-Ray combo packs come with a digital copy, I can unquestionably say that this was a good idea.  It&#8217;s funny, too, since I get a Blu-Ray combo pack, sock away the media and jam a digital copy on my NAS with the other media .</span>
  </p>
  
  <p>
    Now, on with the install. I went with CentOS because it&#8217;s easy to administrate for me.  I don&#8217;t really know windows well enough to comfortably admin a box anymore and I don&#8217;t want to spend the extra money on a mac just to run plex. I like to run things on minimalist systems if I can, and Linux is easy enough to tune down to a very small footprint. My plex media server actually runs really well as a VM. Lets assume that you have an already built CentOS 6.5 box. I chose minimalist install but this will work for any install option.
  </p>
  
  <pre>yum -y install wget
wget http://downloads.plexapp.com/plex-media-server/0.9.8.18.290-11b7fdd \ 
/plexmediaserver-0.9.8.18.290-11b7fdd.x86_64.rpm
rpm -ivh plexmediaserver-0.9.8.18.290-11b7fdd.x86_64.rpm 
yum -y update</pre>
  
  <p>
    You should see something like this:
  </p>
  
  <pre>[root@plex buraglio]# yum update
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: centos.sonn.com
 * epel: fedora-epel.mirror.iweb.com
 * extras: centos.sonn.com
 * rpmforge: apt.sw.be
 * updates: centos.sonn.com
PlexRepo                                                 |  951 B     00:00
PlexRepo/primary                                         | 5.4 kB     00:00
PlexRepo                                                              12/12
Setting up Update Process
No Packages marked for Update</pre>
  
  <p>
    Now start Plex Media Server and tell it to start at boot:
  </p>
  
  <pre>service plexmediaserver start
chkconfig plexmediaserver on</pre>
  
  <p>
    Since mine runs internally, I disable iptables all together:
  </p>
  
  <pre>service iptables stop
service ip6tables stop
chkconfig iptables off
chkconfig ip6tables off</pre>
  
  <p>
    You can probably also add a rule to allow access [untested by me]
  </p>
  
  <p>
    Add IPTables rules:
  </p>
  
  <pre>sudo iptables -I INPUT -p tcp -m state --state NEW -m tcp --dport 32400 -j ACCEPT
sudo ip6tables -I INPUT -p tcp -m state --state NEW -m tcp --dport 32400 -j ACCEPT  
service iptables save
service ip6tables save</pre>
  
  <p>
    Although plex does not listen on IPv6, I have it enabled on my network so I’m going to add a rule for it for future use.
  </p>
  
  <p>
    Install and enable Avahi for local discovery
  </p>
  
  <pre>yum -y install avahi
service avahi-daemon start
chkconfig  avahi-daemon on</pre>
  
  <p>
    Now you just need to add your media via the web interface. Point your browser at the plex box: http://plex:32400/web/index.html
  </p>
  
  <p>
    <a href="http://www.nickburaglio.com/wp-content/uploads/2014/01/Screen-Shot-2014-01-18-at-10.32.12-AM.png"><img class="aligncenter size-medium wp-image-618" alt="Screen Shot 2014-01-18 at 10.32.12 AM" src="http://www.nickburaglio.com/wp-content/uploads/2014/01/Screen-Shot-2014-01-18-at-10.32.12-AM-300x250.png" width="300" height="250" /></a>
  </p>
  
  <p>
    After a bit plex will scrape all of the metadata from it&#8217;s sources and you should see a nice display of media detail. This works for Music, TV shows and Movies. It will also happily display photos and home movies. I have mine pointed at my iTunes library and my iPhoto library as well as having 2 dedicated containers for videos I&#8217;ve purchased like grappling, cycling and skate videos.
  </p>
  
  <p>
    If your media exists on mounted drives like mine does, I would also suggest disabling the &#8220;Empty Trash&#8221; option in case the drives do not mount or become unavailable (suggestion via <a href="https://plus.google.com/+JamesEyrich" target="_blank">IcePick</a>, who also is the one who introduced me to Plex).
  </p>
  
  <p>
    <a href="http://www.nickburaglio.com/wp-content/uploads/2014/01/Screen-Shot-2014-01-18-at-10.14.53-AM.png"><img class="aligncenter size-medium wp-image-620" alt="Screen Shot 2014-01-18 at 10.14.53 AM" src="http://www.nickburaglio.com/wp-content/uploads/2014/01/Screen-Shot-2014-01-18-at-10.14.53-AM-300x238.png" width="300" height="238" /></a>
  </p>
  
  <p>
    &nbsp;
  </p>
  
  <p>
    Now you can get the mobile plex for your iPhone, iPad, chromecast, Android device or any number of other devices.  Personally we use a <a href="http://www.roku.com/" target="_blank">Roku</a> with the plex channel but when I&#8217;m traveling I will often use my iPad as a media player from my hotel room and play my own content directly from my house, sometimes even over a cellular connection if there is spotty wifi.  It&#8217;s like having netflix with my own content.  Win-Win.
  </p>
  
  <p>
    * I have not tested this personally, yet, however, I would encourage anyone to pay for the lifetime <a href="https://plex.tv/subscription/about" target="_blank">plexpass</a>. I plan to do so as soon.
  </p>
  
  <p>
    ** You may need to <a href="http://www.crypt.gen.nz/selinux/disable_selinux.html" target="_blank">disable selinux</a>.  I do it by default so I can&#8217;t say if it works with it on or not.
  </p>