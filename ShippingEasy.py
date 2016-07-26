# coding: utf-8
import hmac
import hashlib
import base64
import requests
import time
import json
from urllib import urlencode

KeyId = 'YOUR API KEY'
KeySecret = 'YOUR API SECRET'
StoreApiKey = 'YOUR STORE API KEY'
url_base = 'https://app.shippingeasy.com'


def CreateOrder(payload):
		
	method = 'POST'
	url = '/api/stores/%s/orders' % StoreApiKey
		
	url_string = GetUrlParamsString()
		
	payload_string = json.dumps(payload)
	
	request_url = GetSignedUrl(method, url, url_string, payload_string)
	
	r = requests.post(request_url, json=payload)
		
	return r
	
def GetOrders(url_params=None):
		
	method = 'GET'
	url = '/api/orders'
	url_string = GetUrlParamsString(url_params)
	
	request_url = GetSignedUrl(method, url, url_string)
	
	r = requests.get(request_url)
		
	return r
	
def GetOrder(id):
		
	method = 'GET'
	url = '/api/orders/%s' % id
	url_string = GetUrlParamsString()
	
	request_url = GetSignedUrl(method, url, url_string)
	
	r = requests.get(request_url)
		
	return r
	
def GetSignedUrl(method, url, url_string, payload_string=None):
	signature = CreateSignature(method, url, url_string, payload_string)
	
	request_url = '%s%s?%s&api_signature=%s' % (url_base, url, url_string, signature)
	return request_url
	
	
def CreateSignature(method, url, url_string, payload_string=None):
	string_tosign = '%s&%s&%s' % (method, url, url_string)
	if payload_string:
			string_tosign = '%s&%s' % (string_tosign, payload_string)
		
	dig = hmac.new(KeySecret, msg=string_tosign, digestmod=hashlib.sha256).hexdigest()
	return dig
	
def GetUrlParamsString(url_params = None):
	url_params = url_params or {}
	url_params['api_key'] = KeyId
	url_params['api_timestamp'] = int(time.time())
		
	keys = url_params.keys()
	keys.sort()
	values = map(url_params.get, keys)
		
	val = urlencode(zip(keys, values))
	return val
	
