#!/usr/bin/env python3

import re
from collections import Counter

import utils as u

sample_text = "This is a sample text. This text is for testing purposes.\n\nIt contains multiple paragraphs, sentences, and words."


def count_specific_word(word, article):
    u.validate_input(article)
    u.validate_input(word)
    words = re.findall(r"\b\w+\b", article.lower())
    counts = Counter(words)
    return counts[word.lower()]


def identify_most_common_word(text):
    u.validate_input(text)
    words = u.tokenize_text(text)
    counts = Counter(words)
    max_count = max(counts.values())
    most_common = None
    for word in words:
        if counts[word] == max_count:
            most_common = word
    return most_common


def calculate_average_word_length(text):
    u.validate_input(text)
    words = u.tokenize_text(text)
    total_length = 0
    for w in words:
        total_length += len(w)

    return total_length / len(words) if words else 0.0


def count_paragraphs(text):
    u.validate_input(text)
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return len(paragraphs)


def count_sentences(text):
    u.validate_input(text)
    s = text.strip()
    i = 0
    count = 0
    in_sentence = False
    while i < len(s):
        ch = s[i]
        if ch.isalnum():
            in_sentence = True
            i += 1
        elif ch in ".!?":
            if in_sentence:
                count += 1
                in_sentence = False
            while i < len(s) and s[i] in ".!?":
                i += 1
        else:
            i += 1

    return count
