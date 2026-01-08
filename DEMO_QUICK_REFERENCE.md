# 🎬 DEMO VIDEO QUICK REFERENCE
## One-Page Script for Recording (90 seconds)

---

## ⏱️ TIMELINE

| Time | Scene | Action | Duration |
|------|-------|--------|----------|
| 0:00 | Intro | Welcome + overview | 10s |
| 0:10 | Skills | Show 5 skill files | 15s |
| 0:25 | Workflow | Explain automation | 15s |
| 0:40 | API Demo | Create + get task | 30s |
| 1:10 | Tests | Run pytest | 10s |
| 1:20 | Close | Summary + thank you | 10s |

---

## 📜 SCRIPT (speak these exact words)

### 0:00 - INTRO (10s)
> "Hi! I'm [MUHAMMAD ZAHID BUTT, and this is my Task Management API project for Panaversity. I built 5 AI-powered skills and a production-ready FastAPI application. Let me show you what I created."

### 0:10 - SKILLS (15s)
> "I created 5 reusable skills: 3 technical skills for FastAPI, pytest, and SQLModel... Plus 2 workflow skills that automate complete feature development. These skills work together - the workflow skills orchestrate the technical skills automatically."

**SHOW:** `ls -la .claude/skills/*.skill`

### 0:25 - WORKFLOW (15s)
> "Here's the API Feature Development workflow in action. It automatically calls SQLModel to design the database, FastAPI to build endpoints, and pytest to write tests. Everything following best practices."

**SHOW:** Workflow file or diagram

### 0:40 - API (30s)
> "Now let's see the Task API in action. Starting the server..."

**RUN:** `uv run uvicorn main:app --reload`

> "Opening the interactive documentation at localhost:8000/docs..."

**SHOW:** Browser, create task with demo data

> "The API connects to Neon cloud database with SQLModel. Let me get that task back..."

**SHOW:** Get task by ID

### 1:10 - TESTS (10s)
> "The API has comprehensive test coverage. Running all 36 tests now..."

**RUN:** `uv run pytest tests/ -v --tb=no`

**SHOW:** 36 passed, 99% coverage

### 1:20 - CLOSE (10s)
> "That's my complete project: 5 AI skills automating development, a production-ready FastAPI with SQLModel and Neon database, and comprehensive pytest coverage. Thank you for watching!"

**SHOW:** Summary slide

---

## 💻 COMMANDS (copy-paste ready)

```bash
# Terminal 1: Show skills
cd .claude/skills && ls -la *.skill

# Terminal 2: Start API server
cd task-api && uv run uvicorn main:app --reload

# Terminal 3: Run tests
cd task-api && uv run pytest tests/ -v --tb=no

# Browser: Open docs
http://localhost:8000/docs
```

---

## 📝 DEMO TASK DATA

```json
{
  "complain_no": "DEMO001",
  "complain_remarks": "Video demo task",
  "complain_status": "pending",
  "created_by": "demo_user"
}
```

---

## ✅ PRE-RECORDING CHECKLIST

```
□ Clear terminal history (clear/cls)
□ Close unnecessary apps
□ Test all commands work
□ Browser at localhost:8000/docs
□ Timer ready
□ Mic tested
□ Notifications OFF
□ Phone silent
□ Good lighting
□ Script on second screen
```

---

## 🎯 KEY POINTS TO HIT

1. ✓ **5 skills** (3 technical + 2 workflow)
2. ✓ **Automation** (workflows orchestrate)
3. ✓ **API works** (FastAPI + SQLModel)
4. ✓ **Cloud DB** (Neon PostgreSQL)
5. ✓ **Quality** (36 tests, 99% coverage)

---

## 🚨 COMMON MISTAKES TO AVOID

- ❌ Going too fast or too slow
- ❌ Saying "um" or "uh"
- ❌ Apologizing or sounding uncertain
- ❌ Showing errors or troubleshooting
- ❌ Going over 90 seconds
- ❌ Low audio volume
- ❌ Small terminal font
- ❌ Forgetting to show key visuals

---

## 💡 QUICK TIPS

- **Energy:** Sound enthusiastic!
- **Pace:** Clear and moderate
- **Pauses:** Brief pauses between sections
- **Practice:** 3-5 run-throughs before recording
- **Multiple takes:** Record 2-3 times, pick best
- **Smile:** It shows in your voice!

---

## 🎬 VISUAL PRIORITY

**MUST SHOW:**
1. Skill files (5 .skill files)
2. API docs interface (/docs)
3. Create task succeeding
4. Get task response
5. Tests passing (36 passed)

**NICE TO SHOW:**
- Project folder structure
- Workflow file preview
- Coverage report
- Final summary slide

---

## 📊 EXPECTED OUTPUTS

### Skills Command
```
✓ fastapi-builder.skill
✓ pytest-skill.skill
✓ sqlmodel-skill.skill
✓ api-feature-workflow.skill
✓ tdd-workflow.skill
```

### Server Start
```
INFO: Uvicorn running on http://127.0.0.1:8000
INFO: Application startup complete.
```

### Create Task Response
```json
{
  "id": 1,
  "complain_no": "DEMO001",
  "complain_remarks": "Video demo task",
  "complain_status": "pending",
  "created_by": "demo_user"
}
```

### Test Results
```
====== 36 passed in 36.24s ======
Coverage: 99%
```

---

## 🎥 FINAL REMINDERS

1. **Breathe** - You've got this!
2. **Timer** - Keep track of time
3. **Energy** - Stay enthusiastic
4. **Show** - Visuals > talking
5. **Confidence** - You built something great!

---

## 📤 AFTER RECORDING

```
□ Watch full video
□ Check audio clear
□ Verify key points shown
□ Edit if needed
□ Add text overlays
□ Export as MP4 (1080p)
□ Test exported file plays
□ Submit!
```

---

**Good luck! 🚀 You've built something impressive - now show it!**
