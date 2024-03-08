import os
from crewai import Agent, Task, Crew
from langchain_community.llms.ollama import Ollama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import DuckDuckGoSearchResults

os.environ["OPENAI_API_KEY"] = "YOUR KEY"

# Use Open AI api driver to integrate with any openai api compliant (such as text-gen etc..)
os.environ["OPENAI_API_BASE"] = "http://127.0.0.1:5000/v1"

llm = Ollama(model="mixtral:8x7b")
# llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7)

search_tool = DuckDuckGoSearchRun()

# Define your agents with roles and goals
researcher = Agent(
  role='Senior Research Analyst',
  goal='Uncover cutting-edge developments in AI and data science',
  backstory="""You work at a leading tech think tank.
  Your expertise lies in identifying emerging trends.
  You have a knack for dissecting complex data and presenting
  actionable insights.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool],
  llm=llm
)
writer = Agent(
  role='Tech Content Strategist',
  goal='Craft compelling content on tech advancements',
  backstory="""You are a renowned Content Strategist, known for
  your insightful and engaging articles.
  You transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=True,
  llm=llm
)

# Create tasks for your agents
task1 = Task(
  description="""Conduct a comprehensive analysis of the latest advancements in AI in 2024.
  Identify key trends, breakthrough technologies, and potential industry impacts.
  Your final answer MUST be a full analysis report""",
  agent=researcher,
  expected_output="Full analysis report in bullet points",
)

task2 = Task(
  description="""Using the insights provided, develop an engaging blog
  post that highlights the most significant AI advancements.
  Your post should be informative yet accessible, catering to a tech-savvy audience.
  Make it sound cool, avoid complex words so it doesn't sound like AI.
  Your final answer MUST be the full blog post of at least 4 paragraphs.""",
  agent=writer,
  expected_output="Full analysis report in bullet points",
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2,  # You can set it to 1 or 2 to different logging levels
  share_crew=False,  # share telemetry with crew ai team.
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
