class Time:
    def __init__(self,h,m,s):
        self.s=s
        self.m=m
        self.h=h
    def show(self):
        print(self.h,":",self.m,":",self.s)

    def z_to_s(self):
        result=(self.h*3600)+(self.m*60)+(self.s)
        return result
    
    def s_to_z(self,f):
        self.h = f// 3600
        f=f-(self.h*3600)
        self.m=f//60
        f=f-(self.m*60)
        self.s=f

time=Time(2,24,30)

f=4600
t=Time(None,None,None)
t.s_to_z(f)
t.show()
result=time.z_to_s()
print( "result:",result,"saneieh")