"""Praetorian SOW-2026-02-2507 authorized render probe.

Marker PRAETXSS9. Payloads below are inert: the handlers set a window property
and contact no host. They test whether analyzer output derived from repository
content is HTML-escaped when rendered in the portal.

Docstring payload: <img src=x onerror="window.__PRAETXSS9_DOC=1">
Attribute breakout: " autofocus onfocus="window.__PRAETXSS9_ATTR=1
Script payload: <script>window.__PRAETXSS9_SCRIPT=1</script>
"""

PRAETXSS9_STRING_SINK = '<img src=x onerror="window.__PRAETXSS9_STR=1">'
PRAETXSS9_ATTR_SINK = '" autofocus onfocus="window.__PRAETXSS9_ATTR2=1'

# comment payload: <svg/onload="window.__PRAETXSS9_CMT=1">


def praetxss9_undocumented_and_long():
    total = 0
    for i in range(200):
        if i % 2 == 0:
            if i % 3 == 0:
                if i % 5 == 0:
                    if i % 7 == 0:
                        total += i * 11
                    else:
                        total += i * 7
                else:
                    total += i * 5
            else:
                total += i * 3
        else:
            total += i
    payload = PRAETXSS9_STRING_SINK + PRAETXSS9_ATTR_SINK
    return total, payload


def praetxss9_taint_source(user_input):
    """Returns <img src=x onerror="window.__PRAETXSS9_FN=1"> to the caller."""
    import os
    return os.popen(user_input).read()
