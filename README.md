# pyShippingEasy
Provide a thin wrapper around the ShippingEasy API, making it easy to send and sign requests.
Reference https://shippingeasy.readme.io/docs/getting-started for API argument formats.

This module requires requests module, which can be obtained via pip. Methods return a requests object.

##Properties##
Please set prior to using methods. This can be done by editing ShippingEasy.py directly, or by setting variables on the module (see Example.py)

**KeyId**
User API key. Find in ShippingEasy settings.

**KeySecret**
User secret. Find in ShippingEasy settings.

**StoreApiKey**
Required only for CreateOrder. Can be found in ShippingEasy settings, or by inspecting GetOrders return info.

##Methods

**GetOrders(optional Params)**

Get orders corresponding to API key, all stores.
Params: dict with url parameters

**GetOrder(Id)**

Get a single order, by ID.
Id: string of desired order's ID.

**CreateOrder(Order)**

Create an order.
Order: dict with order info. See API docs for format and required parameters. 
