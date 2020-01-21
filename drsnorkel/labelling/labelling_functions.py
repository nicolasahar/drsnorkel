from typing import List

import scispacy
from scispacy.umls_linking import UmlsEntityLinker

from pymetamap import MetaMap

from snorkel.labeling import labeling_function

@labeling_function()
def metamap(sent):
	metamap_dir = "/Users/nicolasahar/Projects/repos/public_mm/bin/metamap18"

	mm = MetaMap.get_instance(metamap_dir) # import metamap: (should point to the public_mm_lite folder which contains metamaplite.sh)

	concepts, error = mm.extract_concepts([sent.sent], [1]) # can only pass in one sentence at a time to snorkel!

	if concepts:
		if float(concepts[0].score) < 1: # abstain if score < 1 
			return -1 

		return concepts[0].cui

	else:
		return 0

@labeling_function()
def scispacy_el(sent: str):
	"""
	Test this code! 
	"""
	linker = UmlsEntityLinker(resolve_abbreviations=True)	
	nlp.add_pipe(linker)

	doc = nlp(sent)

	entities = doc.ents
	
	import pdb; pdb.set_trace() 