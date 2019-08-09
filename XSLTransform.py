#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of Beremiz.
# See COPYING file for copyrights details.

from __future__ import absolute_import
from lxml import etree

class XSLTransform(object):
    """ a class to handle XSLT queries on project and libs """
    def __init__(self, xsltpath, xsltext):

        # parse and compile. "beremiz" arbitrary namespace for extensions
        self.xslt = etree.XSLT(
            etree.parse(
                xsltpath,
                etree.XMLParser()),
            extensions={("beremiz", name): call for name, call in xsltext})

    def transform(self, root, **kwargs):
        res = self.xslt(root, **{k: etree.XSLT.strparam(v) for k, v in kwargs.iteritems()})
        # print(self.xslt.error_log)
        return res


