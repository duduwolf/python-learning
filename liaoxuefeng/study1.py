#!/usr/bin/env python
import sys
import urllib
import base64
import os

domains = '''
google.com
www.google.com
docs.google.com
code.google.com
www.facebook.com
facebook.com
www.twitter.com
twitter.com
mail.google.com
whatismyipaddress.com
ggpht.com
www.youtube.com
youtube.com
youtu.be
ziplib.com
autoproxy-gfwlist.googlecode.com
googlepages.com
fuckgfw.com
ssl.gstatic.com
gstatic.com
support.google.com
survey.googleratings.com
play.google.com
plus.google.com
googleads.g.doubleclick.net
doubleclick.net
www.gmail.com
accounts.google.com
wallet.google.com
maps.google.com
news.google.com
drive.google.com
translate.google.com
books.google.com
www.blogger.com
photos.google.com
picasaweb.google.com
myaccount.google.com
apis.google.com
clients1.google.com
clients2.google.com
clients3.google.com
clients4.google.com
clients5.google.com
clients6.google.com
googlecode.com
smarthosts.googlecode.com
apps.google.com
www.sexinsex.net
support.google.com
survey.googleratings.com
plus.google.com
play.google.com
wallet.google.com
books.google.com
www.blogger.com
chrome.google.com
families.google.com
passwords.google.com
security.google.com
settings.xn--9trs65b.com
wallet.google.com
photos.google.com
www.gstatic.com
lh5.googleusercontent.com

'''
VPNIF='ppp0'
# str = 'www.google.com'
# print(type(str.encode()))
# print(base64.encodestring(str.encode()))

if not os.access('/etc/hosts', os.W_OK):
    print >> sys.stderr,'you need sudo ...'
    exit(1)

url = 'http://bluehua.org/demo/getip.php?&name[]=' + '&name[]='.join([base64.encodestring(d).strip() for d in domains.split('\n') if d])
print(url)
iptable = urllib.urlopen(url).read().split('\n')
print(iptable)
ips = [rule.split(' ')[0] for rule in iptable if rule]
print(ips)

print('update route table')
for ip in ips:
    if sys.platform == 'darwin':
        # print >> sys.stderr,ip + ' ' + VPNIF
        os.system('route add -net %s -interface %s' % (ip, VPNIF))
    else:
        os.system('route add -net %s netmask 255.255.255.255 dev %s' % (ip, VPNIF))


print('update hosts')
