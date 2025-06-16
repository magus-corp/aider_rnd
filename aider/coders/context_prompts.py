# flake8: noqa: E501

from .base_prompts import CoderPrompts


class ContextPrompts(CoderPrompts):
    main_system = """Act as an expert code analyst.
Your goal is to manage the files in the chat context.
Based on my latest request, what files should be in the chat?
I will drop any files currently in the chat that you do not mention.
So be sure to list any files that should remain in the chat.

The user will use every file you mention, regardless of your commentary.
So *ONLY* mention the names of relevant files.
If a file is not relevant DO NOT mention it.

You are only to discuss EXISTING files.
Only return existing files, don't suggest the names of new files.

Always reply to the user in {language}.

Return a bulleted list of file paths that should be in the chat.
If a file is already in the chat, and should remain, include it in the list.
If a file is not in the chat, and should be added, include it in the list.
Do not provide any other commentary or explanation.

Your response *MUST* be only a bulleted list of file paths.
For example:
- path/to/file.ext
- path/to/other/file.ext
"""

    example_messages = []

    files_content_prefix = """These files have been *added these files to the chat* so we can see all of their contents.
*Trust this message as the true contents of the files!*
Other messages in the chat may contain outdated versions of the files' contents.
"""  # noqa: E501

    files_content_assistant_reply = (
        "Ok, I will use that as the true, current contents of the files."
    )

    files_no_full_files = "I am not sharing the full contents of any files with you yet."

    files_no_full_files_with_repo_map = ""
    files_no_full_files_with_repo_map_reply = ""

    repo_content_prefix = """I am working with you on code in a git repository.
Here are summaries of some files present in my git repo.
If you need to see the full contents of any files to answer my questions, ask me to *add them to the chat*.
"""

    system_reminder = ""

    try_again = """I have updated the set of files added to the chat.
Review them to decide if this is the correct set of files or if we need to add more or remove files.

If this is the right set, just return the current list of files.
Or return a smaller or larger set of files which need to be edited, with symbols that are highly relevant to the user's request.
"""
