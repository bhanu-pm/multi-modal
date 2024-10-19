import re
import copy


class SimpleTokenizer:
	def __init__(self, main_vocab_dict):
		if '<unk>' not in main_vocab_dict.keys(): 
			main_vocab_dict['<unk>'] = len(main_vocab_dict.keys())
		if '<|endoftext|>' not in main_vocab_dict.keys():
			main_vocab_dict['<|endoftext|>'] = len(main_vocab_dict.keys())
		self.str_to_int = main_vocab_dict
		self.int_to_str = {i:s for s, i in self.str_to_int.items()}
		
	def encoder(self, text):
		# Creating a token list for given text
		if re.search('(<\|endoftext\|>)', text):
			pass
		else:
			text = text + "<|endoftext|>"
		
		self.result = re.split('([\s_:;\'"\-!?,.&%]|<\|endoftext\|>)', text)
		self.tokens = [i.lower().strip() for i in self.result if i.strip() != '']

		self.token_ids = []
		for i, tok in enumerate(self.tokens):
			if tok in self.str_to_int.keys():
				val = self.str_to_int[tok]
			elif tok not in self.str_to_int.keys():
				val = self.str_to_int['<unk>']
			self.token_ids.append(val)

		return self.token_ids

	def decoder(self, integers):
		# Getting back the text from token IDs
		text_list = []
		for val in integers:
			word = self.int_to_str[val]
			text_list.append(word)

		unparsed_text_list = copy.deepcopy(text_list)
		unparsed_text_list.remove('<|endoftext|>')

		unparsed_final_text = ' '.join(unparsed_text_list)
		parsed_final_text = ' '.join(text_list)
		return unparsed_final_text, parsed_final_text



if __name__ == '__main__':
	text = "Thy The thee :;quick & 'brown' fox -jumps!? over, %the \"lazy\" dawg."
	tokens_to_int = {'!': 0, '"': 1, '%': 2, '&': 3, "'": 4, ',': 5, '-': 6, '.': 7, ':': 8, ';': 9, '?': 10, 'brown': 11, 'dawg': 12, 'fox': 13, 'jumps': 14, 'lazy': 15, 'over': 16, 'quick': 17, 'the': 18}
	tokenizer = SimpleTokenizer(tokens_to_int)
	token_ids_for_text = tokenizer.encoder(text)
	print("Initial text :")
	print(text)
	print(token_ids_for_text)

	rawtext_from_token_ids, text_from_token_ids = tokenizer.decoder(token_ids_for_text)
	print(rawtext_from_token_ids)
	print(text_from_token_ids)