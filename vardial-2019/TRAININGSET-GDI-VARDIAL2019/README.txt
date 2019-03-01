== Data Format ==

The training data for this year's GDI task is split across six files, three for the training set and three for the development/validation set.

The training set contains the following files:
	train.txt	each line contains the transcript of one utterance and the corresponding dialect label,
				separated by a tab: sentence<tab>dialect-label
	train.norm	each line contains the transcription text together with word-level normalization (but not the
				dialect label), separated by |: originalword1|normalizedword1 originalword2|normalizedword2 ...
	train.vec	each line contains a 400-dimensional iVector representing the acoustic features of the utterance 
				(but not the dialect label); the values are separated by spaces

The development set contains the files dev.txt, dev.norm and dev.vec in the same formats.
The test set will be released later and will contain the files test.txt, test.norm and test.vec in the same formats, except for test.txt which will not contain dialect labels.

You can use the development set for model selection to avoid overfitting the training set. The training/development/test split is the same as last year, but some additional filters and corrections have been applied to the data. The training data contains utterances from four Swiss German dialects: Bern (BE), Basel (BS), Lucerne (LU) and Zurich (ZH). The training set contains data from 3-7 speakers per dialect, and the development set contains data from 1 speaker per dialect. There is no speaker overlap between the training and development sets. Due to this rather small number of speakers, we recommend you to train your final chosen system on the combined training and development sets. The test set will contain data from 1-2 speakers per dialect, again without speaker overlap between test and training/development set.

The word-level normalizations have been produced automatically using character-level statistical machine translation (see https://www.linguistics.rub.de/konvens16/pub/32_konvensproc.pdf for details on the approach). Words that could not be normalized show an underscore as their normalization, e.g. cho|_. Normalizations consisting of more than one word are joined by an underscore, e.g. dasch|das_ist. This word-level normalization format hopefully allows participants to experiment with various feature representations such as inferred character alignments.

=== About the transcriptions ===

There is no widely spread convention for writing Swiss German. All instances have been transcribed using the writing system "Schwyzertütschi Dialäktschrift" proposed by Dieth (1986) to provide some guidance on how to write in a Swiss German dialect. The transcription is expected to show the phonetic properties of the variety but in a way that is legible for everybody who is familiar with standard German orthography (Dieth, 1986, 10). Dieth's system, which is originally phonemic, can be implemented in different ways depending on how differentiated the phonetic qualities are to be expressed. Although it is the objective to keep track of the pronunciation, Dieth's transcription method is orthographic and partially adapted to spelling habits in standard German. Therefore it does not provide the same precision and explicitness as phonetic transcription methods do. The transcriptions exclusively use lower case characters. Note that Dieth's system is hardly known by laymen, so that e.g. Swiss German data extracted from social media may look fairly different from our transcriptions.

In our transcriptions, we do not use the full power of phonemic distinctions available in the Dieth script. The grapheme inventory in the Dieth script is always related to the dialect and its phonetic properties, so that, for example, the grapheme <e> stands for different vowel qualities, [e], [ɛ] or [ə], depending on the dialect, the accentuation of the syllable and - to substantial degree - also to the dialectal background of the transcriber. For each dialect area, we include instances of several speakers and several transcribers.

== Evaluation ==

The test data (to be released later) will contain the files test.txt, test.norm and test.vec in the same formats as explained above, but without their dialect labels.

Participants will be required to submit the labels for these test instances.

The exact details of the submission file format will be provided later.
