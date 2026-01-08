# Demo Video Script - Task Management API Project
## Panaversity Project Submission

**Total Duration:** 90 seconds
**Target Audience:** Instructors & reviewers
**Goal:** Showcase skills, API functionality, and professional development practices

---

## 🎬 FULL SCRIPT WITH TIMING

### SCENE 1: INTRODUCTION (0:00 - 0:10) - 10 seconds

**VISUAL:** Show project folder structure or IDE with files visible

**SCRIPT:**
> "Hi! I'm Muhammad Zahid Butt, and this is my Task Management API project for Panaversity.
> I built 5 AI-powered skills and a production-ready FastAPI application.
> Let me show you what I created."

**ACTIONS:**
- Speak clearly and confidently
- Have IDE/VS Code open with project visible
- Show task-api folder structure briefly

---

### SCENE 2: SKILLS OVERVIEW (0:10 - 0:25) - 15 seconds

**VISUAL:** Show skills folder with .skill files

**SCRIPT:**
> "I created 5 reusable skills: 3 technical skills for FastAPI, pytest, and SQLModel...
> Plus 2 workflow skills that automate complete feature development.
> These skills work together - the workflow skills orchestrate the technical skills automatically."

**ACTIONS:**
```bash
# Navigate to skills directory
cd .claude/skills

# Show skill files
ls -la *.skill
```

**SHOW ON SCREEN:**
```
Technical Skills (3):
✓ fastapi-builder.skill
✓ pytest-skill.skill
✓ sqlmodel-skill.skill

Workflow Skills (2):
✓ api-feature-workflow.skill
✓ tdd-workflow.skill
```

---

### SCENE 3: WORKFLOW IN ACTION (0:25 - 0:40) - 15 seconds

**VISUAL:** Terminal showing skill invocation OR quick file preview

**SCRIPT:**
> "Here's the API Feature Development workflow in action.
> It automatically calls SQLModel to design the database,
> FastAPI to build endpoints, and pytest to write tests.
> Everything following best practices."

**OPTION A - Show file contents:**
```bash
# Quick preview of workflow skill
cat .claude/skills/api-feature-workflow/SKILL.md | head -20
```

**OPTION B - Show the workflow steps:**
**SHOW ON SCREEN (as overlay):**
```
API Feature Development Workflow:
Step 1: Requirements → ✓
Step 2: Database Design → SQLModel skill
Step 3: API Creation → FastAPI skill
Step 4: Testing → pytest skill
Step 5: Verification → ✓
```

---

### SCENE 4: TASK API DEMO (0:40 - 1:10) - 30 seconds

**VISUAL:** Split screen or switch between terminal and browser

#### Part A: Start Server (5 seconds)

**SCRIPT:**
> "Now let's see the Task API in action. Starting the server..."

**ACTIONS:**
```bash
cd task-api
uv run uvicorn main:app --reload
```

**WAIT:** 2-3 seconds for server to start

---

#### Part B: Interactive API Docs (10 seconds)

**SCRIPT:**
> "Opening the interactive documentation at localhost:8000/docs..."

**ACTIONS:**
- Open browser to `http://localhost:8000/docs`
- Scroll to show all endpoints

**SHOW ON SCREEN:**
```
✓ POST /tasks     - Create
✓ GET /tasks      - List all
✓ GET /tasks/{id} - Get one
✓ PUT /tasks/{id} - Update
✓ DELETE /tasks/{id} - Delete
```

---

#### Part C: Create Task (8 seconds)

**SCRIPT:**
> "Let's create a task. I'll use the Try it out feature..."

**ACTIONS:**
1. Click on `POST /tasks`
2. Click "Try it out"
3. Enter sample data:
```json
{
  "complain_no": "DEMO001",
  "complain_remarks": "Video demo task",
  "complain_status": "pending",
  "created_by": "demo_user"
}
```
4. Click "Execute"
5. Show 201 response with ID

---

#### Part D: Show Database Connection (7 seconds)

**SCRIPT:**
> "The API connects to Neon cloud database with SQLModel.
> Let me get that task back..."

**ACTIONS:**
1. Click on `GET /tasks/{id}`
2. Enter the ID from previous response
3. Click "Execute"
4. Show 200 response with task data

**ALTERNATIVE:** Show the list endpoint
```bash
# Or show in terminal
curl http://localhost:8000/tasks
```

---

### SCENE 5: TESTS RUNNING (1:10 - 1:20) - 10 seconds

**VISUAL:** Terminal with pytest running

**SCRIPT:**
> "The API has comprehensive test coverage. Running all 36 tests now..."

**ACTIONS:**
```bash
# In a new terminal (or stop server with Ctrl+C)
cd task-api
uv run pytest tests/ -v --tb=no
```

**SHOW:** Tests running and passing (can speed up 2x in editing)

**EXPECTED OUTPUT:**
```
36 passed in 36.24s
99% code coverage
```

---

### SCENE 6: CLOSING (1:20 - 1:30) - 10 seconds

**VISUAL:** Return to IDE or show project summary

**SCRIPT:**
> "That's my complete project: 5 AI skills automating development,
> a production-ready FastAPI with SQLModel and Neon database,
> and comprehensive pytest coverage.
> Thank you for watching!"

**SHOW ON SCREEN (final slide):**
```
Project Summary:
✓ 5 Reusable Skills (3 tech + 2 workflow)
✓ Complete CRUD API (FastAPI + SQLModel)
✓ Cloud Database (Neon PostgreSQL)
✓ 36 Tests (99% coverage)
✓ Professional Development Practices

[Your Name]
Panaversity Quarter 4 Project
```

---

## 📋 QUICK REFERENCE CARD

### Pre-Recording Checklist
```
□ Close all unnecessary applications
□ Clear terminal history (clear or cls)
□ Restart FastAPI server to ensure clean state
□ Test database has sample data OR is empty
□ Browser has docs page ready (http://localhost:8000/docs)
□ All terminal tabs ready
□ Test commands work before recording
□ Check audio levels
□ Good lighting if showing face
□ Timer/stopwatch ready
```

---

### Commands Quick Copy-Paste

```bash
# Scene 2: Show skills
cd .claude/skills
ls -la *.skill

# Scene 4: Start server
cd task-api
uv run uvicorn main:app --reload

# Scene 4: Test endpoint (alternative)
curl http://localhost:8000/tasks

# Scene 5: Run tests
cd task-api
uv run pytest tests/ -v --tb=no

# Or with coverage
uv run pytest tests/ --cov=. --cov-report=term
```

---

### Sample Task Data (Copy-Paste Ready)

```json
{
  "complain_no": "DEMO001",
  "complain_remarks": "This is a demo task for video presentation",
  "complain_status": "pending",
  "created_by": "demo_user"
}
```

```json
{
  "complain_no": "URGENT999",
  "complain_remarks": "High priority complaint",
  "complain_status": "pending",
  "created_by": "admin"
}
```

---

## 🎥 SHOT-BY-SHOT BREAKDOWN

### Shot 1: Title Slide (2 seconds)
**Text on screen:**
```
Task Management API
Panaversity Q4 Project
By [Your Name]
```

### Shot 2: IDE Overview (3 seconds)
**Show:** Project folder structure
**Highlight:**
- task-api/
- .claude/skills/
- tests/

### Shot 3: Skills Files (5 seconds)
**Show:** Terminal with skill files
**Command:** `ls -la .claude/skills/*.skill`

### Shot 4: Workflow Preview (10 seconds)
**Option A:** Show SKILL.md file briefly
**Option B:** Animated graphic showing workflow steps

### Shot 5: Server Start (5 seconds)
**Show:** Terminal starting uvicorn
**Wait for:** "Uvicorn running on..."

### Shot 6: API Docs (5 seconds)
**Show:** Browser at /docs
**Scroll:** Show all endpoints

### Shot 7: Create Task (10 seconds)
**Show:**
1. Click POST /tasks
2. Enter data
3. Execute
4. Show response with ID=1

### Shot 8: Get Task (5 seconds)
**Show:**
1. Click GET /tasks/1
2. Execute
3. Show response data

### Shot 9: Tests Running (10 seconds)
**Show:** Terminal with pytest
**Speed up:** 2x in editing if needed
**Show result:** 36 passed

### Shot 10: Closing (5 seconds)
**Show:** Summary screen with checkmarks

### Shot 11: Thank You (2 seconds)
**Text on screen:**
```
Thank You!
[Your Email/GitHub]
```

---

## 🎭 ALTERNATIVE SCRIPTS

### SHORT VERSION (60 seconds)

**Remove/Shorten:**
- Skills overview (5s instead of 15s)
- Workflow demo (skip file preview)
- API demo (show only create, not get)
- Tests (show only final result)

**Script:**
> "Hi, I'm [Name]. I built 5 AI skills and a Task Management API.
> [Show skills files - 5s]
> Here's my FastAPI running on Neon database...
> [Create task - 15s]
> With 36 comprehensive tests...
> [Show test results - 10s]
> Production-ready with 99% coverage. Thank you!"

---

### DETAILED VERSION (90 seconds with extras)

**Add:**
- Show TDD workflow in action
- Demonstrate filtering tasks
- Show database health check
- Update a task status
- Show coverage report

---

## 🎬 FILMING TIPS

### Equipment Setup
```
✓ Good microphone (or quiet room)
✓ Screen recording software (OBS, Loom, QuickTime)
✓ 1080p resolution minimum
✓ Clear terminal font (16-18pt)
✓ High contrast theme
```

### Recording Settings
```
✓ Record at 60fps (smooth)
✓ Record full screen or selected window
✓ Show cursor (helps viewers follow)
✓ Use zoom/highlight for important parts
✓ Add background music (optional, low volume)
```

### Voice Recording
```
✓ Speak clearly and moderately paced
✓ Pause briefly between sections
✓ Smile (it shows in voice!)
✓ Re-record sections if needed
✓ Remove "um" and "uh" in editing
```

### Editing
```
✓ Cut out delays/loading times
✓ Speed up slow parts (tests running)
✓ Add text overlays for key points
✓ Add transitions between scenes
✓ Add music fade in/out
✓ Export in MP4 format
```

---

## 📝 SCRIPT VARIATIONS

### Variation A: Technical Focus

**Emphasize:**
- SQLModel ORM features
- FastAPI automatic documentation
- Pytest fixtures and coverage
- Neon cloud database

### Variation B: Workflow Focus

**Emphasize:**
- How workflow skills orchestrate technical skills
- Automation of repetitive tasks
- TDD methodology
- Best practices built-in

### Variation C: Results Focus

**Emphasize:**
- 99% test coverage
- Production-ready code
- Professional development practices
- Reusable automation

---

## 🎯 KEY MESSAGES TO CONVEY

1. **Skills Created:** 5 reusable skills (3 technical, 2 workflow)
2. **Automation:** Workflows orchestrate technical skills
3. **API Working:** Complete CRUD with FastAPI + SQLModel
4. **Cloud Database:** Using Neon PostgreSQL
5. **Quality:** 36 tests, 99% coverage
6. **Professional:** Production-ready, best practices

---

## ⏱️ TIMING BREAKDOWN

```
Introduction:           10s  (11%)
Skills Overview:        15s  (17%)
Workflow Demo:          15s  (17%)
API Demo:              30s  (33%)
  - Start server:       5s
  - Show docs:          10s
  - Create task:        8s
  - Get task:           7s
Tests Running:         10s  (11%)
Closing:               10s  (11%)
────────────────────────────
TOTAL:                 90s  (100%)
```

---

## 🚀 PRACTICE SCHEDULE

### Run-Through 1: Read script (10 min)
- Familiarize with flow
- Time each section
- Identify difficult parts

### Run-Through 2: Commands (15 min)
- Test all commands work
- Verify outputs
- Screenshot expected results

### Run-Through 3: Full rehearsal (20 min)
- Do complete run with timer
- Don't record yet
- Note what needs adjustment

### Run-Through 4: Record attempt 1 (25 min)
- Record with audio
- Review and critique
- List improvements

### Run-Through 5: Final recording (30 min)
- Record best version
- Basic editing
- Export and review

---

## 📊 WHAT TO SHOW VS WHAT TO SAY

### SHOW (Visual Priority)
```
✓ Skill files existing
✓ API documentation interface
✓ Creating a task
✓ Response with data
✓ Tests passing
✓ Coverage report
```

### SAY (Audio Priority)
```
✓ Project overview
✓ Skills purpose
✓ How workflows automate
✓ Technology stack
✓ Quality metrics
```

### DON'T SHOW/SAY
```
✗ Code implementation details
✗ Installation steps
✗ Troubleshooting
✗ Failed attempts
✗ Apologies or uncertainties
```

---

## 🎬 FINAL CHECKLIST

**Before Recording:**
```
□ Script memorized or on second screen
□ Timer visible
□ All commands tested
□ Server can start cleanly
□ Tests pass
□ Browser ready
□ Audio tested
□ Lighting checked
□ Notifications off
□ Phone on silent
```

**During Recording:**
```
□ Start timer
□ Speak clearly
□ Follow script timing
□ Show key visuals
□ Stay on pace
□ Smile (voice shows it!)
```

**After Recording:**
```
□ Review full video
□ Check audio quality
□ Verify all key points shown
□ Edit as needed
□ Add text overlays
□ Export in HD
□ Test exported file
□ Upload to submission platform
```

---

## 💡 PRO TIPS

1. **Practice 3-5 times** before recording
2. **Record multiple takes** - pick the best
3. **Speed up boring parts** in editing (2x tests running)
4. **Add captions** for accessibility
5. **Use text overlays** to highlight key points
6. **Keep energy high** - enthusiasm is contagious
7. **Show results, not process** - viewers want to see it work
8. **End strong** - summary slide leaves lasting impression

---

## 🎥 SOFTWARE RECOMMENDATIONS

### Screen Recording
- **OBS Studio** (Free, powerful)
- **Loom** (Easy, cloud-based)
- **ShareX** (Free, Windows)
- **QuickTime** (Mac built-in)
- **Camtasia** (Professional, paid)

### Video Editing
- **DaVinci Resolve** (Free, professional)
- **iMovie** (Mac, free)
- **OpenShot** (Free, cross-platform)
- **Shotcut** (Free, simple)
- **Adobe Premiere** (Professional, paid)

### Audio
- **Audacity** (Free audio editing)
- **Built-in laptop mic** (acceptable)
- **External USB mic** (better quality)

---

## 📤 EXPORT SETTINGS

```
Format:        MP4
Codec:         H.264
Resolution:    1920x1080 (1080p)
Frame Rate:    30fps or 60fps
Bitrate:       5-10 Mbps
Audio:         AAC, 192kbps
File Size:     Keep under 100MB if possible
```

---

## ✨ INSPIRATION QUOTES FOR CONFIDENCE

> "This project showcases professional development practices."

> "These skills automate what I used to do manually."

> "Production-ready code with comprehensive testing."

> "AI-native development workflow in action."

---

## 🎓 SUBMISSION PLATFORM NOTES

Check your submission requirements:
- Maximum file size
- Accepted formats
- Upload method (YouTube link, direct upload, etc.)
- Whether captions are required
- Resolution requirements

---

Good luck with your demo video! You've built something impressive - now show it with confidence! 🚀
