# DrSnorkel
A package for programmatically building clinical training data via weak supervision through Snorkel

# Installation 

- Install metamap from [here](https://metamap.nlm.nih.gov/MainDownload.shtml).
- Install [pymetamap](https://github.com/AnthonyMRios/pymetamap/blob/master/pymetamap/MetaMapLite.py?fbclid=IwAR2xqL2RzAV70IoFO15N0UgNkR9BeSZAqIPOLwxhBRXZ985J6n41f8YujW0).

# How to run: 
- In a terminal session, navigate to the directory where the metamap bin is (e.g. $HOME/Projects/repos/public_mm/bin/), and start the metamap tagger server with `./bin/skrmedpostctl start`
- In another terminal session, run `python -m drsnorkel.drsnorkel` from this repo's root dir to execute the main entry point

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
- Ideas of multilabel: 
  - https://github.com/snorkel-team/snorkel/issues/1041
    - So create n binary classifiers: We appreciate the offer to contribute! In general, you can naively support multi-label problems by just treating each label as a separate binary classification problem.
    - the basic approach is just to treat a $k$-wise multi-label classification problem as $k$ separate binary tasks. These can also share / jointly learn representations using a multi-task learning approach as supported in Snorkel!
- what does context hierarchy mean?
- check this out - We thus trade off expressivity and efficiency by allowing users to write labeling functions at two levels of abstraction: custom Python functions and declarative operators.
- add whole sieve to snorkel! (e.g. use declarative LFs)
- Label density for snorkel! KEY FOR US TO BRAINSTORM
- Why do dependencies bw labelling functions skew accuracies?
- try out declarative labelling functions?
- **** - we need to estimate label density ASAP! after LFs ASAP! - performance and speed tradeoff: all about density of label matrix - we may not even have improvement bc of our long-tail
  - In the low-density setting, sparsity of labels will mean that there is limited room for even an optimal weighting of the labeling functions to diverge much from the majority vote
  - As density grows, known theory confirms that the majority vote will eventually be optimal [27].
  - It is the middle-density regime where we expect to most benefit from applying the genera- tive model. 
    - In this middle regime, we expect that modeling the accuracies of the labeling functions will deliver the greatest gains in predictive performance because we will have many data points with a small number of dis- agreeing labeling functions. For such points, the estimated labeling function accuracies can heavily affect the predicted labels.
- key = we need 10-100 LFs get the advantage!
- ***Aim for: the majority of the data points have a large number of labels. For ex- ample, we might be working in an extremely high-volume crowdsourcing setting, or an application with many high- coverage knowledge bases as distant supervision.
- How do we use snorkel's discriminative models?
- ** predictive performance for  disc for uLF vs LF is low for EHR - worth it?? 
- how do we use their context hierarchy to use structure-based labelling functions? (p11)
- get their viewer? A key aspect of labeling function development is that the pro- cess is iterative. After developing an initial set of labeling func- tions, it is important for users to visualize the errors of the end model. Therefore, when the model is evaluated on the devel- opment data set, the candidates are separated into true positive, false positive, true negative, and false negative sets. Each of these buckets can be loaded into a viewer in a notebook (Figure 10) so that SMEs can identify common patterns that are either not covered or misclassified by their current labeling functions. The viewer also supports labeling candidates directly in order to cre- ate or expand development and test sets.
- what is this? automatically defining candidates using their named-entity recognition features.

# New: 
- reprocess data to make more sense with preprocessing function! 
- should we do by sents or docs? 
- our major problem is we still assume only 1 CUI per sentence - but can have many CUIs per document!
  - in our preprocessor - we can output new fields for each datapoint in a dict - we can thus assume a max of 10-20 CUIs per datapoint, and create these as fields (we will have to see what max CUI / datapoint is over the dataset!)

# Training: 
-what do we want to train in - allennlp or their own MTL framework - for our discriminative model? 

- ideal approach: https://github.com/snorkel-team/snorkel/issues/1041
  - 1) Create n binary classifier "LF wrappers" for each CUI - use LF generators - see paper p4
  - 2) Preprocess text with true labelling function (e.g. MetaMap, Scispacy) in a preprocessing step 
  - 3) Preprocesser feeds 1 to CUIn LF if CUIn is present in text, else 0.
  - 4) for the label model, use n versions of the basic label model
      - These can also share / jointly learn representations using a multi-task learning approach as supported in Snorkel
- try to find more info of their EHR labelling functions / regex (p10)

