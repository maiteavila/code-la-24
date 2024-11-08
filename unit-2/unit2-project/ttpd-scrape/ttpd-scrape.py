# import the requests library
import requests

# import beautifulsoup
from bs4 import BeautifulSoup

fortnight_response = requests.get("https://www.google.com/search?q=taylor+swift+fortnight+lyrics&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=hLYfZ8e6CM6Fw8cP9prS6Q4&ved=0ahUKEwjHjOe1urGJAxXOwvACHXaNNO0Q4dUDCA8&uact=5&oq=taylor+swift+fortnight+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiHXRheWxvciBzd2lmdCBmb3J0bmlnaHQgbHlyaWNzMgcQABiABBgNMgYQABgHGB4yBxAAGIAEGA0yBxAAGIAEGA0yCBAAGAcYChgeMggQABgHGAoYHjIIEAAYBxgKGB4yCBAAGAcYChgeMgYQABgHGB4yBxAAGIAEGA1I4BVQzARYxBRwAXgBkAEAmAGPAqABuw2qAQUyLjEuNrgBA8gBAPgBAZgCBaAC2wTCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICDhAAGLADGOQCGNYE2AEBwgITEC4YgAQYsAMYQxjIAxiKBdgBAcICChAAGIAEGLEDGA2YAwCIBgGQBhK6BgYIARABGAmSBwUzLjAuMqAH8Ek&sclient=gws-wiz-serp")
ttpd_response = requests.get("https://www.google.com/search?q=taylor+swift+ttpd+lyrics&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=ccofZ6KkG82optQP8dTZ8QQ&ved=0ahUKEwjioKa2zbGJAxVNlIkEHXFqNk4Q4dUDCA8&uact=5&oq=taylor+swift+ttpd+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiGHRheWxvciBzd2lmdCB0dHBkIGx5cmljczIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBhAAGAcYHjIIEAAYBxgKGB4yBhAAGAcYHjIFEAAYgAQyBRAAGIAEMgQQABgeSOILUPMEWPIJcAJ4AZABAJgBdqABvwKqAQMzLjG4AQPIAQD4AQGYAgWgAuEBwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigXCAg4QABiwAxjkAhjWBNgBAcICExAuGIAEGLADGEMYyAMYigXYAQGYAwCIBgGQBhO6BgYIARABGAmSBwE1oAe_GQ&sclient=gws-wiz-serp")
myboy_response = requests.get ("https://www.google.com/search?q=taylor+swift+my+boy+only+breaks+lyrics&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=ksofZ9zVN6CHptQP4O_q-QE&ved=0ahUKEwjc5qDGzbGJAxWgg4kEHeC3Oh8Q4dUDCA8&uact=5&oq=taylor+swift+my+boy+only+breaks+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiJnRheWxvciBzd2lmdCBteSBib3kgb25seSBicmVha3MgbHlyaWNzMgYQABgHGB4yCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCBAAGIAEGKIEMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIESNsfUOQDWN4ccAJ4AZABAJgBzQGgAaETqgEGMTUuOC4xuAEDyAEA-AEBmAISoAKQC8ICChAAGLADGNYEGEfCAg0QABiABBiwAxhDGIoFwgIOEAAYsAMY5AIY1gTYAQHCAhMQLhiABBiwAxhDGMgDGIoF2AEBwgIYEC4YgAQYsAMYQxjUAhjIAxiKBRgK2AEBwgIHEAAYgAQYDcICCBAAGAcYChgewgIKEAAYgAQYsQMYDcICDhAAGIAEGJECGLEDGIoFwgILEAAYgAQYkQIYigXCAgUQABiABMICCBAAGAcYCBgewgIIEAAYCBgNGB6YAwCIBgGQBhO6BgYIARABGAmSBwQxNC40oAffpgE&sclient=gws-wiz-serp")
downbad_response = requests.get ("https://www.google.com/search?q=taylor+swift+down+bad+lyrics&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=ocofZ5WFNrjbptQPidn38A8&ved=0ahUKEwjV2bLNzbGJAxW4rYkEHYnsHf4Q4dUDCA8&uact=5&oq=taylor+swift+down+bad+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiHHRheWxvciBzd2lmdCBkb3duIGJhZCBseXJpY3MyBRAAGIAEMgYQABgHGB4yBRAAGIAEMgYQABgHGB4yBRAAGIAEMgUQABiABDIIEAAYBxgKGB4yBRAAGIAEMgUQABiABDIEEAAYHki-MFAAWJEvcAN4AZABAZgBgAKgAdQLqgEFNS41LjK4AQPIAQD4AQGYAgigAsIDwgIOEAAYgAQYkQIYsQMYigXCAgoQABiwAxjWBBhHwgIIEAAYBxgIGB7CAggQABgFGAcYHsICBxAAGIAEGA2YAwCIBgGQBgiSBwM3LjGgB8Zd&sclient=gws-wiz-serp")
solong_response = requests.get ("https://www.google.com/search?q=taylor+swift+so+long+london+lyrics&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=tcofZ4jHFceV5OMP58noiQk&ved=0ahUKEwjI9dbWzbGJAxXHCnkGHeckOpEQ4dUDCA8&uact=5&oq=taylor+swift+so+long+london+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiInRheWxvciBzd2lmdCBzbyBsb25nIGxvbmRvbiBseXJpY3MyBRAAGIAEMgUQABiABDIGEAAYBxgeMgUQABiABDIFEAAYgAQyBBAAGB4yBBAAGB4yBhAAGAUYHjIGEAAYCBgeMgYQABgIGB5I_hRQnQJYuRJwAXgBkAEBmAH3AaABog2qAQU5LjUuMbgBA8gBAPgBAZgCC6ACjwfCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICDhAAGLADGOQCGNYE2AEBwgITEC4YgAQYsAMYQxjIAxiKBdgBAcICDhAAGIAEGJECGLEDGIoFwgILEAAYgAQYkQIYigXCAggQABgHGAoYHsICCBAAGAcYCBgewgIIEAAYBRgHGB7CAgcQABiABBgNmAMAiAYBkAYTugYGCAEQARgJkgcDOS4yoAe9lwE&sclient=gws-wiz-serp")
butdaddy_response = requests.get ("https://www.google.com/search?q=taylor+swift+but+daddy+i+love+him+lyrics&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=GMsfZ_aKGK6mptQPucv3oAc&ved=0ahUKEwj29vOFzrGJAxUuk4kEHbnlHXQQ4dUDCA8&uact=5&oq=taylor+swift+but+daddy+i+love+him+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiKHRheWxvciBzd2lmdCBidXQgZGFkZHkgaSBsb3ZlIGhpbSBseXJpY3MyBRAAGIAEMgUQABiABDIGEAAYBxgeMgYQABgHGB4yBRAAGIAEMgYQABgFGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB4yBhAAGAgYHkirCVDsA1jHBnABeAGQAQCYAVagAZ8BqgEBMrgBA8gBAPgBAZgCA6ACpwHCAgoQABiwAxjWBBhHwgIHEAAYgAQYDcICCBAAGAcYCBgewgIIEAAYBRgHGB6YAwDiAwUSATEgQIgGAZAGCJIHATOgB5gT&sclient=gws-wiz-serp")
freshout_response = requests.get ("https://www.google.com/search?q=taylor+swift+fresh+out+the+slammer+lyrics&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=GssfZ52yObaJptQPyuDa-Qo&oq=taylor+swift+fresh+out+the+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiIXRheWxvciBzd2lmdCBmcmVzaCBvdXQgdGhlIGx5cmljcyoCCAAyBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB4yBhAAGAgYHkiRGVDkBVjCEXABeAGQAQCYAXagAeMIqgEEMTAuM7gBAcgBAPgBAZgCCqACgAbCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICDhAAGLADGOQCGNYE2AEBwgITEC4YgAQYsAMYQxjIAxiKBdgBAcICCBAAGAcYChgewgIIEAAYBxgIGB6YAwCIBgGQBhO6BgYIARABGAmSBwM5LjGgB-Z3&sclient=gws-wiz-serp")
florida_response = requests.get ("https://www.google.com/search?q=taylor+swift+florida+lyrics&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=KMsfZ-DCJvyGptQPloP44AM&ved=0ahUKEwjg9tKNzrGJAxV8g4kEHZYBHjwQ4dUDCA8&uact=5&oq=taylor+swift+florida+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiG3RheWxvciBzd2lmdCBmbG9yaWRhIGx5cmljczIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBhAAGAcYHjIEEAAYHjIEEAAYHjIEEAAYHjIGEAAYCBgeMgYQABgIGB5I1xlQrQNY0hZwBngBkAEAmAHsAaABvAqqAQU2LjUuMbgBA8gBAPgBAZgCDKAC1gTCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICDhAAGLADGOQCGNYE2AEBwgITEC4YgAQYsAMYQxjIAxiKBdgBAcICBxAAGIAEGA3CAggQABgIGA0YHsICBhAAGA0YHsICCBAAGAcYChgewgILEAAYgAQYhgMYigXCAggQABiABBiiBMICCBAAGAcYCBgemAMAiAYBkAYTugYGCAEQARgJkgcEMTAuMqAHmmQ&sclient=gws-wiz-serp")
guiltyas_response = requests.get ("https://www.google.com/search?q=taylor+swift+guilty+as+sin+lyrics&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=ossfZ-vmMLmYptQPtfq3eQ&ved=0ahUKEwjrv_PHzrGJAxU5jIkEHTX9LQ8Q4dUDCA8&uact=5&oq=taylor+swift+guilty+as+sin+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiIXRheWxvciBzd2lmdCBndWlsdHkgYXMgc2luIGx5cmljczIFEAAYgAQyBRAAGIAEMgYQABgHGB4yBhAAGAcYHjIFEAAYgAQyBRAAGIAEMgQQABgeMgQQABgeMgQQABgeMggQABgFGAoYHkj0L1CMCFiCKnAGeAGQAQOYAcgDoAHxFqoBCTguNy4yLjEuMbgBA8gBAPgBAZgCEaAC4wjCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICDhAAGLADGOQCGNYE2AEBwgIWEC4YgAQYsAMYQxjUAhjIAxiKBdgBAcICExAuGIAEGLADGEMYyAMYigXYAQHCAgYQABgNGB7CAggQABgIGA0YHsICChAAGAgYChgNGB7CAgsQABiABBiGAxiKBcICCBAAGIAEGKIEwgIIEAAYogQYiQXCAgoQIRigARjDBBgKwgIIECEYoAEYwwTCAgcQABiABBgNwgIIEAAYBxgIGB7CAgoQABgFGAcYChgewgIGEAAYCBgemAMAiAYBkAYTugYGCAEQARgJkgcEMTQuM6AHja0B&sclient=gws-wiz-serp")
whosafraid_response = requests.get ("https://www.google.com/search?q=who%27s+afraid+of+little+old+me+lyrics+taylor+swift&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=OdAfZ-ODBsmgptQPq-eG6Qo&oq=taylor+swift+whos+afraid++lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiIHRheWxvciBzd2lmdCB3aG9zIGFmcmFpZCAgbHlyaWNzKgIIADIIEAAYBxgKGB4yCBAAGAcYChgeMggQABgIGAoYHjILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMggQABiABBiiBDIIEAAYgAQYogQyCBAAGIAEGKIEMggQABiABBiiBEjoJFDTA1iPFHABeAGQAQCYAbIDoAHgD6oBCTIuOC4xLjAuMbgBAcgBAPgBAZgCBqACkQjCAggQLhgIGAoYHsICCBAAGKIEGIkFwgIKEC4YBxgIGAoYHsICChAAGAcYCBgKGB6YAwCIBgGSBwcyLjMuNC0xoAeNaQ&sclient=gws-wiz-serp")
fixhim_response = requests.get ("https://www.google.com/search?q=i+can+fix+him+no+really+i+can+lyrics+taylor+swift&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=UNAfZ5DlJYOJptQPiJHs4Ac&ved=0ahUKEwiQzYiD07GJAxWDhIkEHYgIG3wQ4dUDCA8&uact=5&oq=i+can+fix+him+no+really+i+can+lyrics+taylor+swift&gs_lp=Egxnd3Mtd2l6LXNlcnAiMWkgY2FuIGZpeCBoaW0gbm8gcmVhbGx5IGkgY2FuIGx5cmljcyB0YXlsb3Igc3dpZnQyBBAAGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB4yCxAAGIAEGIYDGIoFMggQABiABBiiBDIIEAAYgAQYogRInx1QAFiUG3AAeAGQAQCYAYsBoAGkE6oBBDIwLjm4AQPIAQD4AQGYAhegAvUOwgIGEAAYBxgewgIIEAAYBxgIGB7CAgoQABgFGAcYChgewgIKEAAYBxgIGAoYHsICCBAAGAgYDRgewgIHEAAYgAQYDcICBRAAGIAEmAMAkgcEMTYuN6AH4pEC&sclient=gws-wiz-serp")
loml_response = requests.get ("https://www.google.com/search?q=loml+lyrics+taylor+swift&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=n9EfZ5OZJZS3ptQP9ZGy2Ac&ved=0ahUKEwjT5Oai1LGJAxWUm4kEHfWIDHsQ4dUDCA8&uact=5&oq=loml+lyrics+taylor+swift&gs_lp=Egxnd3Mtd2l6LXNlcnAiGGxvbWwgbHlyaWNzIHRheWxvciBzd2lmdDIKEAAYgAQYQxiKBTIFEAAYgAQyBhAAGAcYHjIFEAAYgAQyBBAAGB4yBBAAGB4yBBAAGB4yBBAAGB4yBBAAGB4yBBAAGB5I2R9QrhZYvh1wAXgBkAEAmAGcAaAB5wSqAQMzLjO4AQPIAQD4AQGYAgagApMEwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigXCAggQABgHGAoYHsICBxAAGIAEGA2YAwCIBgGQBgqSBwMzLjOgB-Up&sclient=gws-wiz-serp")
brokenheart_response = requests.get ("https://www.google.com/search?q=i+can+do+it+with+a+broken+heart+lyrics+taylor+swift&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=v9EfZ8H8OPyHptQPweT-sAo&ved=0ahUKEwiB2Juy1LGJAxX8g4kEHUGyH6YQ4dUDCA8&uact=5&oq=i+can+do+it+with+a+broken+heart+lyrics+taylor+swift&gs_lp=Egxnd3Mtd2l6LXNlcnAiM2kgY2FuIGRvIGl0IHdpdGggYSBicm9rZW4gaGVhcnQgbHlyaWNzIHRheWxvciBzd2lmdDIFEAAYgAQyBhAAGAcYHjIEEAAYHjIEEAAYHjIGEAAYCBgeMgYQABgIGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB4yBhAAGAgYHkiSBVCHA1iHA3AAeAOQAQCYAVagAVaqAQExuAEDyAEA-AEBmAIDoAJgwgIEEAAYR5gDAOIDBRIBMSBAiAYBkAYIkgcBM6AHmwk&sclient=gws-wiz-serp")
smallestman_response = requests.get ("https://www.google.com/search?q=the+smallest+man+who+ever+lived+lyrics+taylor+swift&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=xNEfZ6KhMZW2ptQPxIqL4Qg&ved=0ahUKEwiik8W01LGJAxUVm4kEHUTFIowQ4dUDCA8&uact=5&oq=the+smallest+man+who+ever+lived+lyrics+taylor+swift&gs_lp=Egxnd3Mtd2l6LXNlcnAiM3RoZSBzbWFsbGVzdCBtYW4gd2hvIGV2ZXIgbGl2ZWQgbHlyaWNzIHRheWxvciBzd2lmdDIFEAAYgAQyBhAAGAgYHjIGEAAYCBgeMgYQABgIGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB5IpS5QAFjAKXAEeAGQAQCYAYsBoAGfGKoBBTIzLjEyuAEDyAEA-AEBmAIYoALaDMICBhAAGAcYHsICCBAAGAcYCBgewgILEAAYgAQYhgMYigXCAggQABiABBiiBMICBhAAGA0YHsICCBAAGKIEGIkFwgIHEAAYgAQYDZgDAJIHBDIxLjOgB9_FAg&sclient=gws-wiz-serp")
alchemy_response = requests.get("https://www.google.com/search?q=the+alchemy+lyrics+taylor+swift&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=-dEfZ65EsKym1A_c2NLxAQ&ved=0ahUKEwjupLfN1LGJAxUwlokEHVysNB4Q4dUDCA8&uact=5&oq=the+alchemy+lyrics+taylor+swift&gs_lp=Egxnd3Mtd2l6LXNlcnAiH3RoZSBhbGNoZW15IGx5cmljcyB0YXlsb3Igc3dpZnQyBRAAGIAEMgQQABgeMgQQABgeMgQQABgeMgYQABgIGB4yCBAAGAgYChgeMgYQABgIGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB5I-wpQAFj-CHAAeAGQAQGYAbwBoAGYC6oBAzMuObgBA8gBAPgBAZgCBaACvAPCAgYQABgHGB7CAggQABgHGAgYHsICChAAGAcYCBgKGB7CAgcQABiABBgNmAMAkgcDMi4zoAe6bQ&sclient=gws-wiz-serp")
clarabow_response = requests.get ("https://www.google.com/search?q=clara+bow+lyrics+taylor+swift&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=BdIfZ4CpCvqX5OMPsL3ImQk&ved=0ahUKEwjAv53T1LGJAxX6C3kGHbAeMpMQ4dUDCA8&uact=5&oq=clara+bow+lyrics+taylor+swift&gs_lp=Egxnd3Mtd2l6LXNlcnAiHWNsYXJhIGJvdyBseXJpY3MgdGF5bG9yIHN3aWZ0MgUQABiABDIFEAAYgAQyBBAAGB4yBBAAGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB5I3xpQAFi6GHAHeAGQAQCYAZwBoAHZCqoBBDEzLjO4AQPIAQD4AQGYAhKgAoMHwgIGEAAYBxgewgIIEAAYBxgKGB7CAggQABgHGAgYHsICBxAAGIAEGA3CAgYQABgNGB7CAggQABgFGA0YHsICCBAAGIAEGKIEwgIIEAAYogQYiQXCAggQABgIGAoYHsICCBAAGAgYDRgewgILEAAYgAQYhgMYigWYAwCSBwQxNi4yoAe0eQ&sclient=gws-wiz-serp")


# print(response.text[:500])

fortnight_soup_html = BeautifulSoup(fortnight_response.text, "html.parser")
ttpd_soup_html = BeautifulSoup(ttpd_response.text, "html.parser")
myboy_soup_html = BeautifulSoup(myboy_response.text, "html.parser")
downbad_soup_html = BeautifulSoup(downbad_response.text, "html.parser")
solong_soup_html = BeautifulSoup(solong_response.text, "html.parser")
butdaddy_soup_html = BeautifulSoup(butdaddy_response.text, "html.parser")
freshout_soup_html = BeautifulSoup(freshout_response.text, "html.parser")
florida_soup_html = BeautifulSoup(florida_response.text, "html.parser")
guiltyas_soup_html = BeautifulSoup(guiltyas_response.text, "html.parser")
whosafraid_soup_html = BeautifulSoup(whosafraid_response.text, "html.parser")
fixhim_soup_html = BeautifulSoup(fixhim_response.text, "html.parser")
loml_soup_html = BeautifulSoup(loml_response.text, "html.parser")
brokenheart_soup_html = BeautifulSoup(brokenheart_response.text, "html.parser")
smallestman_soup_html = BeautifulSoup(smallestman_response.text, "html.parser")
alchemy_soup_html = BeautifulSoup(alchemy_response.text, "html.parser")
clarabow_soup_html = BeautifulSoup(clarabow_response.text, "html.parser")




fortnight_soup_text = fortnight_soup_html.get_text()
ttpd_soup_text = ttpd_soup_html.get_text()
myboy_soup_text = myboy_soup_html.get_text()
downbad_soup_text = downbad_soup_html.get_text()
solong_soup_text = solong_soup_html.get_text()
butdaddy_soup_text = butdaddy_soup_html.get_text()
freshout_soup_text = freshout_soup_html.get_text()
florida_soup_text = florida_soup_html.get_text()
guiltyas_soup_text = guiltyas_soup_html.get_text()
whosafraid_soup_text = whosafraid_soup_html.get_text()
fixhim_soup_text = fixhim_soup_html.get_text()
loml_soup_text = loml_soup_html.get_text()
brokenheart_soup_text = brokenheart_soup_html.get_text()
smallestman_soup_text = smallestman_soup_html.get_text()
alchemy_soup_text = alchemy_soup_html.get_text()
clarabow_soup_text = clarabow_soup_html.get_text()



fortnight_data = open('fortnight.txt', 'w')
fortnight_data.write(fortnight_soup_text)
fortnight_data.close()

ttpd_data = open('ttpd.txt', 'w')
ttpd_data.write(ttpd_soup_text)
ttpd_data.close()

myboy_data = open('my-boy-only-breaks-his-favorite-toys.txt', 'w')
myboy_data.write(myboy_soup_text)
myboy_data.close()

downbad_data = open('down-bad.txt', 'w')
downbad_data.write(downbad_soup_text)
downbad_data.close()

solong_data = open('so-long-london.txt', 'w')
solong_data.write(solong_soup_text)
solong_data.close()

butdaddy_data = open('but-daddy-i-love-him.txt', 'w')
butdaddy_data.write(butdaddy_soup_text)
butdaddy_data.close()

freshout_data = open('fresh-out-the-slammer.txt', 'w')
freshout_data.write(freshout_soup_text)
freshout_data.close()

florida_data = open('florida.txt', 'w')
florida_data.write(florida_soup_text)
florida_data.close()

guiltyas_data = open('guily-as-sin.txt', 'w')
guiltyas_data.write(guiltyas_soup_text)
guiltyas_data.close()

whosafraid_data = open('whos-afraid-of-little-old-me.txt', 'w')
whosafraid_data.write(whosafraid_soup_text)
whosafraid_data.close()

fixhim_data = open('i-can-fix-him.txt', 'w')
fixhim_data.write(fixhim_soup_text)
fixhim_data.close()

loml_data = open('loml.txt', 'w')
loml_data.write(loml_soup_text)
loml_data.close()

brokenheart_data = open('i-can-do-it-with-a-broken-heart.txt', 'w')
brokenheart_data.write(brokenheart_soup_text)
brokenheart_data.close()

smallestman_data = open('the-smallest-man-who-ever-lived.txt', 'w')
smallestman_data.write(smallestman_soup_text)
smallestman_data.close()

alchemy_data = open('the-alchemy.txt', 'w')
alchemy_data.write(alchemy_soup_text)
alchemy_data.close()

clarabow_data = open('clara-bow.txt', 'w')
clarabow_data.write(clarabow_soup_text)
clarabow_data.close()
# def getTitles(soupdata):  
#   titles = soupdata.select("text")
#   if titles:
#     for t in titles:
#       print(t.text)
      
# print("Tim Mcgraw........")
# getTitles(tim_soup_html)
# print("Picture To Burn.........")
# getTitles(picture_soup_html)
