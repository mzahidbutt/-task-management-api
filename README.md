# 🚀 Task Management API - AI-Native Development Project

> **Panaversity Quarter 4 Project** | Production-ready FastAPI with AI-powered development skills

A complete Task Management API built using modern Python technologies and AI-native development workflows. This project demonstrates professional software engineering practices including automated development workflows, comprehensive testing, and cloud database integration.

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128.0+-009688.svg)](https://fastapi.tiangolo.com)
[![SQLModel](https://img.shields.io/badge/SQLModel-0.0.22+-red.svg)](https://sqlmodel.tiangolo.com)
[![Tests](https://img.shields.io/badge/tests-36%20passed-success.svg)](./task-api/tests/)
[![Coverage](https://img.shields.io/badge/coverage-99%25-brightgreen.svg)](./task-api/tests/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Project Architecture](#-project-architecture)
- [AI Skills Created](#-ai-skills-created)
- [Tech Stack](#-tech-stack)
- [Quick Start](#-quick-start)
- [API Documentation](#-api-documentation)
- [Testing](#-testing)
- [Project Structure](#-project-structure)
- [Development Workflow](#-development-workflow)
- [Demo Video](#-demo-video)
- [What I Learned](#-what-i-learned)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Overview

This project showcases **AI-native development** by creating reusable skills that automate repetitive development tasks. It includes a production-ready Task Management API with full CRUD operations, comprehensive test coverage, and cloud database integration.

### Project Goals

1. ✅ **Create 5 Reusable AI Skills** (3 technical + 2 workflow)
2. ✅ **Build Complete CRUD API** using FastAPI + SQLModel
3. ✅ **Implement TDD Practices** with comprehensive test coverage
4. ✅ **Deploy to Cloud Database** using Neon PostgreSQL
5. ✅ **Demonstrate Professional Practices** with 99% test coverage

---

## ✨ Key Features

### Task Management API
- **Complete CRUD Operations** - Create, Read, Update, Delete tasks
- **Advanced Filtering** - Filter by status, creator, with pagination
- **Cloud Database** - Neon PostgreSQL with SQLModel ORM
- **Interactive Documentation** - Auto-generated Swagger/OpenAPI docs
- **Health Checks** - API and database health monitoring
- **Type Safety** - Full type hints with Pydantic validation

### AI Development Skills
- **Workflow Automation** - Skills that orchestrate other skills
- **Best Practices Built-in** - Automated quality assurance
- **Reusable Components** - DRY principle for development
- **TDD Support** - Test-driven development workflow

### Quality Assurance
- **36 Comprehensive Tests** - All CRUD operations covered
- **99% Code Coverage** - High confidence in code quality
- **Automated Testing** - Fast in-memory test database
- **CI/CD Ready** - Tests can run in pipeline

---

## 🏗️ Project Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    CLIENT (Browser/API)                  │
└─────────────────────┬───────────────────────────────────┘
                      │ HTTP Requests
                      ▼
┌─────────────────────────────────────────────────────────┐
│                   FASTAPI APPLICATION                    │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │   Routes    │  │  Validation  │  │ Error Handler │  │
│  │  (CRUD API) │──│  (Pydantic)  │──│   (HTTPExc)   │  │
│  └─────────────┘  └──────────────┘  └───────────────┘  │
└─────────────────────┬───────────────────────────────────┘
                      │ Database Operations
                      ▼
┌─────────────────────────────────────────────────────────┐
│                    SQLMODEL ORM                          │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │   Models    │  │   Session    │  │    Queries    │  │
│  │   (Task)    │──│  Management  │──│   (Select)    │  │
│  └─────────────┘  └──────────────┘  └───────────────┘  │
└─────────────────────┬───────────────────────────────────┘
                      │ SQL Queries
                      ▼
┌─────────────────────────────────────────────────────────┐
│              NEON POSTGRESQL (Cloud)                     │
│                    Tasks Table                           │
└─────────────────────────────────────────────────────────┘
```

### Skills Architecture

```
┌──────────────────────────────────────────────┐
│         WORKFLOW SKILLS (Orchestrators)       │
│  ┌──────────────────┐  ┌─────────────────┐  │
│  │ API Feature Dev  │  │  TDD Workflow   │  │
│  │    Workflow      │  │                 │  │
│  └────────┬─────────┘  └────────┬────────┘  │
└───────────┼──────────────────────┼───────────┘
            │                      │
            │ Calls                │ Calls
            ▼                      ▼
┌──────────────────────────────────────────────┐
│         TECHNICAL SKILLS (Building Blocks)    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ SQLModel │  │ FastAPI  │  │  pytest  │  │
│  │  Skill   │  │  Skill   │  │  Skill   │  │
│  └──────────┘  └──────────┘  └──────────┘  │
└──────────────────────────────────────────────┘
```

---

## 🤖 AI Skills Created

### Technical Skills (3)

#### 1. SQLModel Skill
Database design and management using SQLModel ORM.

**Capabilities:**
- Create database models with type hints
- Define relationships (foreign keys)
- Set up indexes for performance
- Handle migrations
- Query optimization

#### 2. FastAPI Skill
Build REST API endpoints with FastAPI framework.

**Capabilities:**
- Create CRUD endpoints
- Pydantic request/response models
- Automatic OpenAPI documentation
- Request validation
- Error handling

#### 3. pytest Skill
Comprehensive testing with pytest framework.

**Capabilities:**
- Write unit tests
- Integration tests
- Test fixtures
- Coverage reports
- Parametrized tests

### Workflow Skills (2)

#### 4. API Feature Development Workflow
End-to-end workflow for building complete API features.

**Steps:** Requirements → Database (SQLModel) → API (FastAPI) → Tests (pytest) → Verification → Review

**Benefits:** Systematic approach, best practices built-in, consistent quality

#### 5. TDD Workflow
Test-Driven Development using Red-Green-Refactor cycle.

**Cycle:** 🔴 Write test → 🟢 Implement → 🔵 Refactor → 🔁 Repeat

**Benefits:** Higher code quality, catch bugs early, better design, confidence to refactor

---

## 🛠️ Tech Stack

- **FastAPI** (0.128.0+) - Modern, fast web framework
- **SQLModel** (0.0.22+) - SQL databases with Python type hints
- **Neon PostgreSQL** - Serverless PostgreSQL cloud database
- **pytest** (9.0.2+) - Testing framework
- **uv** - Fast Python package manager
- **Python 3.12+** - Latest stable Python

---

## 🚀 Quick Start

### Prerequisites

```bash
# Check Python version (3.12+ required)
python --version

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd Pana_project/task-api
```

2. **Install dependencies**
```bash
uv sync
```

3. **Configure environment**
```bash
# Edit .env and add your Neon database URL
# DATABASE_URL=postgresql://user:pass@host/db?sslmode=require
```

4. **Start the server**
```bash
uv run uvicorn main:app --reload
```

5. **Open API documentation**
```
http://localhost:8000/docs
```

---

## 📚 API Documentation

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API health check |
| GET | `/health/db` | Database connection check |
| POST | `/tasks` | Create a new task |
| GET | `/tasks` | List all tasks (with filters) |
| GET | `/tasks/{task_id}` | Get specific task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

### Example: Create Task

**Request:**
```http
POST /tasks
Content-Type: application/json

{
  "complain_no": "TASK001",
  "complain_remarks": "System not responding",
  "complain_status": "pending",
  "created_by": "john_doe"
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "complain_no": "TASK001",
  "complain_remarks": "System not responding",
  "complain_status": "pending",
  "created_by": "john_doe"
}
```

### Query Parameters

- `status` - Filter by task status
- `created_by` - Filter by creator
- `skip` - Pagination offset (default: 0)
- `limit` - Results per page (default: 100)

---

## 🧪 Testing

### Run All Tests

```bash
cd task-api
uv run pytest tests/ -v
```

**Expected:** 36 passed in 36.24s

### Test Coverage

```bash
uv run pytest tests/ --cov=. --cov-report=term-missing
```

**Expected:** 99% coverage

### Test Categories

- **CREATE Tests** (5) - Task creation with validation
- **READ Tests** (11) - List, filter, pagination, get by ID
- **UPDATE Tests** (6) - Full/partial updates, validations
- **DELETE Tests** (4) - Delete, verify, error cases
- **Integration Tests** (3) - Complete workflows
- **Edge Cases** (7) - Special characters, long strings, boundary values

---

## 📁 Project Structure

```
Pana_project/
├── task-api/                          # Main API application
│   ├── main.py                        # FastAPI application
│   ├── .env                           # Environment variables
│   ├── pyproject.toml                 # Dependencies
│   └── tests/                         # Test suite (36 tests)
│
├── .claude/skills/                    # AI Skills
│   ├── fastapi-builder/               # Technical skill
│   ├── pytest-skill/                  # Technical skill
│   ├── sqlmodel-skill/                # Technical skill
│   ├── api-feature-workflow/          # Workflow skill
│   └── tdd-workflow/                  # Workflow skill
│
├── *.skill                            # Packaged skills
├── DEMO_*.md                          # Demo video guides
└── README.md                          # This file
```

---

## 💼 Development Workflow

### Using API Feature Development Workflow

```
Input: "Add comments to tasks"

Workflow:
1. Understand requirements
2. SQLModel skill → Create Comments table
3. FastAPI skill → Create comment endpoints
4. pytest skill → Write tests
5. Manual verification
6. Code review

Output: Complete feature with tests ✅
```

### Using TDD Workflow

```
Input: "Add priority field"

Cycle:
1. 🔴 Write failing test (pytest)
2. 🟢 Add field (SQLModel + FastAPI)
3. 🔵 Refactor (add enum validation)
4. Tests pass ✅

Output: High-quality feature ✅
```

---

## 🎬 Demo Video

> **Demo Video Link:** [Add your video link here]

**Duration:** 90 seconds

**Content:**
- 5 AI skills overview
- Workflow orchestration
- API demonstration
- Test results (36 passed, 99% coverage)

---

## 🎓 What I Learned

### Technical Skills
- FastAPI development and REST API design
- SQLModel ORM and database management
- Test-Driven Development practices
- Cloud database integration (Neon)
- Python type hints and validation

### Professional Practices
- Workflow automation with AI skills
- Code quality and testing standards
- Documentation and communication
- Project management and planning
- Systematic development approach

---

## 🚀 Future Enhancements

- [ ] User authentication (JWT)
- [ ] Task assignment to team members
- [ ] Priority levels and categories
- [ ] File attachments
- [ ] Email notifications
- [ ] Docker deployment
- [ ] CI/CD pipeline
- [ ] API rate limiting

---

## 📄 License

This project is licensed under the MIT License.

---

## 📧 Contact

**[Your Name]**
- Email: [your.email@example.com]
- LinkedIn: [linkedin.com/in/yourprofile]
- GitHub: [github.com/yourusername]

---

## 🙏 Acknowledgments

- **Panaversity** - Comprehensive curriculum and guidance
- **FastAPI** - Excellent web framework
- **SQLModel** - Making SQLAlchemy easier
- **Neon** - Serverless PostgreSQL
- **Claude Code** - AI-native development capabilities

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| Lines of Code | ~1,200 |
| Test Coverage | 99% |
| API Endpoints | 7 |
| Skills Created | 5 |
| Tests Written | 36 |
| Development Time | 4 weeks |

---

<div align="center">

**Built with ❤️ for Panaversity Quarter 4 Project**

⭐ Star this repo if you found it helpful!

[Demo Video](#) | [Documentation](#-api-documentation) | [Tests](#-testing)

</div>

---

**Last Updated:** January 2026
**Status:** ✅ Complete and Ready for Submission
