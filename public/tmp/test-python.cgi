#!/usr/bin/python
# -*- coding: euc-jp -*-

import site
import cgi
import os

print "content-type: text/html\n\n"

print '<html>'
print '<head><meta charset="euc-jp"></head>'
print '<body>'
print '<h1>CGI����ץ�</h1>'
print '<form action="test-python.cgi" method="get">'
print '��å����� <input type="text" name="msg">'
print '<input type="submit">'
print '</form>'

# form�������������ˡ��������ƽ��Ϥ��Ƥߤ�
if os.environ['REQUEST_METHOD'] == 'POST':
	print 'POST'
elif os.environ['REQUEST_METHOD'] == 'GET':
	print 'GET'

print '<br />'

# ���Ϥ��줿�ͤ���Ϥ���
form = cgi.FieldStorage()
if form.has_key('msg'):
	print '<h2>' + form['msg'].value + '</h2>'

print '<body>'
print '</html>'
