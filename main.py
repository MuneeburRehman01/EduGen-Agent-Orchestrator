import os
from typing import List, Dict
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class EduGenOrchestrator:
    def __init__(self, model_name: str = "gpt-4"):
        self.llm = ChatOpenAI(model=model_name, temperature=0.7)
        self.agents = {}

    def create_learning_path(self, subject: str) -> Dict:
        """Generates a structured learning path for a given subject."""
        prompt = f"Create a 5-step detailed learning path for: {subject}. Include objectives for each step."
        response = self.llm.invoke(prompt)
        return {"subject": subject, "path": response.content}

    def generate_assessment(self, module_content: str) -> str:
        """Generates 3 multiple choice questions based on content."""
        prompt = f"Generate 3 MCQ questions with answers based on this content: {module_content}"
        response = self.llm.invoke(prompt)
        return response.content

if __name__ == "__main__":
    orchestrator = EduGenOrchestrator()
    path = orchestrator.create_learning_path("Machine Learning Architectures")
    print(f"Generated Path for {path['subject']}:\n{path['path']}")