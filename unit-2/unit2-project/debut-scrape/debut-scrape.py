# import the requests library
import requests

# import beautifulsoup
from bs4 import BeautifulSoup

tim_response = requests.get("https://www.google.com/search?q=taylor+swift+tim+mcgraw+lyrics&sca_esv=dcbcef83952848e4&ei=Y0QZZ6GoKpCv5NoPybKyKA&oq=taylor+swift+timmcgraw+l&gs_lp=Egxnd3Mtd2l6LXNlcnAiGHRheWxvciBzd2lmdCB0aW1tY2dyYXcgbCoCCAAyBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBxAAGIAEGA0yBhAAGBYYHjIIEAAYFhgKGB4yBhAAGA0YHjIGEAAYFhgeSO-pBlD8CliuG3ACeACQAQGYAeUBoAGkCqoBBjEwLjIuMbgBAcgBAPgBAZgCDaACxwjCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICDhAAGLADGOQCGNYE2AEBwgITEC4YgAQYsAMYQxjIAxiKBdgBAcICEBAAGIAEGJECGIoFGEYY-wHCAhEQABiABBiRAhixAxiDARiKBcICDhAAGIAEGJECGLEDGIoFwgIFEAAYgATCAgsQABiABBixAxiDAcICDhAAGIAEGLEDGIMBGIoFwgIIEAAYgAQYsQPCAhwQABiABBiRAhiKBRhGGPsBGJcFGIwFGN0E2AEBwgIIEC4YgAQYsQPCAgUQLhiABMICCxAAGIAEGJECGIoFwgIHEAAYgAQYCsICChAuGIAEGLEDGArCAgcQLhiABBgKwgIHEC4YgAQYDZgDAIgGAZAGE7oGBggBEAEYCZIHBDEwLjOgB6uuAQ&sclient=gws-wiz-serp")
picture_response = requests.get("https://www.google.com/search?q=taylor+swift+picture+to+burn+lyrics&sca_esv=dcbcef83952848e4&ei=uLIfZ5TvJaedptQP0eXW0Ac&ved=0ahUKEwiUq8bmtrGJAxWnjokEHdGyFXoQ4dUDCA8&uact=5&oq=taylor+swift+picture+to+burn+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiI3RheWxvciBzd2lmdCBwaWN0dXJlIHRvIGJ1cm4gbHlyaWNzMgsQABiABBiRAhiKBTIGEAAYBxgeMgQQABgeMgYQABgIGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB5InNgBULO-AVj90wFwBHgBkAEAmAGLBKABjxyqAQswLjQuMy4wLjQuMbgBA8gBAPgBAZgCBqACmQfCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICDhAAGLADGOQCGNYE2AEBwgITEC4YgAQYsAMYQxjIAxiKBdgBAcICCBAAGAgYDRgewgILEAAYgAQYhgMYigXCAggQABiABBiiBMICBxAAGIAEGA3CAggQABgHGAgYHpgDAIgGAZAGE7oGBggBEAEYCZIHBTQuNC0yoAfoXg&sclient=gws-wiz-serp")
teardrops_response = requests.get ("https://www.google.com/search?q=taylor+swift+teardrops+on+my+guitar+lyrics&sca_esv=dcbcef83952848e4&ei=2LIfZ_KlOKDXptQPkqXakAo&ved=0ahUKEwjy8fn1trGJAxWgq4kEHZKSFqIQ4dUDCA8&uact=5&oq=taylor+swift+teardrops+on+my+guitar+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiKnRheWxvciBzd2lmdCB0ZWFyZHJvcHMgb24gbXkgZ3VpdGFyIGx5cmljc0j7LlCAEViALXAFeAGQAQCYAZABoAHBEKoBBDE1Lji4AQPIAQD4AQGYAhCgAucHwgIKEAAYsAMY1gQYR8ICDRAAGIAEGLADGEMYigXCAg4QABiwAxjkAhjWBNgBAcICExAuGIAEGLADGEMYyAMYigXYAQHCAgcQABiABBgNwgIGEAAYBxgewgIIEAAYBxgIGB7CAgoQABgHGAgYChgewgIIEAAYBxgKGB7CAgsQABiABBiGAxiKBcICCBAAGIAEGKIEwgIGEAAYCBgewgIIEAAYCBgKGB6YAwCIBgGQBhO6BgYIARABGAmSBwQxMy4zoAfs3QE&sclient=gws-wiz-serp")
place_response = requests.get ("https://www.google.com/search?q=taylor+swift+a+place+in+this+world+lyrics&sca_esv=dcbcef83952848e4&ei=H7UfZ5z9Ls-xptQPuPPP0Qk&ved=0ahUKEwjciPCLubGJAxXPmIkEHbj5M5oQ4dUDCA8&uact=5&oq=taylor+swift+a+plce+in+this+world+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiKHRheWxvciBzd2lmdCBhIHBsY2UgaW4gdGhpcyB3b3JsZCBseXJpY3MyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEcyBBAAGEdI3gFQAFgAcAB4ApABAJgBAKABAKoBALgBA8gBAJgCAaACBpgDAOIDBRIBMSBAiAYBkAYIkgcBMaAHAA&sclient=gws-wiz-serp")
cold_response = requests.get ("https://www.google.com/search?q=taylor+swift+cold+as+you+lyrics&sca_esv=dcbcef83952848e4&ei=JLUfZ8S8HJyIptQPpu2q-A4&ved=0ahUKEwjE3o6OubGJAxUchIkEHaa2Cu8Q4dUDCA8&uact=5&oq=taylor+swift+cold+as+you+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiH3RheWxvciBzd2lmdCBjb2xkIGFzIHlvdSBseXJpY3MyBhAAGAcYHjIGEAAYCBgeMgYQABgIGB4yCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMggQABiABBiiBEjiDlCQAliDDHABeAGQAQGYAe0CoAGFD6oBBzIuMi41LjG4AQPIAQD4AQGYAgKgAtQBmAMAiAYBkgcDMS4xoAeWRA&sclient=gws-wiz-serp")
outside_response = requests.get ("https://www.google.com/search?q=taylor+swift+the+oustide+lyrics&sca_esv=dcbcef83952848e4&ei=c7UfZ_reE6aZptQPyoT18AU&ved=0ahUKEwi65NuzubGJAxWmjIkEHUpCHV4Q4dUDCA8&uact=5&oq=taylor+swift+the+oustide+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiH3RheWxvciBzd2lmdCB0aGUgb3VzdGlkZSBseXJpY3MyBxAAGIAEGA0yCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTIIEAAYgAQYogQyCBAAGIAEGKIEMggQABiABBiiBEj8EFC8AVj4D3ABeAGQAQGYAXugAfAIqgEDOC41uAEDyAEA-AEBmAILoALcBsICChAAGLADGNYEGEfCAg0QABiABBiwAxhDGIoFwgIOEAAYsAMY5AIY1gTYAQHCAhYQLhiABBiwAxhDGNQCGMgDGIoF2AEBwgITEC4YgAQYsAMYQxjIAxiKBdgBAcICBhAAGAcYHsICDhAAGIAEGJECGLEDGIoFwgILEAAYgAQYkQIYigXCAgUQABiABMICCBAAGAcYChgewgIIEAAYBxgIGB7CAgoQIRigARjDBBgKmAMAiAYBkAYTugYGCAEQARgJkgcDOS4yoAelVA&sclient=gws-wiz-serp")
togethersmile_response = requests.get ("https://www.google.com/search?q=taylor+swift+tied+together+with+a+smile+lyrics&sca_esv=dcbcef83952848e4&ei=37UfZ7SMNIPdptQPsbnG6AU&oq=taylor+swift+tied++lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiGXRheWxvciBzd2lmdCB0aWVkICBseXJpY3MqAggAMgYQABgHGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB4yBhAAGAgYHjIGEAAYCBgeMgsQABiABBiGAxiKBUjjMVCsI1ibKXAAeASQAQCYAZgBoAG5A6oBAzIuMrgBAcgBAPgBAZgCB6AC4APCAgQQABhHwgIIEAAYBxgIGB6YAwDiAwUSATEgQIgGAZAGCJIHAzUuMqAH6iE&sclient=gws-wiz-serp")
staybeautiful_response = requests.get ("https://www.google.com/search?q=taylor+swift+stay+beautiful+lyrics&sca_esv=dcbcef83952848e4&ei=ALYfZ6ycN7CjptQP4djOwAM&oq=taylor+swifts+stay+beau+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiHnRheWxvciBzd2lmdHMgc3RheSBiZWF1IGx5cmljcyoCCAAyBxAAGIAEGA0yCBAAGAgYDRgeMggQABgIGA0YHjIIEAAYCBgNGB4yCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCBAAGIAEGKIEMggQABiABBiiBDIIEAAYgAQYogRIkiVQwAFYxB1wBXgBkAEAmAGSAaABywqqAQQxMS40uAEByAEA-AEBmAIOoALGBsICChAAGLADGNYEGEfCAg0QABiABBiwAxhDGIoFwgIOEAAYsAMY5AIY1gTYAQHCAhMQLhiABBiwAxhDGMgDGIoF2AEBwgIHEAAYgAQYCsICCBAAGAcYChgewgIKEAAYgAQYsQMYDcICChAAGAcYCBgKGB7CAgYQABgNGB7CAgoQIRigARjDBBgKmAMAiAYBkAYTugYGCAEQARgJkgcEMTEuM6AH-YIB&sclient=gws-wiz-serp")
shouldvesaidno_response = requests.get ("https://www.google.com/search?q=taylor+swift+shouldve+said+no+lyrics&sca_esv=dcbcef83952848e4&ei=MbYfZ42yEvaiptQP1oyc-AY&ved=0ahUKEwjNjqeOurGJAxV2kYkEHVYGB28Q4dUDCA8&uact=5&oq=taylor+swift+shouldve+said+no+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiJHRheWxvciBzd2lmdCBzaG91bGR2ZSBzYWlkIG5vIGx5cmljc0jBKlDaAVjwJXAEeAGQAQWYAYADoAGPHaoBCDQuMTcuMi4xuAEDyAEA-AEBmAIKoALbBcICCBAAGIAEGKIEwgIIEAAYCBgNGB7CAgoQABgIGAoYDRgewgILEAAYgAQYhgMYigXCAgoQABgFGAoYDRgemAMAiAYBkgcDNi40oAeWmwE&sclient=gws-wiz-serp")
marysong_response = requests.get ("https://www.google.com/search?sca_esv=dcbcef83952848e4&q=taylor+swift+mary%27s+song+lyrics&spell=1&sa=X&ved=2ahUKEwjw5_SpurGJAxXCrokEHd2kIR8QBSgAegQIChAB&biw=1440&bih=778&dpr=2")
oursong_response = requests.get ("https://www.google.com/search?q=taylor+swift+our+song+lyrics&sca_esv=dcbcef83952848e4&biw=1440&bih=778&ei=brYfZ7WjBpLdptQPg4C00AI&ved=0ahUKEwi1kqarurGJAxWSrokEHQMADSoQ4dUDCA8&uact=5&oq=taylor+swift+our+song+lyrics&gs_lp=Egxnd3Mtd2l6LXNlcnAiHHRheWxvciBzd2lmdCBvdXIgc29uZyBseXJpY3MyCxAAGIAEGJECGIoFMgYQABgHGB4yBRAAGIAEMggQABgHGAgYHjIKEAAYBxgIGAoYHjIEEAAYHjIEEAAYHjIEEAAYHjIEEAAYHjIGEAAYCBgeSKcKUKcCWPAHcAF4AZABAJgBvAKgAdENqgEHMC4zLjMuMrgBA8gBAPgBAZgCA6ACrwPCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICDhAAGLADGOQCGNYE2AEBwgITEC4YgAQYsAMYQxjIAxiKBdgBAcICFhAuGIAEGLADGEMY1AIYyAMYigXYAQGYAwCIBgGQBhO6BgYIARABGAmSBwcxLjEuMC4xoAf6Qw&sclient=gws-wiz-serp")


# print(response.text[:500])

tim_soup_html = BeautifulSoup(tim_response.text, "html.parser")
picture_soup_html = BeautifulSoup(picture_response.text, "html.parser")
teardrops_soup_html = BeautifulSoup(teardrops_response.text, "html.parser")
place_soup_html = BeautifulSoup(place_response.text, "html.parser")
cold_soup_html = BeautifulSoup(cold_response.text, "html.parser")
outside_soup_html = BeautifulSoup(outside_response.text, "html.parser")
togethersmile_soup_html = BeautifulSoup(togethersmile_response.text, "html.parser")
staybeautiful_soup_html = BeautifulSoup(staybeautiful_response.text, "html.parser")
shouldvesaidno_soup_html = BeautifulSoup(shouldvesaidno_response.text, "html.parser")
marysong_soup_html = BeautifulSoup(marysong_response.text, "html.parser")
oursong_soup_html = BeautifulSoup(oursong_response.text, "html.parser")



tim_soup_text = tim_soup_html.get_text()
picture_soup_text = picture_soup_html.get_text()
teardrops_soup_text = teardrops_soup_html.get_text()
place_soup_text = place_soup_html.get_text()
cold_soup_text = cold_soup_html.get_text()
outside_soup_text = outside_soup_html.get_text()
togethersmile_soup_text = togethersmile_soup_html.get_text()
staybeautiful_soup_text = staybeautiful_soup_html.get_text()
shouldvesaidno_soup_text = shouldvesaidno_soup_html.get_text()
marysong_soup_text = marysong_soup_html.get_text()
oursong_soup_text = oursong_soup_html.get_text()



tim_data = open('tim-mcgraw.txt', 'w')
tim_data.write(tim_soup_text)
tim_data.close()

picture_data = open('picture-to-burn.txt', 'w')
picture_data.write(picture_soup_text)
picture_data.close()

teardrops_data = open('teardrops-on-my-guitar.txt', 'w')
teardrops_data.write(teardrops_soup_text)
teardrops_data.close()

place_data = open('a-place-in-this-world.txt', 'w')
place_data.write(place_soup_text)
place_data.close()

cold_data = open('cold-as-you.txt', 'w')
cold_data.write(cold_soup_text)
cold_data.close()

outside_data = open('the-outside.txt', 'w')
outside_data.write(outside_soup_text)
outside_data.close()

togethersmile_data = open('tied-together-with-a-smile.txt', 'w')
togethersmile_data.write(togethersmile_soup_text)
togethersmile_data.close()

staybeautiful_data = open('stay-beautiful.txt', 'w')
staybeautiful_data.write(staybeautiful_soup_text)
staybeautiful_data.close()

shouldvesaidno_data = open('shouldve-said-no.txt', 'w')
shouldvesaidno_data.write(shouldvesaidno_soup_text)
shouldvesaidno_data.close()

marysong_data = open('marys-song.txt', 'w')
marysong_data.write(marysong_soup_text)
marysong_data.close()

oursong_data = open('our-song.txt', 'w')
oursong_data.write(oursong_soup_text)
oursong_data.close()


