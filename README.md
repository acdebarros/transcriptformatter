# Transcript Formatter
Python code to format a .vtt file as a transcript.

## Installing

Using Transcript Formatter requires you to have Python installed on your system. Please see instructions on how to do that [here](https://wiki.python.org/moin/BeginnersGuide/Download).

You can download the file from this repository by hitting the green "<> Code" button and either cloning the repository (if you're used to using git) or by downloading the files as a .zip. Then, unzip the folder and save the files wherever you'd like to use them.

You can also install this using the .whl file in the dist folder. In your command line, run:

`pip install /path/to/.whlfile`

Replace `/path/to/.whlfile` with the full file path to wherever you saved the file.

Note: If you have a Mac, you may need to first use homebrew to install pipx. Run:

`brew install pipx`

Then, replace pip with pipx in the command above.

## How to Use

1. Open a terminal in the same folder where you have saved the Python file.
2. To start using transcriptFormatter, you always begin with `python3 formatTranscript.py`. Then you will need to add a flag (i.e., an option). One of them will always be --format (unless you're just looking for the help message). The flags offered by Transcript Formatter are:
-	-h, --help: These show you a help message and then exit
-	--format: This is how you specify the file that needs to be formatted. If it's saved in the same folder as the Python script, you just need to give it the file name. If not, you need the whole file path. Make sure to run it in quotation marks if there are spaces in the file path (e.g., `python3 formatTranscript.py --format "Users/anacarolinadebarros/Documents/GitHub Repositories"`), or use escape characters (e.g., `python3 formatTranscript.py --format Users/anacarolinadebarros/Documents/GitHub\ Repositories). 
-	--changeparticipant: This allows you to change the display name of the participant, and you will need to follow it up with both the display name and the name you want to replace it with. For example, if the participant's display name was their participant ID and you want to replace it with their pseudonym, you would run: `python3 formatTranscript.py --format FILENAME --changeparticipant "RD111" "Andrew"`. Note that this only works if the script can find your participant's display name exactly as you provide it.
-	--changeinterviewer: This allows you to change the display name of the interviewer, and you will need to follow it up with both the display name and the name you want to replace it with. For example, if the interviewer's display name was their first name and their affiliation and you want to replace it with their initials, you would run: `python3 formatTranscript.py --format FILENAME --changeparticipant "Carolina (she/her) - van Anders Lab" "CDB"`. Note that this only works if the script can find your interviewer's display name exactly as you provide it.

**Note**: If you installed the code as a package using the .whl file, instead of running `python3 formatTranscript.py`, you can just run `transformat` followed by the necessary flags.

## Questions, Comments, Concerns

Please email a.debarros@queensu.ca.
