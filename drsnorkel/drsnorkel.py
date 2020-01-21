import os
import logging
import argparse
from typing import List

from drsnorkel.labelling.labelling_functions import metamap

logger = logging.getLogger(__name__)
logging.basicConfig(level=20)


class DrSnorkel():
	"""
	Main entry into DrSnorkel

	Notes
	-----
	"""
	def __init__(self) -> None:
		pass

	def label_with_metamap(self, sent: List):
		
		return metamap(sent)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='DrSnorkel main parser')
	
	# Preprocessing settings
	parser.add_argument('--metamap_dir', type=str, default="/Users/nicolasahar/Projects/repos/public_mm/bin/metamap18", help='Absolute path to metamamp dir. Note: path MUST be absolute or pymetamap will error out.')

	args = parser.parse_args()
	
	sent = ['Heart Attack']

	test_snorkel = DrSnorkel()

	concept = test_snorkel.label_with_metamap(sent)

	import pdb; pdb.set_trace()





