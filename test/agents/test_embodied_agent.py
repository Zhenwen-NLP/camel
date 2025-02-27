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

from camel.agents import EmbodiedAgent, HuggingFaceToolAgent
from camel.generators import SystemMessageGenerator
from camel.messages import ChatMessage, UserChatMessage
from camel.typing import RoleType
from camel.utils import openai_api_key_required


@openai_api_key_required
def test_get_action_space_prompt():
    role_name = "Artist"
    meta_dict = dict(role=role_name, task="Drawing")
    sys_msg = SystemMessageGenerator().from_dict(
        meta_dict=meta_dict,
        role_tuple=(f"{role_name}'s Embodiment", RoleType.EMBODIMENT))
    agent = EmbodiedAgent(
        sys_msg,
        action_space=[HuggingFaceToolAgent('hugging_face_tool_agent')])
    expected_prompt = "*** hugging_face_tool_agent ***:\n"
    assert agent.get_action_space_prompt().startswith(expected_prompt)


@pytest.mark.slow
@pytest.mark.full_test_only
@openai_api_key_required
def test_step():
    # Create an embodied agent
    role_name = "Artist"
    meta_dict = dict(role=role_name, task="Drawing")
    sys_msg = SystemMessageGenerator().from_dict(
        meta_dict=meta_dict,
        role_tuple=(f"{role_name}'s Embodiment", RoleType.EMBODIMENT))
    embodied_agent = EmbodiedAgent(sys_msg, verbose=True)
    print(embodied_agent.system_message)
    user_msg = UserChatMessage(
        role_name=role_name,
        content="Draw all the Camelidae species.",
    )
    output_message, terminated, info = embodied_agent.step(user_msg)
    assert isinstance(output_message, ChatMessage)
    assert not terminated
    assert isinstance(info, dict)
