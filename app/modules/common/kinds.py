import webapp2
import logging
from google.appengine.ext import ndb


class Example(ndb.Model):
    value = ndb.StringProperty()