# ilmBot MVP

**ilmBot** — an AI-powered assistant designed to help students in **Pakistan** learn English more effectively.

This approach enables me to:
- Make long-term technical and architectural decisions.
- Select appropriate AI models with thoughtful configurations.
- Build a minimum viable product (MVP) grounded in real-world utility.

For further context and motivation, see the [`documents/`](./documents/) folder, which contains the **technical specification**.

---

## 🚀 Setup & Running Guide

### 1. Set Environment Variables

Start by copying the environment variable template:

```bash
cp env.template .env
```

> 🔑 **IMPORTANT**: Set your `OPENROUTER_API_KEY` in the `.env` file.  
You can create it here: [https://openrouter.ai/settings/keys](https://openrouter.ai/sign-in?redirect_url=https%3A%2F%2Fopenrouter.ai%2Fsettings%2Fkeys)

---

### 2. Local Development Setup

If you want to contribute or run the project locally:

#### ✅ Prerequisites:
- Python: `3.12`
- Poetry: `2.1.1`

#### ⬇️ Setup Commands:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install poetry==2.1.1
poetry install
```

Install pre-commit hooks:
```bash
poetry run pre-commit install
```

---

### 3. Run with Docker

A containerized setup is available for convenience.

#### ✅ Requirements:
- Docker: `v27.3.1`
- Docker Compose: `v2.29.7-desktop.1`

#### 📦 Common Docker Commands:

```bash
make build       # Build Docker images
make run         # Start the containers
make stop        # Stop running containers
make test        # Run all tests using pytest inside Docker
```

---

## 📁 Project Structure

```
.
├── documents/                     # Pitch and technical specification
├── src/
│   ├── api/
│   │   ├── routers/              # API routes
│   │   └── schemas/              # Pydantic schemas
│   ├── core/
│   │   └── services/
│   │       └── llm/
│   │           ├── providers/    # Provider implementations (e.g., OpenRouter)
│   │           └── factory.py    # LLM Factory to manage provider abstraction
│   └── tests/                    # Unit and integration tests
├── Dockerfile
├── Makefile
├── pyproject.toml
├── env.template
└── README.md
```

---

## 📚 API Documentation

Interactive API documentation is available once the server is running:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

You can also download the OpenAPI specification (JSON format) directly:

- [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

---

## 🧪 Endpoint Testing with HTTP Client

A file named `test_endpoints.http` is included to help you quickly test available API endpoints.

To use it:

1. Run the service locally using and then perform tests:

```bash
make run
```

---

## 🧠 Notes & Design Considerations

- **AI Provider Abstraction**: The LLM service is designed with a factory pattern to support multiple AI providers. This allows easy swapping or fallback strategies (e.g., OpenRouter, Anthropic, etc.).
- **Project Mapping**: Mapping the challenge to **ilmBot** gives purpose-driven development aligned with real users and educational needs.
- **Future Enhancements**:
  - Multi-language support for rural accessibility.
  - Mobile-first delivery.
  - Contextual model selection using user history.

---

### 🤝 Contributions

Feel free to explore, open issues, and contribute ideas or code.  
Let’s build something impactful for learners around the world! 🌍📚