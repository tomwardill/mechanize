import sys

if sys.version_info[0] > 2:
    from http.cookiejar import Cookie
else:
    from cookielib import Cookie

if sys.version_info[0] > 2:
    from http.cookiejar import CookieJar
else:
    from cookielib import CookieJar

if sys.version_info[0] > 2:
    from http.cookiejar import MozillaCookieJar
else:
    from cookielib import MozillaCookieJar

if sys.version_info[0] > 2:
    from http.cookiejar import request_host
else:
    from cookielib import request_host

if sys.version_info[0] > 2:
    from http.cookiejar import (DEFAULT_HTTP_PORT, CookiePolicy, DefaultCookiePolicy,
                       FileCookieJar, LoadError, LWPCookieJar, _debug,
                       domain_match, eff_request_host, escape_path, is_HDN,
                       lwp_cookie_str, reach, request_path, request_port,
                       user_domain_match)
else:
    from cookielib import (DEFAULT_HTTP_PORT, CookiePolicy, DefaultCookiePolicy,
                       FileCookieJar, LoadError, LWPCookieJar, _debug,
                       domain_match, eff_request_host, escape_path, is_HDN,
                       lwp_cookie_str, reach, request_path, request_port,
                       user_domain_match)

if sys.version_info[0] > 2:
    import urllib.parse as urlparse
    from urllib.parse import urlencode
    from urllib.parse import urljoin
else:
    import urlparse
    from urllib import urlencode
    from urlparse import urljoin

if sys.version_info[0] > 2:
    from urllib.response import addinfourl
else:
    from urllib import addinfourl

if sys.version_info[0] > 2:
    from urllib.request import (
        ftpwrapper,
        getproxies,
        splitattr,
        splitpasswd,
        splittype,
        splituser,
        splitvalue,
        splitport,
        splithost,
        unquote,
        unwrap,
        url2pathname,
        proxy_bypass
    )
else:
    from urllib import (
        ftpwrapper,
        getproxies,
        splitattr,
        splitpasswd,
        splittype,
        splituser,
        splitvalue,
        splitport,
        splithost,
        unquote,
        unwrap,
        url2pathname,
        proxy_bypass
    )

if sys.version_info[0] > 2:
    from urllib import robotparser
else:
    import robotparser

if sys.version_info[0] > 2:
    from urllib.error import (
        HTTPError,
        URLError
    )
else:
    from urllib2 import HTTPError, URLError

if sys.version_info[0] > 2:
    from http import client as httplib
else:
    import httplib

if sys.version_info[0] > 2:
    from io import StringIO
else:
    from cStringIO import StringIO

# https://stackoverflow.com/a/34463112
if sys.version_info[0] > 2:
    def reraise(tp, value, tb=None):
        if value is None:
            value = tp()
        if value.__traceback__ is not tb:
            raise value.with_traceback(tb)
        raise value
else:
    exec("def reraise(tp, value, tb=None):\n    raise tp, value, tb\n")

if sys.version_info[0] > 2:
    def getheaders(self, header):
        return self.get_all(header)
    from email.message import Message
    Message.getheaders = getheaders
else:
    from mimetools import Message

def message_factory(input_headers):
    if sys.version_info[0] > 2:
        import email
        message = email.message_from_string("\n".join(input_headers))
        return message
    else:
        return Message(StringIO("\n".join(input_headers)))

if sys.version_info[0] > 2:
    STRING_TYPES = (str,)
else:
    from types import StringType, UnicodeType
    STRING_TYPES = (StringType, UnicodeType)

if sys.version_info[0] > 2:
    long = int
else:
    long = long

if sys.version_info[0] > 2:
    HTTPS = True
else:
    HTTPS = hasattr(httplib, 'HTTPS')
