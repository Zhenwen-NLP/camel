# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
import pytest

from camel.messages import BaseMessage
from camel.prompts import CodePrompt, TextPrompt
from camel.typing import RoleType


@pytest.fixture
def base_message() -> BaseMessage:
    return BaseMessage(
        role_name="test_user",
        role_type=RoleType.USER,
        meta_dict={"key": "value"},
        role="user",
        content="test content",
    )


def test_base_message_get_attribute(base_message: BaseMessage):
    assert base_message.upper().content == "TEST CONTENT"
    assert base_message.startswith("test")


def test_base_message_addition_operator(base_message: BaseMessage):
    new_message = base_message + "!"
    assert new_message.content == "test content!"


def test_base_message_multiplication_operator(base_message: BaseMessage):
    new_message = base_message * 3
    assert new_message.content == "test contenttest contenttest content"


def test_base_message_length_operator(base_message: BaseMessage):
    assert len(base_message) == 12


def test_base_message_contains_operator(base_message: BaseMessage):
    assert "test" in base_message
    assert "foo" not in base_message


def test_base_message_token_len(base_message: BaseMessage):
    token_len = base_message.token_len()
    assert isinstance(token_len, int)
    assert token_len == 9


def test_extract_text_and_code_prompts():
    base_message = BaseMessage(
        role_name="test_role_name", role_type=RoleType.USER, meta_dict=dict(),
        role="user", content="This is a text prompt.\n\n"
        "```python\nprint('This is a code prompt')\n```\n"
        "This is another text prompt.\n\n"
        "```c\nprintf(\"This is another code prompt\");\n```")
    text_prompts, code_prompts = base_message.extract_text_and_code_prompts()

    assert len(text_prompts) == 2
    assert isinstance(text_prompts[0], TextPrompt)
    assert isinstance(text_prompts[1], TextPrompt)
    assert text_prompts[0] == "This is a text prompt."
    assert text_prompts[1] == "This is another text prompt."

    assert len(code_prompts) == 2
    assert isinstance(code_prompts[0], CodePrompt)
    assert isinstance(code_prompts[1], CodePrompt)
    assert code_prompts[0] == "print('This is a code prompt')"
    assert code_prompts[1] == "printf(\"This is another code prompt\");"
    assert code_prompts[0].code_type == "python"
    assert code_prompts[1].code_type == "c"


def test_base_message_to_dict(base_message: BaseMessage) -> None:
    expected_dict = {
        "role_name": "test_user",
        "role_type": "USER",
        "key": "value",
        "role": "user",
        "content": "test content",
    }
    assert base_message.to_dict() == expected_dict


def test_base_message():
    role_name = "test_role_name"
    role_type = RoleType.USER
    meta_dict = {"key": "value"}
    role = "user"
    content = "test_content"

    message = BaseMessage(role_name=role_name, role_type=role_type,
                          meta_dict=meta_dict, role=role, content=content)

    assert message.role_name == role_name
    assert message.role_type == role_type
    assert message.meta_dict == meta_dict
    assert message.role == role
    assert message.content == content

    user_message = message.to_user_chat_message()
    assert user_message.role_name == role_name
    assert user_message.role_type == role_type
    assert user_message.meta_dict == meta_dict
    assert user_message.role == "user"
    assert user_message.content == content

    assistant_message = message.to_assistant_chat_message()
    assert assistant_message.role_name == role_name
    assert assistant_message.role_type == role_type
    assert assistant_message.meta_dict == meta_dict
    assert assistant_message.role == "assistant"
    assert assistant_message.content == content

    openai_message = message.to_openai_message()
    assert openai_message == {"role": role, "content": content}

    openai_chat_message = message.to_openai_chat_message()
    assert openai_chat_message == {"role": role, "content": content}

    openai_system_message = message.to_openai_system_message()
    assert openai_system_message == {"role": "system", "content": content}

    openai_user_message = message.to_openai_user_message()
    assert openai_user_message == {"role": "user", "content": content}

    openai_assistant_message = message.to_openai_assistant_message()
    assert openai_assistant_message == {
        "role": "assistant",
        "content": content
    }

    dictionary = message.to_dict()
    assert dictionary == {
        "role_name": role_name,
        "role_type": role_type.name,
        **(meta_dict or {}), "role": role,
        "content": content
    }
