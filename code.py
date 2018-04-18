from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import json
import six
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/exepaul/Documents/google_cloud/monkproject-75258f3c75c2.json"

def entities_text(text):
    """Detects entities in the text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')



    # Instantiates a plain text document.
    # [START migration_analyze_entities]
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities
    return [entity.name for entity in entities]


    # [END migration_analyze_entities]
# [END def_entities_text]
data=entities_text('what is the price of bitcoin today?')
print(data)
