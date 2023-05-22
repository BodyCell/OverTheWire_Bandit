import winsound, time, os, platform


def sound():

	for i in range(3): # Number of repeats
		
		for j in range(9): # Number of beeps
			
			winsound.MessageBeep(-3) # Sound played
		
		time.sleep(1) # How long between beeps
                
# sound()

################################################################################

## RSS Feed Reader ##

# import requests
# from bs4 import BeautifulSoup
# import lxml


# site = requests.get("https://realpython.com/atom.xml")

# soup = BeautifulSoup(site.content, 'xml')
# entries = soup.find_all('entry')

# for entry in entries:
# 	title = entry.title.text
# 	summary = entry.summary.text
# 	link = entry.link['href']

# 	print(f'Title: {title}\n\nSummary: {summary}\n\nLink of this entry: {link}\n\n---------------------------')


# def add_feed(url):
# 	response = requests.get(url, headers = "Defined")

# 	print(response)

# add_feed(site)

# def all_equal(x):
#     return x[n]==x[abs(n-1)] for n in x

# print(all_equal([1, 1, 1]))

# naive solution


# def double_letters(string):
#     for i in range(len(string) - 1):
#         letter1 = string[i]
#         letter2 = string[i+1]
#         if letter1 == letter2:
#             return True
#     return False

# shorter solution
# using a list comprehension, zip, and any
# def double_letters(string):
#     return any([a == b for a, b in zip(string, string[1:])])


# word = 'abcdefg'

# print(word[1:])


# for a, b in zip(word, word[1:3]):
# 	print(a,b)


# def duplicate_count(tester):
# 	test = sorted(tester.lower())
# 	new_list = set()
# 	for x, y in zip(test,test[1:]):
# 		print(x,y)
# 		if x == y:
# 			new_list.add(x)
# 	return len(new_list)

# print(duplicate_count(tester))

################################################## \/\/\/ CODE WARS \/\/\/ ##################################################

# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

# sequence = 'AAAABBBCCDAABBB'

# def unique_in_order(sequence):
# 	if len(sequence) > 0:
# 		new_seq = [sequence[0]]
# 		for x,y in enumerate(sequence[1:]):
# 			if y != sequence[x]:
# 				new_seq.append(y)
# 	else: return sequence
# 	return new_seq

# print(unique_in_order(sequence))


####################################################################################################

# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.
# Examples (Input --> Output)

# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

# pin = '1234'

# def validate_pin(pin):
# 	try:
# 		return (all(isinstance(int(x),int) for x in pin) if (len(pin)==6 or len(pin)==4) else False)
# 	except:
# 		return False

# print(validate_pin(pin))


####################################################################################################


# arr = [10,5,4,-9]

# INEFFICIENT (mistakenly assumed IndexError)
# def find_even_index(arr):
# 	if sum(arr[1:]) == 0:
# 		return 0
# 	else: 
# 		for x,y in enumerate(arr[1:]):
# 			if sum(arr[:x+1]) == sum(arr[x+2:]):
# 				return x+1
# 	return -1

# EFFICIENT EXAMPLE OF ABOVE
# def find_even_index(arr):
#     for i in range(len(arr)):
#         if sum(arr[:i]) == sum(arr[i+1:]):
#             return i
#     return -1

####################################################################################################


# names = ['Alex','John','Dave', 'Val', 'Peggy']

# INEFFICIENT (the naive code)
# def likes(names):
# 	if len(names) == 0:
# 		return "no one likes this"
# 	elif len(names) ==1:
# 		return " ".join((names[0],"likes this"))
# 	elif len(names) == 2:
# 		return "".join((" and ".join(names)," like this"))
# 	elif len(names) == 3:
# 		return f"{names[0]}, {' and '.join(names[1:])} like this"
# 	else:
# 		return f"{names[0]}, {names[1]} and {len(names[2:])} others like this"
	
# EFFICIENT EXAMPLE OF ABOVE
# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this', 
#         2: '{} and {} like this', 
#         3: '{}, {} and {} like this', 
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)

####################################################################################################

# Gausian


# INEFFICIENT (naive code)
# def sort_array(source_array):
# 	odds_only = []
# 	new_array = [x if not x %2 else odds_only.append(x) for x in source_array]
# 	for x in range(len(new_array)):
# 		if new_array[x] == None:
# 			new_array[x] = sorted(odds_only)[0]
# 			odds_only.remove(sorted(odds_only)[0])
# 	return new_array


# EFFICIENT EXAMPLE OF ABOVE
# def sort_array(arr):
#   odds = sorted((x for x in arr if x%2 != 0), reverse=True)
#   return [x if x%2==0 else odds.pop() for x in arr]

####################################################################################################


strarr = ["zone", "abigail", "theta", "abigail", "form", "libe", "zas"]
k = 2

def longest_consec(strarr, k):
	long = ""
	print(strarr,k)
	if (k >= len(strarr)) or (k <= 0):
		return ""
	for x in range(len(strarr)):
		if len("".join(strarr[x:x+k])) > len(long):
			long = "".join(strarr[x:x+k])
	return long


print(longest_consec(strarr,k))