class complex_number:
    def _init_(self,real,img):
        self.real=real
        self.img=img
    def _str_(self):
        return f"{self.real+self.img}i"
    def add(self,other):
        real_sum=self.real+other.real
        img_sum=self.img+other.img
        return complex_number(real_sum,img_sum)
    def sub(self,other):
        real_diff=self.real-other.real
        img_diff=self.img-other.img
        return complex_number(real_diff,img_diff)
    def mul(self,other):
        real_prod=(self.real*other.real)-(self.img*other.img)
        img_prod=(self.real*other.img)+(self.img*other.real)
        return complex_number(real_prod,img_prod)
real1=float(input("enter the real part of the first complex number:"))
img1=float(input("enter the imaginary part of the first complex number:"))
real=float(input("enter the real part of the second complex number:"))
img1=float(input("enter the imaginary part of the first complex number:"))
#create objects
complex_num1=complex_number(real1,img1)
complex_num2=complex_number(real2,img2)
#operations
sum=complex_num1.add(complex_num2)
difference=complex_num1.sub(complex_num2)
product=complex_num1.mul(complex_num2)
#display
print("sum:",sum)
print("difference:",difference)
print("product:",product)

        
    
        
