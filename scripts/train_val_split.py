import random

if __name__ == "__main__":
    with open("../data/raw/train.txt", "r") as train_val_in:
        lines = train_val_in.readlines()
    sentences = []
    sentence = []
    for line in lines:
        line_clean = line.strip()
        if len(line_clean) > 0:
            sentence.append(line_clean.split("\t"))
        else:
            sentences.append(sentence)
            sentence = []
    random.seed(62)
    random.shuffle(sentences)

    with open("../data/input/train.tsv", "w") as train_out:
        for sentence in sentences[:3000]:
            for word, tag in sentence:
                train_out.write(f"{word}\t{tag}\n")
            train_out.write("\n")

    with open("../data/input/val.tsv", "w") as val_out:
        for sentence in sentences[3000:]:
            for word, tag in sentence:
                val_out.write(f"{word}\t{tag}\n")
            val_out.write("\n")

