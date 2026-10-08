def build_prompt(technique, task):

    if technique == "Zero-Shot":
        return f"""
You are an intelligent AI assistant.

Answer the user's task using your own knowledge.
Do not use any examples.

User Task:
{task}

Give a clear and useful answer.
""".strip()


    if technique == "One-Shot":
        return f"""
You are an AI assistant.

Follow the format shown in this example.

Example:
Question: What is Database?
Answer: A database is an organized collection of
data that can be easily stored, managed, and accessed.

Now answer the following question:

Question:
{task}

Answer:
""".strip()


    if technique == "Few-Shot":
        return f"""
You are an AI assistant.

Learn from the following examples.

Example 1:
Question: What is Java?
Answer: Java is an object-oriented programming language.

Example 2:
Question: What is SQL?
Answer: SQL is used to store, retrieve, and manage data
in relational databases.

Example 3:
Question: What is Cloud Computing?
Answer: Cloud computing provides computing resources
such as storage and servers through the internet.

Now answer this question:

Question:
{task}

Answer:
""".strip()


    if technique == "CoT":
        return f"""
You are a problem-solving AI assistant.

Analyze the given task carefully.
Identify the important points and solve the problem
using logical reasoning.

Give only the final answer and a short explanation.
Do not reveal private or internal chain-of-thought.

Task:
{task}

Final Answer:
""".strip()


    if technique == "Manual CoT":
        return f"""
You are an AI assistant.

Follow these instructions while solving the task:

1. Understand what the user is asking.
2. Find the important details.
3. Choose a suitable method.
4. Apply the method to solve the task.
5. Check the result.
6. Provide a clear final answer.

Task:
{task}

Answer:
""".strip()


    if technique == "ToT":
        return f"""
You are an advanced problem-solving assistant.

Explore different possible ways to solve the task.

Solution 1:
Think of the first possible approach.

Solution 2:
Consider another possible approach.

Solution 3:
Consider an alternative approach if needed.

Compare the possible approaches and choose
the most suitable solution.

Provide only the final answer and a short explanation.
Do not reveal private or internal chain-of-thought.

Task:
{task}

Final Answer:
""".strip()


    raise ValueError(
        "Unknown prompting technique: " + technique
    )
