def increment(x, by=1):
    return x + by


def tokenize(sentence):
    return pos_tag(word_tokenize(sentence))


def synsets(sentence):
    tokens = tokenize(sentence)
    return remove_none(tagged_to_synset(*t) for t in tokens)


def remove_none(xs):
    return [x for x in xs if x is not None]


def score(synset, synsets):
    return max(synset.path_similarity(s) for s in synsets)


def sentence_similarity(sentence1, sentence2):
    synsets1 = synsets(sentence1)
    synsets2 = synsets(sentence2)
    scores = remove_none(score(s, synsets2) for s in synsets1)
    return float(sum(scores)) / len(scores)
