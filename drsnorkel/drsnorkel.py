import os
import logging
import argparse
from typing import List

import pandas as pd
from pandas import DataFrame

from snorkel.labeling import PandasLFApplier

from drsnorkel.labelling.labelling_functions import metamap
from drsnorkel.utils.data_utils import process_i2b2_2010

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

	def label_with_metamap(self, sent):
		"""
		Direct access to metamap labelling function
		"""
		return metamap(sent)

	def label_with_scispacy(self, model): # pass a scispacy model (e.g. en-core-sci-md)
		pass

	def process_i2b2_2010(self, root_data_dir: str, data_output_dir: str) -> None: 
		process_i2b2_2010(root_data_dir, data_output_dir)

	def apply_metamap(self, dataset: DataFrame): 
		"""
		Apply metamap to a list of sentences
		"""
		train_data = dataset.loc[dataset["split"] == "train"]
		test_data = dataset.loc[dataset["split"] == "test"]

		applier = applier = PandasLFApplier(lfs=[metamap])

		metamap_train = applier.apply(df=train_data)
		metamap_test = applier.apply(df=test_data)

		
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Main DrSnorkel parser')
	
	parser.add_argument('--process_i2b2_2010', action="store_true", help="Set flag to process i2b2_2010. Writes 'processed_i2b2b_2010.csv' to 'data_output_dir")
	parser.add_argument('--metamap_dir', type=str, default="/Users/nicolasahar/Projects/repos/public_mm/bin/metamap18", help='Absolute path to metamamp dir. Note: path MUST be absolute or pymetamap will error out.')
	parser.add_argument('--root_data_dir', type=str, default="./data", help='Relative path to root data dir')
	parser.add_argument('--data_output_dir', type=str, default="./data/processed", help='Relative path to output data dir')
	parser.add_argument('--i2b2_2010_file_name', type=str, default="process_i2b2_2010.csv", help='Name of the processed i2b2 2010 dataset created by the process_i2b2_2010 in the DrSnorkel class')
	
	args = parser.parse_args()
	
	dr_snorkel = DrSnorkel()

	if args.process_i2b2_2010: # Process i2b2-2010 if not already done
		dr_snorkel.process_i2b2_2010(args.root_data_dir, args.data_output_dir)

	# Load the i2b2b 2010 dataset
	dataset_path = os.path.join(args.data_output_dir, args.i2b2_2010_file_name)
	i2b2_2010_dataset = pd.read_csv(dataset_path)

	# Apply our metamap LF to the i2b2b 2010 dataset
	dr_snorkel.apply_metamap(i2b2_2010_dataset)

	import pdb; pdb.set_trace()




