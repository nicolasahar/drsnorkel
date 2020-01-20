
from pymetamap import MetaMapLite

from snorkel.labeling import labeling_function


@labeling_function()
def metamap_labels(x):

	# import metamap: (should point to the public_mm_lite folder which contains metamaplite.sh)
	mm = MetaMapLite.get_instance('/opt/public_mm_lite_3.6.2rc3/')

	# get the concepts
	concepts, errors = mm.extract_concepts(x)
