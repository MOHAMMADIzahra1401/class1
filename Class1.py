class Kasr:
    def __init__(self,s,m) :
        self.s=s
        self.m=m

    def show(self):
        print(self.s,"/",self.m)

    def zarb(self,f):
        result=Kasr(None,None)
        result.s=self.s*f.s
        result.m=self.m*f.m
        return result

    def sum(self,f):
        result=Kasr(None,None)
        result.s=(self.s*f.m)+(f.s*self.m)
        result.m=self.m*f.m
        return result

    def taghsim_kasr(self,f):
        result=Kasr(None,None)
        result.s=self.s*f.m
        result.m=self.m*f.s
        return result

    def tafrigh(self,f):
        result=Kasr(None,None)
        result.s=(self.s*f.m)-(f.s*self.m)
        result.m=self.m*f.m
        return result


    
f1=Kasr(1,5)
f2=Kasr(2,10)
f1.show()
f2.show()

result_z=f1.zarb(f2)
result_z.show()

result_j=f1.sum(f2)
result_j.show()

result_t=f1.taghsim_kasr(f2)
result_t.show()

result_m=f1.tafrigh(f2)
result_m.show()