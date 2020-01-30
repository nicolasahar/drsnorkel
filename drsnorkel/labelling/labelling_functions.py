from typing import List

import scispacy
from scispacy.umls_linking import UmlsEntityLinker

from pymetamap import MetaMap

from snorkel.labeling import labeling_function
from drsnorkel.utils.data_utils import get_cui_indices


@labeling_function()
def metamap(sent, metamap=None):
	"""
	Notes
	-----
	- This is too slow because we instantiate mm and get_cui_indices for every datapoint - find a way around this
	"""
	metamap_dir = "/Users/nicolasahar/Projects/repos/public_mm/bin/metamap18"
	mm = MetaMap.get_instance(metamap_dir) # import metamap: (should point to the public_mm_lite folder which contains metamaplite.sh)

	cui_indices = get_cui_indices("./data/raw/cui/all_cuis_conso.csv")
	concepts, error = mm.extract_concepts([sent.sent], [1]) # can only pass in one sentence at a time to snorkel!

	if concepts:
		if float(concepts[0].score) < 1: # abstain if score < 1 
			return -1 

		cui = concepts[0].cui

		if cui in cui_indices["CUI"]:
			cui_index = (list(cui_indices["CUI"].keys())[list(cui_indices["CUI"].values()).index(cui)])
			return cui_index + 1 # To avoid assigning index 0 a label of 0

		return -1
	
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