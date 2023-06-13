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
from typing import Any

from camel.prompts import TextPrompt, TextPromptDict
from camel.typing import RoleType


# flake8: noqa :E501
class EducationPromptTemplateDict(TextPromptDict):
    r"""A dictionary containing :obj:`TextPrompt` used in the `AI Society`
    task.

    Attributes:
        GENERATE_ASSISTANTS (TextPrompt): A prompt to list different roles
            that the AI assistant can play.
        GENERATE_USERS (TextPrompt): A prompt to list common groups of
            internet users or occupations.
        GENERATE_TASKS (TextPrompt): A prompt to list diverse tasks that
            the AI assistant can assist AI user with.
        TASK_SPECIFY_PROMPT (TextPrompt): A prompt to specify a task in more
            detail.
        ASSISTANT_PROMPT (TextPrompt): A system prompt for the AI assistant
            that outlines the rules of the conversation and provides
            instructions for completing tasks.
        USER_PROMPT (TextPrompt): A system prompt for the AI user that
            outlines the rules of the conversation and provides instructions
            for giving instructions to the AI assistant.
    """
    GENERATE_ASSISTANTS = TextPrompt(
        """""")

    GENERATE_USERS = TextPrompt(
        """""")

    GENERATE_TASKS = TextPrompt(
        """""")

    TASK_SPECIFY_PROMPT = TextPrompt(
        """"""
    )

    ASSISTANT_PROMPT = TextPrompt(
        """Never forget you are a teacher and I am a student. Never flip roles!
You are teaching your students in an interactive way, by providing feedback according ot their responses. Never forget our task! The problem is:
<Problem>: Lisa, Jack, and Tommy earned $60 from washing cars all week. However, half of the $60 was earned by Lisa. Tommy earned half of what Lisa earned. How much more money did Lisa earn than Tommy?
<Solution>: 15
You must help me to correct my errors and misunderstandings to complete the task. Never provide me with the correct solution directly!
Unless I say the task is completed, you should always start with:

Teacher Response: <YOUR_RESPONSE>

<YOUR_RESPONSE> should be imitating human teachers. At the beginning, you can ask the student to start attempting. After receiving attempts from students, you may ask questions like 'So what should you do next?', 'Can you calculate . . . ?', 'Are you sure you need to add here?', 'Why do you think you need to add these numbers?', 'Can you go walk me through your solution?'
Or just reveal the partial solution to the student such as 'You need to add . . . to . . . to get your answer.', 'No, he had . . . items.' to help students to correct their mistakes and approach the correct solution.
Always end <YOUR_RESPONSE> with: Please continue to attempt.""")

    USER_PROMPT = TextPrompt(
        """Never forget you are a student and I am a teacher. Never flip roles! You will always try to solve a math problem step by step until reaching the correct solution. The problem is:
<Problem>: Lisa, Jack, and Tommy earned $60 from washing cars all week. However, half of the $60 was earned by Lisa. Tommy earned half of what Lisa earned. How much more money did Lisa earn than Tommy?
<Solution>: 15  (Please note that you should assume you do not know the answer.)
The teacher will give feedback to your solution, aimming to teach you how to solve a problem. Never forget our task!
You must imitate the behavior of imperfect human students, think the solution step by step, and reply in the following way:

Student Attempt: <YOUR_ATTEMPT>

YOUR_ATTEMPT describes your thoughts towards how to solve the problem. You must try to solve the problem step by step and do not skip any intermediate steps. You must remember that you are imperfect and may make mistakes in your solution. But you can correct them with the instructions from me. 

You must give me one step of your solution in one response. Do not give me the final answer directly.
I must write a question or comment that appropriately respond your attempt as your teacher.
You should always attempt to solve problems, do NOT ask me questions.
Do not add anything else other than your attempt towards the solution!
When the task is completed, you must only reply with a single word <PROBLEM_SOLVED>.""")

    CRITIC_PROMPT = TextPrompt(
        """""")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.update({
            "generate_assistants": self.GENERATE_ASSISTANTS,
            "generate_users": self.GENERATE_USERS,
            "generate_tasks": self.GENERATE_TASKS,
            "task_specify_prompt": self.TASK_SPECIFY_PROMPT,
            RoleType.ASSISTANT: self.ASSISTANT_PROMPT,
            RoleType.USER: self.USER_PROMPT,
            RoleType.CRITIC: self.CRITIC_PROMPT,
        })
