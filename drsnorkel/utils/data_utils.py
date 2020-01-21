"""
Data needs to be loaded into pandas dataframes (preferred) for snorkel.
"""
import os
import pandas as pd 

from tqdm import tqdm

import spacy

nlp = spacy.load("en_core_sci_md")

def process_i2b2_2010(root_data_dir: str, output_dir: str) -> None:

    # Setup paths
    common_data_path = os.path.join(root_data_dir, "raw/i2b2-2010")
    
    path_dict = {
        "train_beth_path": os.path.join(common_data_path, "concept_assertion_relation_training_data/beth/txt"),
        "train_partners_path_txt": os.path.join(common_data_path, "concept_assertion_relation_training_data/partners/txt"),
        "train_partners_path_unnanotated": os.path.join(common_data_path, "concept_assertion_relation_training_data/partners/unannotated"),
        "test_data_path": os.path.join(common_data_path, "test_data")
    }
    columns = ["note_id", "sent_num", "sent", "sent_span_start", "sent_span_end", "split", "source"]
    merged_df = pd.DataFrame(columns=columns)

    row_list = [] # Keep all rows in here before appending to df as iterative appending is expensive (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html)

    for entry, path in path_dict.items():
        files = os.listdir(path)

        for note_name in tqdm(files, desc=f"Processing {entry}", unit="file"): 
            if note_name == ".DS_Store":
                continue 

            file_path = os.path.join(path, note_name)
            text = open(file_path, "r").read()
            
            spacy_text = nlp(text)
            sents = [(sent_num, sent) for sent_num, sent in enumerate(spacy_text.sents)]

            for sent in sents: 
                row_dict = {
                    "note_id": note_name,
                    "sent_num": sent[0],
                    "sent": str(sent[1]),
                    "sent_span_start": sent[1].start,
                    "sent_span_end": sent[1].end,
                    "split": "train" if entry[:5] == "train" else "test",
                    "source": entry
                }

                row_list.append(row_dict)

    merged_df = merged_df.append(row_list)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_name = os.path.join(output_dir, "process_i2b2_2010.csv")
    
    merged_df.to_csv(file_name, index=False)


        