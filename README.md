# DrSnorkel
A package for programmatically building clinical training data via weak supervision through Snorkel

# Installation 

- Install metamap from [here](https://metamap.nlm.nih.gov/MainDownload.shtml).
- Install [pymetamap](https://github.com/AnthonyMRios/pymetamap/blob/master/pymetamap/MetaMapLite.py?fbclid=IwAR2xqL2RzAV70IoFO15N0UgNkR9BeSZAqIPOLwxhBRXZ985J6n41f8YujW0).
- In a terminal session, navigate to the directory where the metamap bin is, and start the metamap tagger server with `./bin/skrmedpostctl start`

# Useful resources
- [Guide](https://metamap.nlm.nih.gov/Docs/MM12_XML_Info.shtml?fbclid=IwAR16ssLjJad6eZPAjliOC4L1m9xQAsCz9bDpW2ppi3te32b52Fd7yB5tXEI) to metamap output. 
- [Java-path-debugging](https://mkyong.com/java/how-to-set-java_home-environment-variable-on-mac-os-x/).

# TODO:
- Figure out acceptable mapping score (or learn this?) else abstain from voting (https://metamap.nlm.nih.gov/Docs/MMI_Output.pdf); 0-1000
- Need a better tokenizer than scispacy
- Align on preprocessing steps to clean data for metamap and scispacy EL - they suck 
- Hack together our concept spanner retainer within metamap given the start/end indices
- We will need to generate new data for every CUI that is labelled within the labelling function? 
- Problem - labelling functions only accept 2 args so we cant pass anything to them (like a metamap instance for e.g.)
- MM LF is too slow because we instantiate mm and get_cui_indices for every datapoint - find a way around this
- Test that my hacked cui_indexer works
- Analyze generated label distributions
- Wipe i2b2-2010