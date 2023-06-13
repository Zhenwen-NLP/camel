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
from colorama import Fore

from camel.agents import RolePlaying
from camel.utils import print_text_animated
from camel.typing import TaskType
import openai, os


def main() -> None:
    task_prompt = """Create an interactive role-playing session of teacher and student collaborating on solving the following math problem:
<Problem>: Lisa, Jack, and Tommy earned $60 from washing cars all week. However, half of the $60 was earned by Lisa. Tommy earned half of what Lisa earned. How much more money did Lisa earn than Tommy?
<Solution>: 15    
"""
    role_play_session = RolePlaying(
        "Teacher",
        "Student",
        task_type = TaskType.EDUCATION,
        with_task_specify=False,
    )

    print(
        Fore.GREEN +
        f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n")
    print(Fore.BLUE +
          f"AI User sys message:\n{role_play_session.user_sys_msg}\n")

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
         Fore.CYAN +
         f"Specified task prompt:\n{role_play_session.specified_task_prompt}\n")
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")
    chat_turn_limit, n = 10, 0
    assistant_msg, _ = role_play_session.init_chat()
    #print(assistant_msg)

    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(
            assistant_msg)

        if assistant_response.terminated:
            print(Fore.GREEN +
                  ("AI Assistant terminated. Reason: "
                   f"{assistant_response.info['termination_reasons']}."))
            break
        if user_response.terminated:
            print(Fore.GREEN +
                  ("AI User terminated. "
                   f"Reason: {user_response.info['termination_reasons']}."))
            break

        print_text_animated(Fore.BLUE +
                            f"AI User:\n\n{user_response.msg.content}\n")
        print_text_animated(Fore.GREEN +
                            f"AI Assistant:\n\n{assistant_response.msg.content}\n")

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break


if __name__ == "__main__":
    main()
