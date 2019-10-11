---
title: Audio Books and the iPhone/iPod/iTunes
author: buraglio
type: post
date: 2008-11-16T10:54:00+00:00
url: /2008/11/16/audio-books-and-the-iphoneipoditunes/
blogger_blog:
  - www.nickburaglio.com
blogger_author:
  - Nick Buraglio
blogger_permalink:
  - /2008/11/audio-books-and-iphoneipoditunes.html
categories:
  - The firehose

---
I am a fan of audio books since I rarely have time to read any fiction (or even nonfiction) anymore the iPod (and now iPhone) have been a great help in making my time more versatile and allowing me to enjoy some books that I would otherwise not have time to enjoy.   
The biggest limitation that I have run into is that iTunes (and by nature the iPod/iPhone) doesn&#8217;t play as nicely as I think it should with mp3 files as it does with it&#8217;s m4b, the format it uses for audio books, and many of the [free audio books][1] come as mp3 format. With the m4b format you can get playback from the &#8220;bookmarking&#8221; of where the file was last played from. More info on the file format can be found [here][2].   
So, as I found, there are many ways to do this. Being a command line junkie like I am, I was obviously searching for a way to just get this done under terminal on my mac.   
I came across [this page][3] which had a few ways to do it and found that the easiest way (for me) was just to use the command  
`<br />mpg123 -s /path/to/file/audiobook.mp3 |faac -b 80 -P -X -w -o /path/to/output/file/audiobook.m4b -<br />`  
which works perfect, the file can be added directly into itunes&#8230;&#8230;assuming you have all of the binaries installed to make it happen (I didn&#8217;t but it was easy enough to get installed).   
For anyone that \*doesn&#8217;t\* have them installed, I **highly** suggest installing [MacPorts][4]. Once you have MacPorts installed (the [instructions][5] are very easy and it&#8217;s fairly painless to install), you&#8217;ll need to install mpg123 and faac.   
To accomplish this open terminal and type

`sudo port install faac`

and 

`sudo port install mpg123`

There will be a bunch of text across the screen as each program is built and it may take some time based on your machine speed.   
After those are installed, run the command above and you should have your audio book.   
Your output should be something like this:  
<img src="http://buraglio.com/nick/gallery2/d/10762-1/m4bcreate.png" alt="m4b creation" width="500" height="500" />

Now just double click the file and iTunes should do the right thing and put it right into your Audio Books play list.

 [1]: http://tinyurl.com/6h5br9
 [2]: http://en.wikipedia.org/wiki/MP4
 [3]: http://polyphase.ca/archives/2004/11/30/homegrown-audio-books-and-ipod/
 [4]: http://www.macports.org/
 [5]: http://www.macports.org/install.php