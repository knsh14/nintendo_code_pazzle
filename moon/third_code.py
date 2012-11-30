# -*- coding:utf-8 -*-
import re

def decode_char(pattern):
	pattern_dict = {"iI"  :"a","Iiii":"b","IiIi":"c","Iii" :"d","i"   :"e","iiIi":"f","IIi" :"g",
					"iiii":"h","ii"  :"i","iIII":"j","IiI" :"k","iIii":"l","II"  :"m","Ii"  :"n",
					"III" :"o","iIIi":"p","IIiI":"q","iIi" :"r","iii" :"s","I"   :"t","iiI" :"u",
					"iiiI":"v","iII" :"w","IiiI":"x","IiII":"y","IIii":"z"}
	if pattern in pattern_dict:
		return pattern_dict[pattern]
	else:
		return ''

def decode_morse(text):
	decode_text = re.split('[\s]+', text)
	ans_text = ''
	for pattern in decode_text:
		ans_text += decode_char(pattern)
	return ans_text