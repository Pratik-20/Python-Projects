import pygeoip

gip = pygeoip.GeoIP("/storage/emulated/0/Python/GeoLiteCity.dat")
d=input(print("Enter IP adress:"))
res = gip.record_by_addr(d)

for key,val in res.items():
	print('%s : %s'%(key,val))

