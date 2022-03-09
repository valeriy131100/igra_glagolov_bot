from google.cloud import dialogflow

import config


def get_dialogflow_answer(text, session_client, session_id,
                          return_fallback=False):
    project_id = config.dialogflow_project_id

    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(
        text=text,
        language_code='ru-RU'
    )

    query_input = dialogflow.QueryInput(
        text=text_input
    )

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    is_fallback = response.query_result.intent.is_fallback

    if not is_fallback or return_fallback:
        return response.query_result.fulfillment_text
