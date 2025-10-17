# formatTranscript.py

# The below code takes the .vtt files output by Zoom and does the formatting that I've been having the RAs do (since it's time-consuming and a bit of a pain)

# Imports
import argparse
import webvtt
import os

def format_file(filename, **kwargs):
    """Formats the .vtt file and saves it in the folder as a .txt file.

    Args:
        filename (str): File name.
    """

    # Get information on changing participant/interviewer
    change_participant = False
    change_interviewer = False
    if 'participant' in kwargs.keys():
        change_participant = True
        participant = kwargs['participant']
        participant_display = participant[0]
        participant_replace = participant[1]
    if 'interviewer' in kwargs.keys():
        change_interviewer = True
        interviewer = kwargs['interviewer']
        interviewer_display = interviewer[0]
        interviewer_replace = interviewer[1]

    # Set up variables for transcript, current line, and current speaker
    formatted_transcript = ""
    current_line = ""
    current_speaker = ""

    # Loop over .vtt file
    for caption in webvtt.read(filename):
        current_line = caption.text.strip()

        # Change display names if necessary
        if change_interviewer:
            if interviewer_display in current_line:
                current_line = current_line.replace(interviewer_display, interviewer_replace)
        if change_participant:
            if participant_display in current_line:
                current_line = current_line.replace(participant_display, participant_replace)
        
        # Split line into speaker and speech
        split_current_line = current_line.split(": ")
        speaker = split_current_line[0]
        speech = split_current_line[1]
        
        # Check if it is a new speaker or the current speaker
        if speaker == current_speaker:
            # Continuing the previous line --> do not input a \n
            formatted_transcript += speech + ' '
        elif speaker != current_speaker:
            # New speaker
            # If it's the first speaker, don't add new lines
            if len(formatted_transcript) > 0:
                formatted_transcript += "\n \n"
            # Add new line with speaker
            formatted_transcript += current_line
            formatted_transcript += " "
            # Change current speaker
            current_speaker = speaker

    # Save formatted transcript as .txt
    new_filename = filename[:-4]
    new_filename += ".txt"
    with open(new_filename, 'w') as f:
        f.write(formatted_transcript)

# I/O functions
def create_parser():
    """
    Creates a parser for the program.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--format', nargs=1, help="The file to be formatted.", metavar="FILE")
    parser.add_argument('--changeparticipant', nargs=2, help="Change the display name of the participant to an alternate name in the transcript.", metavar=("DISPLAY", "REPLACE"))
    parser.add_argument('--changeinterviewer', nargs=2, help="Change the interviewer's display name on Zoom to an alternate name in the transcript.", metavar=("DISPLAY", "REPLACE"))

    return parser

if __name__ == "__main__":
    # Set up parser & exit handler
    parser = create_parser()
    args = parser.parse_args()

    # Get args
    if args.format:
        path = args.format[0]
        if args.changeinterviewer:
            interviewer = args.changeinterviewer
        else:
            interviewer = []
        if args.changeparticipant:
            participant = args.changeparticipant
        else:
            participant = []
        if len(interviewer) > 0 and len(participant) > 0:
            format_file(path, interviewer=interviewer, participant=participant)
        elif len(interviewer) > 0:
            format_file(path, interviewer=interviewer)
        elif len(participant) > 0:
            format_file(path, participant=participant)
        else:
            format_file(path)