# Format of the ServiceAccountKey.py Module #

The Lizard Server application depends on a Python module named
`ServiceAccountKey.py`. This module contains a single class,
`ServiceAccountKey`, which contains only the method `getPath()`, used to get
the path of the `.json` file containing the private Service Account Key. This
module needs to be created by the uer in order for the application to start.
Given below is an example of a correctly defined module:

```
ServiceAccountKey.py:

class ServiceAccountKey:
	def getPath():
		return ('/path/to/service/key.json')
```

And that's all. The Lizard application server is already set up to handle this
module correctly.
