# for entity extraction


import spacy

nlp = spacy.load('en_core_web_md')

model = nlp('tell me, tomorrow what will be the price of Bitcoin')

for ent in model.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

output

# tomorrow 9 17 DATE
# Bitcoin 44 51 ORG


# output

# (tomorrow, Bitcoin)


new_text = 'Apple is looking at buying U.K. startup for $1 billion'

for token in model(new_text):
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)

# output


# for Part of speech without any noisy words

import json
import spacy as nlp_model

Noisy_frequencies_weights = {'6f74686572', '616761696e', '796f7572', '6f7574', '7768657265', '74686579277265',
                             '686176696e67', '77686f6d', '69276c6c', '616e', '647572696e67', '692764', '7570',
                             '66757274686572', '7768696368', '6f72', '68652764', '746861742773', '776173', '6865276c6c',
                             '796f752764', '776f756c64', '616c6c', '77657265', '626f7468', '646f6573', '7468726f756768',
                             '69276d', '646964', '6265666f7265', '616d', '74686174', '6973', '7765', '6f6e',
                             '746865792764', '686572', '646f', '77686f2773', '776879', '7468657265', '68657273',
                             '73616d65', '7468656e', '756e646572', '6966', '7768656e', '616e79', '7368652773',
                             '74686579277665', '6174', '7468656972', '62656361757365', '6f6e6c79', '6f757273656c766573',
                             '6265696e67', '696e746f', '68657273656c66', '646f776e', '62656c6f77', '776861742773',
                             '696e', '6d6f7265', '77686174', '68657265', '69277665', '6865', '796f757273',
                             '796f75277265', '666f72', '686973', '73756368', '61', '77686572652773', '7468656d',
                             '7768792773', '6974', '7765277665', '6d7973656c66', '697473656c66', '7768656e2773',
                             '6c65742773', '6f6e6365', '796f757273656c66', '746f', '7765277265', '7468657365', '627574',
                             '74686579276c6c', '6d79', '66726f6d', '6279', '6d6f7374', '7368652764', '796f75277665',
                             '69742773', '6d65', '77697468', '736f6d65', '7765276c6c', '746865', '7768696c65',
                             '686f772773', '6e6f72', '61626f7665', '666577', '68696d', '646f696e67', '6f776e', '6f7572',
                             '616e64', '6f66', '756e74696c', '617265', '68652773', '796f75', '61626f7574', '77686f',
                             '77652764', '68696d73656c66', '73686f756c64', '6265747765656e', '6f766572', '736865276c6c',
                             '74686579', '65616368', '74686572652773', '746865697273', '636f756c64', '686572652773',
                             '746f6f', '796f757273656c766573', '7468656d73656c766573', '6f757273', '736f', '6173',
                             '74686973', '76657279', '697473', '6f75676874', '69', '6265656e', '6166746572', '686164',
                             '686f77', '796f75276c6c', '74686f7365', '6265', '686173', '7468616e', '68617665', '736865',
                             '616761696e7374'}

# Data cleaning part Frequencies which are noisy and should be remove before sending the output to natural_language_processing

English_Validation_weights = {65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
                              87, 88, 89, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112,
                              113, 114, 115, 116, 117, 118, 119, 120, 121}

# Check point for English words validation , avoid other than English words

Number_validation_weights = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def natural_language_processing(user_query):
    natural_language_understanding_ = nlp_model.load('en_core_web_md')

    # Using natual language processing getting the most weighted words from user_query


    meaning_intent_dependency = []

    for _pos in natural_language_understanding_(user_query):

        if _pos.pos_ == 'NOUN' and str(_pos).encode('utf-8').hex() not in Noisy_frequencies_weights:

            # Ignoring the noisy frequencies and making data clean


            # checking if any Noun in user query


            # ex : i am looking something for sit :
            #                  \_______/    \___/

            #                   ++ #N_1     ++ #N_2



            if str(_pos) not in meaning_intent_dependency:
                meaning_intent_dependency.append(str(_pos))

        if _pos.pos_ == 'VERB' and str(_pos).encode('utf-8').hex() not in Noisy_frequencies_weights:

            # checking if any VERB in user query


            # ex : i am looking something for sit :
            #       \__/ \_____/
            #        #v_1  #v_2



            if str(_pos) not in meaning_intent_dependency:
                meaning_intent_dependency.append(str(_pos))

        if _pos.pos_ == 'PROPN' and str(_pos).encode('utf-8').hex() not in Noisy_frequencies_weights:

            # checking if any PROPN ==> Proper Noun in user query

            # ex : Is Seasonal Collections available? :
            #     |__||____|  |__________|
            #      #P1  #P2        #P3


            if str(_pos) not in meaning_intent_dependency:
                meaning_intent_dependency.append(str(_pos))

        if _pos.pos_ == 'ADJ' and _pos not in Noisy_frequencies_weights:

            # checking if any ADJ >> Adjectives


            # ex : Hi, i am looking for android phone. :
            #                          |_______|
            #                             ADJ

            if str(_pos) not in meaning_intent_dependency:
                meaning_intent_dependency.append(str(_pos))
    return meaning_intent_dependency

print(natural_language_processing("hello i am buying apple what are you doing tomorrow for your tea"))


# output

# ['buying', 'apple', 'tomorrow', 'your', 'tea']


