def ArrayChallenge(strArr):
  # code goes here
  count=0
  string1 = strArr[0]
  string2 = strArr[1]

  for i in range(len(string1)):
    if string1[i] != string2[i]:
       print(string1[i])
       count += 1
       
  return count

def get_input():
  strArr = ["abcdef", "defabc"]
  return strArr  

# keep this function call here 
print(ArrayChallenge(get_input()))