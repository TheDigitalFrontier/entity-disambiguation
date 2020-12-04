import csv
import os

import numpy as np
import pandas as pd


def normalize_text(text):
    """Return turn in most comparative formatting
    - Strip whitespace
    - Lower case
    - Spaces, not "_"
    """
    return str(text).strip().lower().replace("_", " ")

def process_input(mydir, match="token", train=1.0):
    """
    Function that processes the training input into required formatting (ACY dataset)

    Args:
    mydir, the directory that ADY dataset lives in on user's local machine
    target, individual token or full_mention as classified by ACY
    train, percentage of training samples specified by user, default 80%

    Returns:
    train_x, input for training (tokens and word counts in between this mention and the last mention)
    train_y, output for training (wikipedia page ID's)
    train_x, input for testing
    train_y, output for testing
    """
    tsv_file = open(os.path.join(mydir, "AIDA-YAGO2-DATASET.tsv"))
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    df = []
    for row in read_tsv:
        df.append(row)
    acy_df = pd.DataFrame(data=df[1:])
    new = ["token", "mention", "full_mention", "YAGO2", "wikipedia_URL", "wikipedia_ID", "freebase"]
    acy_df = acy_df.rename(columns=dict(zip(range(7), new)))

    # Decide what to input
    if match == "token":
        matches = acy_df.token.values
    elif match == "full_mention":
        matches = acy_df.full_mention.values

    ids = acy_df.wikipedia_ID.values

    new_matches = []
    new_ids = []
    new_until_next = []

    until_next = 0
    for i in range(len(acy_df)):
        # if we have a token with an entity
        if ids[i] != None:
            new_until_next.append(until_next)
            # re-initialize word count in between
            until_next = 0
            new_ids.append(ids[i])
            new_matches.append(matches[i])
        # else we append to words counts between mentions
        else:
            until_next += 1

    new_ids = np.array(new_ids)
    train_len = int(train * len(new_matches))

    train_x = pd.DataFrame(columns=[match, "in_between_word_count"])
    train_x[match] = new_matches[:train_len]
    train_x.in_between_word_count = new_until_next[:train_len]
    train_y = new_ids[:train_len]

    test_x = pd.DataFrame(columns=[match, "in_between_word_count"])
    test_x[match] = new_matches[train_len:]
    test_x.in_between_word_count = new_until_next[train_len:]
    test_y = new_ids[train_len:]

    return train_x, train_y, test_x, test_y
