import random
import string


def generate_password():
	word = ''
	lst = []
	keep_password = string.ascii_letters + string.digits + string.punctuation
	for _ in range (random.randrange(16, 50)):
		lst.append(random.choice(keep_password))
	return ''.join(lst).strip()
		
	

print(generate_password())


