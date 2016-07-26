# coding: utf-8
import datetime
import json
import ShippingEasy


ShippingEasy.KeyId = 'KEY'
ShippingEasy.KeySecret = 'SECRET'
ShippingEasy.StoreApiKey = 'KEY'

def SendRequest():
	payload = { 'order': 
	   {
	      'external_order_identifier':'Example1',
	      'ordered_at':datetime.datetime.now().isoformat(),
	      'recipients':[{
	         'first_name':'firstName',
	         'last_name':'lastName',
	         'email':'email',
	         'address':'address',
	         'address2':'address2',
	         'state':'state',
	         'city': 'city',
	         'postal_code':'zipCode',
	         'country':'country',
	         'items_total':'1',
	         'items_shipped':'0',
	         'line_items':[{
	            'item_name':'Item',
	            'quantity':'1'
	         }]
	      }]
	   }
	}
	res = ShippingEasy.CreateOrder(payload)
	pretty = json.dumps(res.json(), sort_keys=True, indent=4)
