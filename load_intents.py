import json
import argparse
from google.cloud import dialogflow

import config


def add_intent(display_name, questions, answer):
    parent = dialogflow.AgentsClient.agent_path(
        config.dialogflow_project_id
    )
    training_phrases = []
    for training_phrases_part in questions:
        part = dialogflow.Intent.TrainingPhrase.Part(
            text=training_phrases_part
        )
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=[answer])
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message]
    )

    intents_client.create_intent(
        request={'parent': parent, 'intent': intent}
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Load intents for DialogFlow'
    )

    parser.add_argument('intents_path')

    args = parser.parse_args()

    intents_path = args.intents_path
    intents_client = dialogflow.IntentsClient()

    with open(intents_path, 'r', encoding='utf-8') as intents_file:
        intents = json.load(intents_file)

    for display_name, intent_description in intents.items():
        add_intent(
            display_name,
            intent_description['questions'],
            intent_description['answer']
        )
