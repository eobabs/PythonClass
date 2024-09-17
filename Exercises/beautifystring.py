def put_full_stop(any_word):

	if not any_word.endswith('.'):
		any_word += '.'
	return any_word



def capitalize_casing(any_word):
	if any_word:
		any_word = any_word[0].upper() + any_word[1:]
	return any_word


def beautify_string(any_word):
	any_word = put_full_stop(any_word)
	any_word = capitalize_casing(any_word)
	return any_word


type_words = input('Enter any sentence ')
print ("The beautified string is ", beautify_string(type_words))