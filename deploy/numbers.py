#perfect number
n = 6;
sum = 0;
for i in range(1, int(n /2) + 1):
  if n%i == 0:
    sum = sum + i;
print(sum);
if sum == n:
  print("Perfect");
else:
  print("Not perfect");


#palindrome
n = 372
s = 0;
r = 0;
i = n;

while i > 0:
  r = i % 10;
  s = s * 10 + r;
  i = i // 10;
  print(i);
print(s);
if n == s:
  print("palindrome");
else:
  print("not palindrome");

#sort
nums =[21,1,2,12];
for i in range(len(nums) - 1):
  if nums[i] > nums[i + 1]:
    temp = nums[i];
    nums[i] = nums[i + 1];
    nums[i + 1] = temp;

    i = -1;
print(nums);
print((nums[1] + nums[-2]) / 2);

#find largest

def find_largest(nums ,s):
  max_num = 0;
  for  n in nums:
    if n > max_num:
      max_num = n;
  return max_num;
nums =[5,4,9,8,12];
largest = find_largest(nums,len(nums));
print(largest)

# find three largest
def three_largest(nums,n):
  first = second = third = 0;
  for num in nums:
    if num > first:
      third = second;
      second = first;
      first = num;
    elif num > second:
      third = second;
      second = num;
    elif num > third:
      third = num;
  print(first,second,third);
three_largest(nums,len(nums));

#second largest
def three_largest(nums,n):
  first = second = third = 0;
  for num in nums:
    if num > first:
      second = first;
      first = num;
    elif num > second:
      second = num;
  print(second);
three_largest(nums,len(nums));

#second smallest
def three_largest(nums,n):
  first = second = third = nums[0];
  for num in nums:
    if num < first:
      second = first; # 5
      first = num; # 4
    elif num < second:
      second = num;
  print(second);
three_largest(nums,len(nums));


#most occuring
def most_frequent(lst):
  counter = 0;
  max_count = lst[0];
  for i in lst:
    counts = lst.count(i);
    if counts > counter:
      counter = counts;
      max_count = i;
  return max_count;  
lst = [1,2,2,2,3,3,1];
print(most_frequent(lst));



def find_largest(nums ,s):
  max_num = '';
  for  n in nums:
    if n > max_num:
      max_num = n;
  return max_num;
str_lst ='abcdfag';
largest = find_largest(str_lst,len(str_lst));
print(largest)

# find three largest
def three_largest(nums,n):
  first = second = third = nums[0];
  for num in nums:
    if num < first:
      third = second;
      second = first;
      first = num;
    elif num < second:
      third = second;
      second = num;
    elif num < third:
      third = num;
  print(first,second,third);
three_largest(str_lst,len(str_lst));

#update mul
def update_every(nums,n):
  prev_elem = nums[0];
  nums[0]  = prev_elem * nums[1];
  for i in range(1,n - 1):
    curr_elem = nums[i];
    nums[i] = prev_elem * nums[i+1];
    prev_elem = curr_elem;
  nums[-1] = nums[-1] * prev_elem;

  for i in nums:
    print(i);

update_every(nums,len(nums));


#palindrome
string = "abc";
string2 ='';
for i in range(len(string) -1, -1 , -1):
  string2 = string2 + string[i];
if string2 == string:
  print("Palindrome");
else:
  print('Not palinmdrome');

#Find the numbers in a given string and calculate the sum of all numbers

string ="we2011";
string2 = "";
sum = 0;
for word in string:
  if ord(word) >= 48 and ord(word) <= 57:
    string2 = string2 + word;
    sum = sum + int(word);
print(string2 , sum);