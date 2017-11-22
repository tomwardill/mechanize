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
    from urllib.parse import urlparse
else:
    import urlparse

if sys.version_info[0] > 2:
    from urllib.parse import urlencode
else:
    from urllib import urlencode

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
        unquote,
        unwrap,
        url2pathname
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
        unquote,
        unwrap,
        url2pathname
    )

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
    from email.message import Message
else:
    from mimetools import Message
