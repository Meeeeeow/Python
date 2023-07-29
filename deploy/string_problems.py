#  find the length of a string without using library function. 

string = input("Enter something: ");
length = 0;
for word in string:
  length += 1;

print(length);

# separate the individual characters from a string.

print(' '.join([word for word in string]));

#print individual characters of string in reverse order.
print(' '.join([word for word in string[::-1]]));

#count the total number of words in a string
print(string.count(' ') + 1);

#compare two strings without using string library functions.
string1 = input("enter another string: ");
print("Are equal " if string == string1 else "Are not equal");

#count total number of alphabets, digits and special characters in a string.

import re;
x = re.findall("[a-zA-Z]",string);
y = re.findall("[0-9]",string);
z = len(string) - (len(x) + len(y));
print(f"alphabets are: {len(x)} and numbers are {len(y)} and special characters are {z} ")

#copy one string to another string.
string3 = string;
print(string3);

#count total number of vowel or consonant in a string.
pattern = "[^aeiou]";
x = re.findall("[a-zA-Z]",string1);
string2 = ''.join([w for w in x]);
print(string2);
y = re.findall(pattern,string2);
print(f"vowels are {len(string2) - len(y)} and consonants are {len(y)}");

# find maximum occurring character in a string
max_count= string.count(string[0]);
w = string[0];
for word in string:
  if word == ' ':
    pass;
  else:
    a = string.count(word);
    if a > max_count:
      max_count = a;
      w = word;
print(w , max_count);

#sort a string array in ascending order. 
string4 = input("Enter a string: ");
print(''.join([str(i) for i in sorted(string4)]));

str5 = "";
string4=list(string4);
for i in range(len(string4)):
  for j in range(len(string4) - (i+1)):
    if string4[j] > string4[j + 1]:
      temp = string4[j];
      string4[j] = string4[j + 1];
      string4[j+1] = temp;
print(''.join([i for i in string4]));

#read a string through keyboard and sort it using bubble sort.
n = int(input("Enter options: "));
str_list = list(input() for i in range(n));
print(str_list);

for i in range(len(str_list)):
  for j in range(len(str_list) - (i + 1)):
    if str_list[j] > str_list[j + 1]:
      temp = str_list[j];
      str_list[j] = str_list[j+1];
      str_list[j+1] = temp;
print('\n'.join([i for i in str_list]));

string5 = input("Enter string: ");
#extract a substring from a given string.
start_pos = int(input());
sub_length = int(input());
print(string5[start_pos:start_pos + sub_length]);
print(string5[9:13]);

#check whether a given substring is present in the given string.
sub_search = input("Substring to search: ");
if sub_search in string5:
  print(f"Present in {string5.index(sub_search)}");
else:
  print("Not Present");

#read a sentence and replace lowercase characters by uppercase and vice-versa

for word in string5:
  if word.islower():
    word = word.upper();
  else:
    word = word.lower();
  str5 = str5 + word;
print(str5);
print(string5);

#find the number of times a given word 'the' appears in the given string.

string6 = input();
print(string6.lower().count('the'));

#remove characters in String Except Alphabets
import re;
x =re.findall("[a-zA-Z]",string6);
print(''.join([i for i in x]));

#Find the Frequency of Characters. 
character = input('What character to find: ');
print(string6.lower().count(character));

#Concatenate Two Strings Manually.
str1 = input();
str2 = input();
print(str1 + ' ' + str2);

#find the largest and smallest word in a string
str7 ="";
def take_len(elem):
  return len(elem);
for word in string6:
  if word == ' ':
    pass;
  else:
    str7  = str7 + word;
sorted_str = sorted(x,key = take_len);
print(sorted_str)


