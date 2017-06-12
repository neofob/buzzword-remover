import time


def read_bs(filename):
	with open(filename) as _file:
		data = _file.readlines()
	return data


class NoBull(object):
	def __init__(self,text):
		"""
		"""
		self.buzzwords = set(read_bs('buzzwords'))  # Removing Uniques set()
		self.text = text
		#print self.text
		self.filtered_text = None
		self.bs = []
		print self.text.split(' ')

	def callbs(self):
		print "Calling bs..."
		text = self.text.lower()
		for buzzword in self.buzzwords:
			if buzzword.strip('\n') != '' and buzzword.strip('\n').strip().lower() in self.text:
				index = self.text.find(buzzword.strip('\n').strip().lower())
				sow = index
				eow = None
				while not eow:
					_char = self.text[index]
					print "Index [{0}], Char: [{1}]".format(index,_char)
					if _char in (' ',',','.'):
						eow = index
					index += 1
				found_word = self.text[sow:eow]
				print "Found {0} at [{1}][{2}][{3}]".format(buzzword.strip('\n'),sow,eow,found_word)
				self.bs.append((buzzword.strip('\n').strip().lower(),found_word))

	def stripbs(self):
		print "Stripping bs..."
		for buzzword in self.bs:
			for _string in buzzword:
				bull = True
				removed = 0
				while bull:
					bs_index = self.text.find(_string)
					print "bs_index = {0} : [{1}]".format(bs_index,_string)
					if bs_index < 0:
						bull = False
					else:
						removed += 1
						self.text = self.text[:bs_index] + self.text[bs_index+len(_string):]
					

		print "Done"

	def _print(self):
		print self.text

	def stf(self,filename):
		with open(filename,'w') as _file:
			_file.write(self.text)




def main():
	with open('sample_text.txt') as _file:
		data = _file.read()
	email = NoBull(data)
	email._print()
	email.callbs()
	email.stripbs()
	email._print()
	email.stf('result.txt')

if __name__ == '__main__':
	main()