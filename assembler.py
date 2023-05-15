register_num_list=[0,1,2,3,4,5,6]
def list_convert(s):
   k=[]
   ret=[]
   k.clear()
   ret.clear()
   k=s.split()
   for i in k:
       if i.strip()!="":
           ret.append(i.strip())
   return ret
