print("\033[0;37;1;0mWhat base do you want to add? (2-64)\n"); base=input(); j=0; q="a"; array = [0,0,0]; z=100000000000000; c=100000000000; v=z*c; strh = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"; mod2 = ""
if base.isdigit()==False or int(base) > 63 or int(base) < 2: base=64; print("\nBase 64 it is!"); strh = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
while j < 3:
  if j == 0 or j==1: print("\n\033[0;37;1;33m Please enter", q, "positive integer (in base 10): \n"); number = input(); i=1; binary = ""; base=int(base)
  if j == 2: number = (array[0]+array[1]); i=1; binary=str(""); number=str(number)
  if number.isdigit() == True: number = (int(number)); q="another"; array[j] = number
  else: print("\n   That's not an integer!"); continue
  while number > 0 and number < v*100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000: mod = number % base; number = number // base; mod2=strh[mod]; binary = mod2 + binary
  print("\033[0;37;1;32m"); n = binary; j+=1; print(binary)