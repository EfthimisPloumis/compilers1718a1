"""
Sample script to test ad-hoc scanning by table drive.
This accepts "term","test" and "long" words.
"""

def getchar(words,pos):
	""" returns char at pos of words, or None if out of bounds """

	if pos<0 or pos>=len(words): return None
	c = words[pos]
	if c>='0' and c<='9':
		return c
	if c==':' or c=='.':
		return 'sep'      
	return 'OTHER'

def scan(text,transition_table,accept_states):
	""" Scans `text` while transitions exist in 'transition_table'.
	After that, if in a state belonging to `accept_states`,
	returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 'q0'
	
	while True:
		
		c = getchar(text,pos)	# get next char
		
		if state in transition_table and c in transition_table[state]:
			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char
		
		else:	# no transition found		
		
			# check if current state is accepting
			if state in accept_states:
				return accept_states[state],pos

			# current state is not accepting
			return 'ERROR_TOKEN',pos
			
	
# the transition table, as a dictionary
td = { 'q0':{ '0':'q1','1':'q1','2':'q2','3':'q3','4':'q3','5':'q3','6':'q3','7':'q3','8':'q3','9':'q3'},
       'q1':{ '0':'q3','1':'q3','2':'q3','3':'q3','4':'q3','5':'q3','6':'q3','7':'q3','8':'q3','9':'q3','sep':'q4'},
       'q2':{ '0':'q3','1':'q3','2':'q3','3':'q3','4':'q3','sep':'q4'},
       'q3':{ 'sep':'q4'},
       'q4':{ '0':'q5','1':'q5','2':'q5','3':'q5','4':'q5','5':'q5'},
       'q5':{ '0':'q6','1':'q6','2':'q6','3':'q6','4':'q6','5':'q6','6':'q6','7':'q6','8':'q6','9':'q6'},
       'q6':{ None:'q9f','sep':'q7'},
       'q7':{ '0':'q8','1':'q8','2':'q8','3':'q8','4':'q8','5':'q8'},
       'q8':{ '0':'q9f','1':'q9f','2':'q9f','3':'q9f','4':'q9f','5':'q9f','6':'q9f','7':'q9f','8':'q9f','9':'q9f'},
       } 

# the dictionary of accepting states and their
# corresponding token
ad = { 'q9f':'TIME_TOKEN' }


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:	# that is, while len(text)>0

	# get next token and position after last char recognized
	token,position = scan(text,td,ad)
	
	if token=='ERROR_TOKEN':
		print('unrecognized input at pos',position,'of',text)
		break
		
	print("token:",token,"string:",text[:position])
	
	# remaining text for next scan
	text = text[position:]
	
