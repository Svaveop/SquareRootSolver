from math import sqrt

A = 17;
print(f"The real value: {(sqrt(69)+1)/2}");

def f(x):
  return x ** 2 - A; # x^2-17

def bisaction(f, a, b, i=0):
  x0 = (a+b)/2; # [a; x0] & [x0; b]
  i+=1;
  if f(x0)==0:
    print(f"The number of itarations: {i}")
    return x0;
  else:
    if f(a)*f(x0)<=0:
      return bisaction(f, a, x0, i);
    elif f(x0)*f(b)<=0:
      return bisaction(f, x0, b, i);
    else:
      print(f"There is no square root in: {[a, b]} interval!");
print(f"The estimated value via bisection algotithm: {bisaction(f, 0, A)}");

def g(x):
  return sqrt(17+x);

def simple_itaration(g, x0, e=1e-16, N=1e+03):
  xn_1=x0;
  xn=g(xn_1);
  i=1;
  while abs(xn-xn_1)>e:
    xn_1=xn;
    xn=g(xn_1);
    i+=1;
    if i>N:
      print(f"There is no root for the {x0} initial point!");
      break;
  print(f"The number of itarations via simple itaration algorithm: {i}");
  return xn;
print(f"The estimated value via simple itaration algorithm: {simple_itaration(g, 0)}");

def Newton(f, df, x0, e=1e-16, N=1e+03):
  xn_1=x0;
  xn=xn_1-f(xn_1)/df(xn_1);
  i=1;
  while abs(xn-xn_1)>e:
    xn_1=xn;
    xn=xn_1-f(xn_1)/df(xn_1);
    i+=1;
    if i>N:
      print(f"There is no root for the {x0} initial point!");
      break;
  print(f"The number of iterations via Newton's method: {i}");
  return xn;
def df(x):
  return 2*x;
print(f"The estimated value via Newton's method: {Newton(f, df, 1)}");
