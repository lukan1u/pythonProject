# it dosen't take subdomanins into the account
def domain_name(url):

    is_https = url.find("http")
    is_www = url.find("www")

    if is_https == -1:
        dot = 1 + url.find(".")
        dot2 = url.find(".", dot+1)
        return(url[dot:dot2])
    
    elif is_www == -1:
        slashes = 2 + url.find("/")
        dot2 = url.find(".")
        return(url[slashes:dot2])
    
    else:
        wws = 3 + url.find("www")
        dot2 = url.find(".", -1)
        return (url[wws:dot2])
