import json
import watson_developer_cloud
from watson_developer_cloud import NaturalLanguageUnderstandingV1


from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions


def natural_language_processing_tokens(query):

    try:
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            username='your user_name', #demo 9c2c3440-6676-9bca-b803-11557d981277
            password='#password',  #demo '#kmHtVHjkglALS
            version='2017-02-27')

        response = natural_language_understanding.analyze(
            text=query,
            features=Features(
                entities=EntitiesOptions(
                    emotion=True,
                    sentiment=True,
                    limit=2),
                keywords=KeywordsOptions(
                    emotion=True,
                    sentiment=True,
                    limit=100)))

        return [sub_item for item in list(map(lambda x: (x['text'].split(),x['sentiment']), response['keywords'])) for sub_item in item]
    except watson_developer_cloud.watson_service.WatsonApiException:
        return []

print(natural_language_processing_tokens('Permanence, perseverance and persistence in spite of all obstacles, discouragements, and impossibilities: It is this, that in all things distinguishes the strong soul from the weak.'))




#output:

# [['strong', 'soul'], {'label': 'positive', 'score': 0.613076}, ['impossibilities'], {'label': 'neutral', 'score': 0.0}, ['Permanence'], {'label': 'positive', 'score': 0.288415}, ['perseverance'], {'label': 'negative', 'score': -0.307953}, ['spite'], {'label': 'negative', 'score': -0.307953}, ['obstacles'], {'label': 'negative', 'score': -0.307953}, ['persistence'], {'label': 'negative', 'score': -0.307953}, ['discouragements'], {'label': 'neutral', 'score': 0.0}, ['things'], {'label': 'positive', 'score': 0.613076}]
