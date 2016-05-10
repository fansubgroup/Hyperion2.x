#!/usr/bin/python
#coding=utf8

from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import re
import urllib
import time
import httplib
import md5
import random
import json

def Writetmpfile(filename,body):
        tmpfile=open(filename,'a')
        tmpfile.writelines('%s' % body)
        tmpfile.close()

def Istxt_file(filename):
        test = re.compile(r".*?txt")
        if test.findall(filename) == []:
                return False
        return True

def split_txt(filename): #分割文件形成独立文件
	jump_ctl = 0
	match_2 = 0 #控制是序号行还是字母行
	zimu_ctl = 0 #控制字母行的数量
	p = re.compile(r"[a-zA-Z]") #排除是字母行的
	q = re.compile(r"[0-9]+")
	print filename
	f = open(filename, 'r')
	lines = f.readlines()
	for i in lines:
		#默认第一行为序号行
		if jump_ctl < 2:
			if match_2 == 0:#index
				i_num = q.findall(i)
				print 'split the %s sentences' % i_num[0]
				Super_value = int(i_num[0])
				#将变量Super_value的值置为序号
                                Writetmpfile('%d_temp.txt' % Super_value,i)
				match_2 = 1
				jump_ctl += 1
			elif match_2 == 1:#timeline
                                Writetmpfile('%d_temp.txt' % Super_value,i)
				match_2 = 0
				jump_ctl += 1
		elif jump_ctl == 2:#body
                        Writetmpfile('%d_temp.txt' % Super_value,i)
			zimu_ctl += 1
			jump_ctl += 1
		elif jump_ctl > 2:
			if p.findall(i):
				#判断是否为下一句的字母行
				if zimu_ctl > 0:
					#print 'else ', zimu_ctl
					#print 'ZiMu second'
                                        Writetmpfile('%d_temp.txt' % Super_value,i)
					zimu_ctl += 1
					jump_ctl += 1
			else:
				#空白行的话
				#print 'this is KB'
				zimu_ctl = 0
				jump_ctl = 0


def get_trans_txt(file_word): #从指定文件中返回需要翻译的字母
	#print 'get_txt_name'
	word_pool = [] #地址池作用
	g = re.compile("[a-zA-Z]+")
	try:
		fp = open(file_word, 'r')
		#print 'find the txt'
		for i in fp.readlines():
			is_word = g.findall(i)
			#判断是否存在字母
			if len(is_word) == 0:
				#如果不存在，则为数字行
				continue
			elif len(is_word) != 0:
				#如果存在，则为字母行
				#print i
				word_pool.append(i)
	except Exception, e:
		print e
	finally:
		if fp:
			fp.close()
			return word_pool


def save_appid(appid, key):
	Usrfile = 'Appid'
	f = open(Usrfile, 'w')
	f.write(appid+'\n'+key)
        f.close()
	print 'Save Successful'

def httpTranslate(appid,key,src,dst,body):
        httpClient = None
	myurl = '/api/trans/vip/translate'
        fromLang = src
        toLang = dst
        salt = random.randint(32768, 65536)
        sign = appid+body+str(salt)+key
        m1 = md5.new()
        m1.update(sign)
        sign = m1.hexdigest()
        myurl = myurl+'?appid='+appid+'&q='+urllib.quote(body)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
	#print appid,key,src,dst
        #print myurl
        try:
                httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
                httpClient.request('GET', myurl)
		response = httpClient.getresponse()
                #print response.status
                ret = response.read()
		#print ret
                json_mid = json.loads(ret)
                #str变字典
                dict_trans = json_mid.get('trans_result')
                #print dict_trans
                #字典中查找元素的值
                dict_trans_mid = dict_trans[0]
                #列表变字典
		result_mid = dict_trans_mid.get('dst')
                #print json_mid[3]['dst']
                result = (result_mid).encode("UTF-8")
                return result
        except Exception, el:
                print el
        finally:
                if httpClient:
                        httpClient.close()

def translation_txt(appid,secretkey,src,dst):
	count_get_app = 0
	path = os.getcwd()
	count_num = 1
	word_pool = [] #地址池的作用
	for txt_name in os.listdir(path):
		#print txt_name
		fp = os.path.join(path, txt_name)
                if not Istxt_file(txt_name):
                        continue
                if os.path.isfile(fp):
			if get_trans_txt(txt_name):
                                print "return trans"
				word_pool = get_trans_txt(txt_name) #获得要翻译的英文句子
				#print 'word_pool for test ', word_pool
				while len(word_pool) != 0: #判断句子池中的句子是否全部翻译完了
					try:
						words = word_pool.pop(0)
					except IndexError, er:
						print er
					if len(words):
                                                result = httpTranslate(appid,secretkey,src,dst,words)
                                                print 'Translation the %d sentences' % count_num
                                                try:
                                                        Writetmpfile(txt_name,result+'\r\n')
                                                except Exception, er:
                                                        print er
                                                count_num += 1

                                        else:
                                                continue
		print 'Now get the result.srt\r\n'
		print '***Finish the translation***'


def join_txt():
	path = os.getcwd()
	result_file = path+'/result.srt'
        q = re.compile(r".*?txt")
	try:
		fres = open(result_file, 'a')
	except Exception, err:
		print err
	filelist = []
        for txt_name in os.listdir(path):
                fp = os.path.join(path, txt_name)
                if q.findall(fp) == []:
                        continue
		filelist.append(txt_name)

	filelist.sort()
	filelist.sort(key=len)

	for txt_name in filelist:
		if os.path.isfile(fp):
                        tmp = open(txt_name, 'r')
                        for i in tmp.readlines():
                                fres.writelines(i)
                                tmp.close()
                        fres.write('\r\n')
        fres.close()
def remove_txt():
	path = os.getcwd()
	word_to_remove = 'temp'
	for filename in os.listdir(path):
		fp = os.path.join(path, filename)
		if os.path.isfile(fp) and word_to_remove in filename:
			os.remove(fp)