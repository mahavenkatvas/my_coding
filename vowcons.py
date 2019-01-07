s=input()
if s.isalpha():
  l=['a','e','i','o','u','A','E','I','O','U']
  if s in l:
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
