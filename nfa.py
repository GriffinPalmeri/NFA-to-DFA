import dfa # imports your DFA class from pa1
from collections import deque


class FileFormatError(Exception):
	"""
	Exception that is raised if the 
	input file to the DFA constructor
	is incorrectly formatted.
	"""
	pass

class NFA:
	""" Simulates an NFA """

	def __init__(self, nfa_filename):
		"""
		Initializes NFA from the file whose name is
		nfa_filename.  (So you should create an internal representation
		of the nfa.)
		"""

		f = open(nfa_filename,'r')
        #get the number of states
		self.num_states =int(f.readline().strip())
        
        #get the alphabet
        #use the unpack (*) method to split the string read into a list
		self.alphabet = [*f.readline().strip()]		
		self.transition_dict = {}

		line = f.readline().strip().split()
		while(len(line) != 0):
			current_state = line[0]
			#if the current state is more than number of states raise file format error
			character = line[1]
			#solve quote problem
			character = character.replace("'","")
			#if character is not in alphabet raise exception
			if(character not in self.alphabet):
				raise FileFormatError
			next_state = line[2]
			#if state is negative then raise exception
			if(int(next_state)<0):
				raise FileFormatError
			#set dictionary

			try:
				self.transition_dict[current_state,character]
			except KeyError:
				self.transition_dict[current_state,character] = []

			self.transition_dict[current_state,character].append(next_state)
			line = f.readline().strip().split()
		
		#now get the start state from the second to last line in file
		self.start_state =f.readline().strip()
		#if len of start state is not == 1 then it is an invalid file
		if(len(self.start_state.split())!=1):
			raise FileFormatError
		#if start state is larger than num states then it is invalid
		if(int(self.start_state)>int(self.num_states)):
			raise FileFormatError

		#get list of states
		self.accept_states = f.readline().strip().split()
		try:
			#if one of the accept states is not an integer then raise exception
			for state in self.accept_states:
				int(state)
		except ValueError:
			raise FileFormatError

		#if there is still a line than it is extra content and thus invalid
		if(f.readline()!=''):
			raise FileFormatError

        




	def to_DFA(self):
		"""
		Converts the "self" NFA into an equivalent DFA object
		and returns that DFA.  The DFA object should be an
		instance of the DFA class that you defined in pa1. 
		The attributes (instance variables) of the DFA must conform to 
		the requirements laid out in the pa2 problem statement (and that are the same
		as the DFA file requirements specified in the pa1 problem statement).

		This function should not read in the NFA file again.  It should
		create the DFA from the internal representation of the NFA that you 
		created in __init__.
		"""	
		#define dfa to return
		new_dfa = dfa.DFA()
		all_states = {}
		state_queue = deque()
		new_dfa.start_state = self.start_state
		new_dfa.alphabet =  self.alphabet
		
		#define DFA
		#enque start state
		start_state_set = set()
		start_state_set.add(new_dfa.start_state)
		state_queue.append(start_state_set)

		#determine data structure to hold dfa
		"""
		in dfa now:
		self.transition_dict[(current_State,character)] = next_State

		new_dfa.transition_dict[(set_of_states,character)] = next_State



		state 1
		state 1,2

		1,2,3

		mapping_dict = {1:[1] , 2:[1,2] , 3:[1,2,3]}
		"""
		counter = 1
		while(len(state_queue)!=0):
			current_state = state_queue.popleft()
			#loop over ever character in alphabet for current state
			for character in new_dfa.alphabet:
				new_dfa.transition_dict[counter,character] = self.transition_dict[(current_state,character)]
				#new_dfa.transition_dict[(current_state,character)] = 
			counter+=1

		#define accept states
		#looping 
		
		print()

		






	

	
if __name__ == "__main__":
	nfa = NFA("nfa2.txt")
	nfa.to_DFA()
	print("")
