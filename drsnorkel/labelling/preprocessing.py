from pymetamap import MetaMap

from snorkel.preprocess import Preprocessor
from snorkel.types import FieldMap

class MetaMapPreprocessor(Preprocessor):
	'''
	Preprocessor that uses a metamap instance to extract CUIs from a given datapoint (sentence)

	Parameters
	----------
	field_names
		Name of data point text field to input (v) mapped to input argument of the run method (k)
	mapped_field_names
		Name of data point field to output parsed document to (k) keyed by output key of run method (k)

	Notes
	-----
	- Preprocessor is a subclass of mapper (https://snorkel.readthedocs.io/en/v0.9.3/packages/_autosummary/map/snorkel.map.Mapper.html#snorkel.map.Mapper)
	- A Mapper maps an data point to a new data point, possibly with
	a different schema. Subclasses of Mapper need to implement the
	``run`` method, which takes fields of the data point as input
	and outputs new fields for the mapped data point as a dictionary.
	The ``run`` method should only be called internally by the ``Mapper``
	object, not directly by a user.
	- See this for working example: https://github.com/snorkel-team/snorkel/blob/master/snorkel/preprocess/nlp.py
	'''
	def __init__(self,  
		field_names={"sent": "sent"}, 
		mapped_field_names={"cui": "cui"} 
	) -> None:

		name = type(self).__name__ # check what this outputs
		super().__init__(
			name, 
			field_names=field_names, 
			mapped_field_names=mapped_field_names
		)

		metamap_dir = "/Users/nicolasahar/Projects/repos/public_mm/bin/metamap18"
		self.mm = MetaMap.get_instance(metamap_dir) # import metamap: (should point to the public_mm_lite folder which contains metamaplite.sh)
		self.cui_indices = get_cui_indices("./data/raw/cui/all_cuis_conso.csv")
	
	def run(self, sent: str=None) -> FieldMap:
		"""Run the metamap cui extractor on input sentence.
		
		Parameters
		----------
		sent
			Sentence of document to parse
		
		Returns
		-------
		FieldMap
			Dictionary with a single key (``"cui"``), mapping to the
			first cui returned by metamap
		"""
		concepts, error = self.mm.extract_concepts([sent.sent], [1])

		if concepts:
			cui = concepts[0].cui # get only the first cui
			
		else:
			cui = None
		
		return {"cui": cui}
