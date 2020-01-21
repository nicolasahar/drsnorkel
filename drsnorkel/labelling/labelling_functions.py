from typing import List

from pymetamap import MetaMap

from snorkel.labeling import labeling_function


@labeling_function()
def metamap(sent: List):
	metamap_dir = "/Users/nicolasahar/Projects/repos/public_mm/bin/metamap18"

	mm = MetaMap.get_instance(metamap_dir) # import metamap: (should point to the public_mm_lite folder which contains metamaplite.sh)

	concepts, error = mm.extract_concepts(sent, [1]) # can only pass in one sentence at a time to snorkel!

	if concepts:
		return concepts[0].cui

	else:
		return 0