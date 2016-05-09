#!/usr/bin/python
# -*- coding: utf-8 -*-

# $Id$

from __future__ import print_function
import sys
import os

# for compatible python 3
try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen

try:
	import chardet
except ImportError:
	osinfo = os.uname ()
	sys.path.append (
		os.getcwd () +
		'/build/lib.' +
		osinfo[0].lower() + '-'
		+ osinfo[4] + '-' +
		str (sys.version_info[0]) + '.'
		+ str(sys.version_info[1])
	)
	import chardet

urlread = lambda url: urlopen (url).read ()
PyVer = int (sys.version[0])

urls = [
	'http://google.cn',
	'http://yahoo.co.jp',
	'http://amazon.co.jp',
	'http://pravda.ru',
	'http://auction.co.kr',
	'http://haaretz.co.il'
]

for url in urls :
	err = []
	print ("URL %-20s : " % url, end=""),
	# det member => encoding(string), confidence(.2f)
	det = chardet.detector (urlread (url), err)
	if ( det == None ) :
		print ("Error: %s" % err)
	print ("encoding: %-15s, confidence: %.2f" % (det.encoding, det.confidence))

sys.exit (0)
