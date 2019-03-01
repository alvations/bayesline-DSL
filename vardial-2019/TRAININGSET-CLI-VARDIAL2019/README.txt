== Data Format ==

The training data contains the following files:

	train.txt - training set
	dev.txt   - development/validation set

Each line in the *.txt files is tab-delimited in the format:

	sentence<tab>dialect-label

The training data contains individual lines from cuneiform texts written in Sumerian (SUX) and in six Akkadian dialects: Old Babylonian (OLB), Middle Babylonian peripheral (MPB), Standard Babylonian (STB), Neo Babylonian (NEB), Late Babylonian (LTB), and Neo Assyrian (NEA). The training data set contains different number of lines for each language or dialect, ranging from 3,803 lines for Old Babylonian to 53,673 lines for Sumerian. The development set data contains 668 lines for each language or dialect. You can use the development set for model selection to avoid overfitting the training set. We recommend you to train your final system on the combined training and development sets.

In order to actually view the contents of the lines you might need to download special fonts depending on your operating system environment. Informatiom about the three Unicode blocks containing Cuneiform script is available in English Wikipedia: https://en.wikipedia.org/wiki/Cuneiform_(Unicode_block).

The task is a closed one, so no information about the languages available through other sources than the datasets provided by the organizers should be used when building and training the language identification system for the task. The datasets are derivations from texts available through ORACC: The Open Richly Annotated Cuneiform Corpus. 

== Evaluation ==

The test data (to be released later) will only contain sentences without their dialect labels.

Participants will be required to submit the labels for these test instances.

The exact details of the submission file format will be provided later.
