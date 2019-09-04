import requests
import sys

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}
try:
    if sys.argv[1] != "":
        try:
            with open(sys.argv[1]) as f:
                for line in f.readlines():
                    line = line.strip()
                    url = 'http://' + line
                    try:
                        response = requests.get(url, headers=header, timeout=1)
                        if 'safedog' not in response.headers['Set-Cookie']:
                            print "[+] No dog: " + line
                            with open('nodog.txt','a+') as g:
                                g.write(line + "\n")
                        else:
                            print "[-] Have dog: " + line
                    except Exception as e:
                        continue
        except Exception as e:
            print "Fail path!"

except Exception as e:
    print "Usge: " + sys.argv[0] + " url.txt"
