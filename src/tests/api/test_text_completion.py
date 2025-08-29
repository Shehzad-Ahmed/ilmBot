def test_text_completion_success(
    client, mock_chat_openai_agenerate, create_mock_llm_result
):
    mock_text = "Complete the text."
    mock_result = create_mock_llm_result([mock_text])
    mock_chat_openai_agenerate.return_value = mock_result

    test_text = "Complete this text. "

    response = client.post(
        "/api/v1/text-completion",
        json={"text": test_text},
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/event-stream")

    content = ""
    for chunk in response.iter_text(chunk_size=1024):
        content += chunk

    assert mock_text == content
    mock_chat_openai_agenerate.assert_called_once()


def test_text_completion_streaming_chunks(
    client, mock_chat_openai_agenerate, create_mock_llm_result
):
    first_chunk = "First chunk "
    second_chunk = "Second chunk"
    mock_result = create_mock_llm_result([first_chunk, second_chunk])
    mock_chat_openai_agenerate.return_value = mock_result
    response = client.post(
        "/api/v1/text-completion",
        json={"text": "Test text"},
    )
    print(response.content)
    assert mock_chat_openai_agenerate.called
    chunks = list(response.iter_text(chunk_size=1024))
    # TODO: perform proper chunk tests by using asyncio
    # assert len(chunks) >= 1
    # assert first_chunk == chunks[0]
    # assert second_chunk == chunks[1]


def test_text_completion_invalid_text(client, mock_chat_openai_agenerate):
    test_text = ""
    response = client.post(
        "/api/v1/text-completion",
        json={"text": test_text},
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Text can not be empty",
        "error_code": "text_cannot_be_empty",
    }

    mock_chat_openai_agenerate.assert_not_called()
