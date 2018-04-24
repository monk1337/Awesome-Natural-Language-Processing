from nltk import ne_chunk, pos_tag, word_tokenize

from nltk.tree import Tree

my_sent="""The Israeli Prime Minister Benjamin Netanyahu has warned that Iran poses a "threat to the entire world."""
sentences = word_tokenize(my_sent)
print(sentences)
pos_tagging = pos_tag(sentences)

print(pos_tagging)


chunked_sentences = ne_chunk(pos_tagging, binary=True)

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

entity_names = []
for tree in chunked_sentences:
    # Print results per sentence
    # print extract_entity_names(tree)

    entity_names.extend(extract_entity_names(tree))

# Print all entity names
print(entity_names)

# Print unique entity names
print(set(entity_names))



#output

# ['The', 'Israeli', 'Prime', 'Minister', 'Benjamin', 'Netanyahu', 'has', 'warned', 'that', 'Iran', 'poses', 'a', '``', 'threat', 'to', 'the', 'entire', 'world', '.']
# [('The', 'DT'), ('Israeli', 'NNP'), ('Prime', 'NNP'), ('Minister', 'NNP'), ('Benjamin', 'NNP'), ('Netanyahu', 'NNP'), ('has', 'VBZ'), ('warned', 'VBN'), ('that', 'IN'), ('Iran', 'NNP'), ('poses', 'VBZ'), ('a', 'DT'), ('``', '``'), ('threat', 'NN'), ('to', 'TO'), ('the', 'DT'), ('entire', 'JJ'), ('world', 'NN'), ('.', '.')]
# ['Israeli', 'Benjamin Netanyahu', 'Iran']
# {'Iran', 'Israeli', 'Benjamin Netanyahu'}
