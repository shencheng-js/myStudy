import urllib.request as ur
def download(url,num_retries=2):
    print("Downloading",url)
    headers = {"User-agent":user_agent}
    request = ur.request_host(url,)
    try:
        html = ur.urlopen(url).read()
    except ur.URLError as e:
        print("Some bad things happen",e.reason)
        html = None

        if num_retries >0 :
            if hasattr(e,'code') and 500 <=e.code <600:
                download(url,num_retries-1)
    return html

