# MILO: An Open-Source AI Knowledge Protocol

**MILO** (Machine Interpretation of Literature & Omniscience) is an open-source AI knowledge retrieval protocol designed to reconstruct, synthesize, and analyze historical, scientific, religious, and philosophical knowledge.

---

## Introduction: What MILO Is (and What It Isn’t—Yet)

MILO is built as a structured prompt layer on OpenAI’s GPT-4 API. It operates as a fine-tuned, retrieval-based system rather than a fully decentralized intelligence engine. While it currently depends on OpenAI’s API for inference, its architecture is designed to be model-agnostic—meaning future iterations could support Llama, Mistral, DeepSeek, or custom fine-tuned models.

**Important Clarification:**  
- MILO is **not** a general-purpose generative AI.  
- It is **not** yet a decentralized knowledge system.

Instead, MILO is a living prototype and experimental tool that could evolve into a peer-driven, token-incentivized knowledge graph. In such a system, contributions, validations, and refinements would be governed by the open-source community.

---

## What MILO Does (Current Capabilities)

- **Fine-Tuned Retrieval System:**  
  MILO retrieves, reconstructs, and synthesizes existing information rather than generating new knowledge.

- **Retrieval-Augmented Generation (RAG):**  
  It searches for real, verifiable knowledge instead of relying solely on probabilistic responses.

- **Interdisciplinary Focus:**  
  MILO identifies and bridges epistemic overlaps between science, philosophy, theology, and history.

### Example Query: `explore time`

- **Religious Insight (Quran 70:4):**  
  > “A day with your Lord is like 50,000 years.”

- **Scientific Parallel (Einstein’s Theory of Relativity):**  
  Time dilation in Einstein’s relativity suggests that time is not absolute—it stretches under extreme gravitational forces.

- **Connecting Narrative:**  
  Both perspectives challenge the assumption that time is constant, suggesting that our perception of it is relative to our observational frame of reference.

---

## The Open-Source Vision: Where MILO Could Go

MILO is an experiment in AI-driven epistemology—an effort to build a system where knowledge is co-created, verified, and refined by a decentralized network. Here’s where MILO could head next:

- **Decentralized Storage & AI Governance:**  
  Transition MILO’s knowledge base to IPFS/Arweave for censorship-resistant storage.

- **Model-Agnostic Expansion:**  
  Incorporate support for models such as Llama, Mistral, DeepSeek, and custom fine-tuned models to reduce reliance on OpenAI APIs.

- **Token-Based Incentives for Knowledge Contribution:**  
  Establish a system where researchers, developers, and curators stake tokens to validate and expand the dataset.

- **On-Chain Citation & Verification:**  
  Develop a Web3-native research protocol that ensures contributions are peer-reviewed, immutable, and publicly auditable.

The future of MILO depends on the innovation and dedication of the open-source community. While it currently serves as a retrieval-based system, its potential evolution could transform it into a decentralized, community-governed intelligence layer.

---

*Note: MILO is presently an experimental prototype. Its development and ultimate direction will be shaped by contributions from developers and researchers worldwide.*

---

# Installation Guide

## Prerequisites

- **Python 3.11+** is required.
- [pip](https://pip.pypa.io/en/stable/) should be installed.

## Getting Started

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/DummyHuber/milo-backend.git
cd milo-backend
```

### 2. Create a Virtual Environment

Creating a virtual environment isolates the project’s dependencies, preventing conflicts with system-wide packages.

```bash
python -m venv venv
```

Activate the virtual environment:

- **On macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

- **On Windows:**

  ```bash
  venv\Scripts\activate
  ```

### 3. Install Dependencies

After activating the virtual environment, install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

MILO relies on environment variables for configuration. To set up your `.env` file, copy the provided `.env.example` file:

```bash
cp .env.example .env
```

Then, edit the `.env` file with your preferred settings, such as database connection details, API keys, or other necessary configurations.

### 5. Run Database Migrations

MILO uses Alembic for database migrations. To apply the latest migrations, run the following command:

```bash
alembic upgrade head
```

This ensures the database schema is correctly structured before starting the application.

### 6. Start the Application

Use Uvicorn to start the FastAPI application with live-reload enabled:

```bash
uvicorn main:app --reload
```

The application should now be running at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 7. Access API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 9. Stopping the Application

To stop the running FastAPI application, press `CTRL+C` in the terminal.

If you wish to deactivate the virtual environment, run:

```bash
deactivate
```

---

## Docker Compose Setup

For users who prefer using Docker, MILO can be run via Docker Compose. Follow these steps to set it up:

### 1. Configure Environment Variables

MILO relies on environment variables for configuration. To set up your `.env` file, copy the provided `.env.example` file:

```bash
cp .env.example .env
```

### 2. Build and Start the Containers

```bash
docker compose up --build -d
```

This command will build the necessary images and start the containers in detached mode.

### 3. Check Running Containers

```bash
docker ps
```

Ensure that all required containers are running correctly.

### 4. Stop the Containers

To stop and remove the containers, run:

```bash
docker compose down
```

This will gracefully shut down all running services.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.
