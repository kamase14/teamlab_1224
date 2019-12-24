import urllib.request as req
import urllib.error as err
import time
import itertools

def query(url):
	res = req.urlopen(url)
	return res.read()

token = "GgoqAQz5LwRodUwNqAehvcUvgtoSMO1v"


string = list(itertools.product('ABCD',repeat=5))
print(string)
dict = {}

print("[")
for i in string:
	print("'" + ''.join(i) + "'",end=',')
print("]")

for i in string:
	moge    = ''.join(i)
	url    = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, moge)
	result = query(url)
	dict[moge] = int(result)

	print(str(moge) + ":"+ str(result))

	time.sleep(1)

sorted_dict = sorted(dict.items(),reverse=True,key=lambda x:x[1])
print(sorted_dict)
ans = ""

for i in sorted_dict:
	ans += str(i[0])
	print(ans)
	url    = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, ans)
	result = query(url)
	time.sleep(1)

	print(result)
	if(len(ans) >= 51):
		break
