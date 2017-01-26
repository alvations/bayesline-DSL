This is the training data for the 2016 DSL Shared Task.

It contains the following files:

task1-train.txt - Training set for sub-task 1
task1-dev.txt - Development set for sub-task 1
task2-train.txt - Training set for sub-task 2 (Arabic dialects)

Each line in the .txt files are tab-delimited in the format:
sentence<tab>language-label

Note that sub-task 2 does not have a development set.

== Evaluation ==

The test data will only contain sentences without their language/variety labels.

!!! IMPORTANT, please note the following to facilitate the evaluation !!!

(1) provide the system output as how the training and development data was 
formatted, without changing the order of the test sentences:

sentence<tab>language-label

(2) Please name your submission files with the following convention,
all in lowercase:

	<team_name>-<system_name>-<open_or_close>-<run#>.txt

For example, if your team_name is "USAAR" , system_name is "DisLang" and it's an
open submission and it's the 1st run that you want to submit, the submission
file should be as such:
	
	usaar-dislang-open-normal-run1.txt


(3) Please also compress ALL run submissions into a single file and send it to
dsl.sharedtask@gmail.com before the submission deadline, please name
compressed file in the following format: (team_name-system-name.zip)
For example:

	usaar-dislang.zip

(4) Do specify in the email title when sending the compression submission file,
e.g. (team_name DSL2016 submission)
Title: USAAR DSL2016 submission

(5) Each team is ONLY allowed to submit 3 runs for closed and/or 3 runs for 
open task, (6 runs in total for teams participating in both)

(6) Along with the systems runs, submit a short description of your system.
This is to facilitate the description of the systems in the summary/finding 
paper for the shared task. You can put it as a plaintext file into the 
compressed zip or just write it in the email as you send the submissions.


