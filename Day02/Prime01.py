def isPrime(num):
  
  # check for number = 1
  if num==1:
    return False
    # check for 2 and 3
  if num<=3:
    return True # 2,3 are primes

  PrimeOrNot = True
 # print(f"{num} is under check for prime")
  for i in range(2, num-1):

    if num%i == 0:
      #print(f"{i} is dividing",{num})
      PrimeOrNot = False
      break

  if PrimeOrNot:
    #print(f"{num} from function os TRUE")
    return True
  else:
    #print(f"{num} from function os FALSE")
    return False


# teating
def main():
    nums = [1,2,3,5,7,93,107,1123,3197,4000]
    for i in nums:
        if isPrime(i):
            print(f"{i} is a prime number")
        else:
            print(f"{i} is not a prime number")

if __name__ == "__main__":
  main()