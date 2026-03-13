# 🎓 EduGen-Agent-Orchestrator

[![AI Engineering](https://img.shields.io/badge/Focus-AI%20Engineering-blue.svg)]()
[![LangChain](https://img.shields.io/badge/Framework-LangChain-green.svg)]()
[![Python](https://img.shields.io/badge/Language-Python%203.9+-yellow.svg)]()

EduGen is an advanced **Multi-Agent Orchestrator** designed to revolutionize personalized education. It leverages Large Language Models (LLMs) to dynamically generate tailored learning paths, interactive study materials, and real-time knowledge assessments.

## 🌟 Key Features

- **Agentic Pathfinding:** Uses a lead 'Orchestrator' agent to break down complex subjects into structured modules.
- **Dynamic Content Generation:** specialized agents for generating quizzes, summaries, and deep-dive explanations.
- **Adaptive Feedback Loop:** Evaluates user responses to adjust the difficulty and focus of subsequent learning materials.
- **Multi-Model Support:** Seamlessly integrates with OpenAI (GPT-4), Anthropic (Claude), and local models via LangChain.

## 🛠️ Architecture

The system operates on a hub-and-spoke model where the **Orchestrator** delegates tasks to specialized sub-agents:

1.  **Curriculum Designer Agent:** Maps out the pedagogical structure.
2.  **Content Creator Agent:** Generates detailed text, examples, and code snippets.
3.  **Assessment Agent:** Designs and grades interactive evaluations.
4.  **Efficiency Monitor:** Tracks token usage and response latency.

## 🚀 Getting Started

`ash
# Clone the repository
git clone https://github.com/MuneeburRehman01/EduGen-Agent-Orchestrator.git

# Install dependencies
pip install -r requirements.txt

# Configure your environment
cp .env.example .env
# Add your API keys (OPENAI_API_KEY, etc.)

# Run the orchestrator
python main.py --subject "Quantum Computing for Beginners"
`

## 📜 Roadmap

- [ ] Integration with Vector Databases (Pinecone/Milvus) for RAG-based learning.
- [ ] Multimodal support (Generating educational diagrams via DALL-E/Stable Diffusion).
- [ ] Voice-interactive learning sessions.

---
Developed with ❤️ by [Muneeb ur Rehman](https://www.linkedin.com/in/muneeb-ur-rehman-a13977207/)