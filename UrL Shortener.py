import pyshorteners
Link= input('Enter Long URL')
s = pyshorteners.Shortener()
print("Here is Short URL")
print(s.tinyurl.short(Link))