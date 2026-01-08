# 🎬 DEMO VIDEO STORYBOARD
## Visual Shot List for 90-Second Demo

---

## 📸 SHOT-BY-SHOT GUIDE

### SHOT 1: TITLE CARD (0:00 - 0:03)
```
┌─────────────────────────────────────┐
│                                     │
│   TASK MANAGEMENT API PROJECT      │
│   Panaversity Quarter 4             │
│                                     │
│   By [Your Name]                    │
│                                     │
└─────────────────────────────────────┘
```
**Duration:** 3 seconds
**Audio:** Background music starts
**Action:** Static title slide

---

### SHOT 2: INTRODUCTION (0:03 - 0:10)
```
┌─────────────────────────────────────┐
│  VS Code / IDE                      │
│  ├── task-api/                      │
│  │   ├── main.py                    │
│  │   ├── tests/                     │
│  │   └── .env                       │
│  └── .claude/                       │
│      └── skills/                    │
│                                     │
│  [Your voiceover plays here]        │
└─────────────────────────────────────┘
```
**Duration:** 7 seconds
**Audio:** "Hi! I'm [Name]... Let me show you what I created."
**Action:** Pan through project structure

---

### SHOT 3: SKILLS FILES (0:10 - 0:18)
```
┌─────────────────────────────────────┐
│  Terminal                           │
│  $ cd .claude/skills               │
│  $ ls -la *.skill                  │
│                                     │
│  fastapi-builder.skill              │
│  pytest-skill.skill                 │
│  sqlmodel-skill.skill               │
│  api-feature-workflow.skill         │
│  tdd-workflow.skill                 │
│                                     │
└─────────────────────────────────────┘
```
**Duration:** 8 seconds
**Audio:** "I created 5 reusable skills..."
**Action:** Command execution showing 5 skill files
**Overlay Text:** "3 Technical + 2 Workflow Skills"

---

### SHOT 4: SKILLS DIAGRAM (0:18 - 0:25)
```
┌─────────────────────────────────────┐
│  Text Overlay or Diagram:          │
│                                     │
│  Technical Skills:                  │
│  ✓ FastAPI Builder                 │
│  ✓ pytest                           │
│  ✓ SQLModel                         │
│                                     │
│  Workflow Skills:                   │
│  ✓ API Feature Development          │
│  ✓ TDD Workflow                     │
│                                     │
└─────────────────────────────────────┘
```
**Duration:** 7 seconds
**Audio:** "Plus 2 workflow skills that automate..."
**Action:** Text appears with checkmarks
**Optional:** Animation showing skills connecting

---

### SHOT 5: WORKFLOW PREVIEW (0:25 - 0:33)
```
┌─────────────────────────────────────┐
│  Workflow Diagram or File:          │
│                                     │
│  API Feature Development:           │
│  1. Requirements ───→ ✓             │
│  2. Database ───→ SQLModel          │
│  3. API ───→ FastAPI                │
│  4. Tests ───→ pytest               │
│  5. Verify ───→ ✓                   │
│                                     │
└─────────────────────────────────────┘
```
**Duration:** 8 seconds
**Audio:** "Here's the workflow... calls SQLModel, FastAPI, pytest"
**Action:** Show workflow steps
**Overlay Text:** "Automated Best Practices"

---

### SHOT 6: WORKFLOW FILE (0:33 - 0:40)
```
┌─────────────────────────────────────┐
│  SKILL.md preview:                  │
│  ---                                │
│  name: api-feature-workflow         │
│  description: End-to-end...         │
│  ---                                │
│                                     │
│  ## Workflow Steps                  │
│  ### Step 1: Understand...          │
│  ### Step 2: Design Database...     │
│  ### Step 3: Create API...          │
│                                     │
└─────────────────────────────────────┘
```
**Duration:** 7 seconds
**Audio:** "...Everything following best practices"
**Action:** Quick scroll through workflow file
**Optional:** Can skip if time is tight

---

### SHOT 7: START SERVER (0:40 - 0:45)
```
┌─────────────────────────────────────┐
│  Terminal                           │
│  $ cd task-api                     │
│  $ uv run uvicorn main:app --reload│
│                                     │
│  INFO: Uvicorn running on           │
│        http://127.0.0.1:8000        │
│  INFO: Application startup complete │
│                                     │
└─────────────────────────────────────┘
```
**Duration:** 5 seconds
**Audio:** "Now let's see the Task API in action..."
**Action:** Command execution, server starts
**Note:** Can speed up in editing if slow

---

### SHOT 8: API DOCS PAGE (0:45 - 0:50)
```
┌─────────────────────────────────────┐
│  Browser: localhost:8000/docs       │
│                                     │
│  Task Complaint API                 │
│  CRUD API for managing complaints   │
│                                     │
│  ▼ POST   /tasks                    │
│  ▼ GET    /tasks                    │
│  ▼ GET    /tasks/{task_id}          │
│  ▼ PUT    /tasks/{task_id}          │
│  ▼ DELETE /tasks/{task_id}          │
│  ▼ GET    /                         │
│  ▼ GET    /health/db                │
│                                     │
└─────────────────────────────────────┘
```
**Duration:** 5 seconds
**Audio:** "Opening the interactive documentation..."
**Action:** Scroll through endpoints
**Overlay Text:** "Complete CRUD Operations"

---

### SHOT 9: CREATE TASK - OPEN (0:50 - 0:53)
```
┌─────────────────────────────────────┐
│  Browser - POST /tasks              │
│                                     │
│  ▼ POST /tasks                      │
│     Create a new task/complaint     │
│                                     │
│     [Try it out] ← CLICK            │
│                                     │
│     Request body                    │
│     complain_no        [required]   │
│     complain_remarks   [optional]   │
│     complain_status    "pending"    │
│     created_by         [required]   │
│                                     │
└─────────────────────────────────────┘
```
**Duration:** 3 seconds
**Audio:** "Let's create a task..."
**Action:** Click "Try it out" button

---

### SHOT 10: CREATE TASK - FILL (0:53 - 0:58)
```
┌─────────────────────────────────────┐
│  Request body:                      │
│  {                                  │
│    "complain_no": "DEMO001",        │
│    "complain_remarks": "Video demo",│
│    "complain_status": "pending",    │
│    "created_by": "demo_user"        │
│  }                                  │
│                                     │
│  [Execute] ← CLICK                  │
│                                     │
└─────────────────────────────────────┘
```
**Duration:** 5 seconds
**Audio:** "I'll use the Try it out feature..."
**Action:** Type or paste data, click Execute
**Note:** Pre-fill data to save time

---

### SHOT 11: CREATE RESPONSE (0:58 - 1:02)
```
┌─────────────────────────────────────┐
│  Response: 201 Created              │
│  {                                  │
│    "id": 1,                    ← ✓  │
│    "complain_no": "DEMO001",        │
│    "complain_remarks": "Video demo",│
│    "complain_status": "pending",    │
│    "created_by": "demo_user"        │
│  }                                  │
│                                     │
│  ✓ Success!                         │
│                                     │
└─────────────────────────────────────┘
```
**Duration:** 4 seconds
**Audio:** Silent or "Successfully created"
**Action:** Show 201 response
**Highlight:** The ID field

---

### SHOT 12: GET TASK (1:02 - 1:10)
```
┌─────────────────────────────────────┐
│  GET /tasks/{task_id}               │
│                                     │
│  task_id: 1                         │
│                                     │
│  [Execute]                          │
│                                     │
│  Response: 200 OK                   │
│  {                                  │
│    "id": 1,                         │
│    "complain_no": "DEMO001",        │
│    ...                              │
│  }                                  │
│                                     │
└─────────────────────────────────────┘
```
**Duration:** 8 seconds
**Audio:** "The API connects to Neon... Let me get that back"
**Action:** Get task by ID=1
**Overlay Text:** "Neon PostgreSQL + SQLModel"

---

### SHOT 13: RUN TESTS (1:10 - 1:17)
```
┌─────────────────────────────────────┐
│  Terminal                           │
│  $ cd task-api                     │
│  $ uv run pytest tests/ -v --tb=no │
│                                     │
│  tests/test_tasks.py::test_...  ✓  │
│  tests/test_tasks.py::test_...  ✓  │
│  tests/test_tasks.py::test_...  ✓  │
│  ...                                │
│  [scrolling tests]                  │
│                                     │
└─────────────────────────────────────┘
```
**Duration:** 7 seconds
**Audio:** "The API has comprehensive test coverage..."
**Action:** Tests running
**Note:** Speed up 2x in editing

---

### SHOT 14: TEST RESULTS (1:17 - 1:20)
```
┌─────────────────────────────────────┐
│  Terminal                           │
│                                     │
│  ===== test session starts =====    │
│                                     │
│  tests/test_tasks.py ............   │
│  ........................            │
│                                     │
│  ===== 36 passed in 36.24s =====    │
│                                     │
│  Coverage: 99%                      │
│                                     │
└─────────────────────────────────────┘
```
**Duration:** 3 seconds
**Audio:** "Running all 36 tests now..."
**Action:** Show final result
**Overlay Text:** "✓ 36 PASSED | 99% COVERAGE"

---

### SHOT 15: SUMMARY SLIDE (1:20 - 1:28)
```
┌─────────────────────────────────────┐
│                                     │
│  PROJECT SUMMARY                    │
│                                     │
│  ✓ 5 Reusable Skills                │
│    (3 technical + 2 workflow)       │
│                                     │
│  ✓ Complete CRUD API                │
│    (FastAPI + SQLModel)             │
│                                     │
│  ✓ Cloud Database                   │
│    (Neon PostgreSQL)                │
│                                     │
│  ✓ 36 Tests | 99% Coverage          │
│                                     │
│  ✓ Production-Ready Code            │
│                                     │
└─────────────────────────────────────┘
```
**Duration:** 8 seconds
**Audio:** "That's my complete project..."
**Action:** Static slide with checkmarks
**Animation:** Checkmarks appear one by one

---

### SHOT 16: THANK YOU (1:28 - 1:30)
```
┌─────────────────────────────────────┐
│                                     │
│                                     │
│         THANK YOU!                  │
│                                     │
│         [Your Name]                 │
│    [Your Email or GitHub]           │
│                                     │
│    Panaversity Q4 Project           │
│                                     │
│                                     │
└─────────────────────────────────────┘
```
**Duration:** 2 seconds
**Audio:** "Thank you for watching!"
**Action:** Final credits
**Music:** Fade out

---

## 🎨 VISUAL STYLE GUIDE

### Color Scheme
```
Background:    Dark theme (easier on eyes)
Text:          High contrast
Highlights:    Green for success (✓)
               Red/orange for emphasis
Terminal:      Default with good font size
```

### Font Sizes
```
Terminal:      18-20pt
Browser:       Default (but zoomed if needed)
Overlays:      Large, readable (24-32pt)
```

### Transitions
```
Between shots: Simple fade or cut
Duration:      0.3-0.5 seconds
Style:         Clean, professional
```

---

## 📐 COMPOSITION TIPS

### Terminal Shots
```
✓ Full screen or windowed (no distractions)
✓ Large font (18-20pt minimum)
✓ High contrast theme
✓ Show only relevant output
✓ Clear command prompt
```

### Browser Shots
```
✓ Hide bookmarks bar
✓ Close extra tabs
✓ Zoom if text is small (Ctrl/Cmd +)
✓ Full screen or clean window
✓ Show only /docs page
```

### Split Screen (Optional)
```
Left:  Terminal / Code
Right: Browser / Output
(Use if comfortable with editing)
```

---

## 🎬 CAMERA ANGLES (if showing yourself)

### Option 1: Screencast Only
- No face cam
- Focus on screen content
- Voiceover only
- **Recommended for technical demo**

### Option 2: Picture-in-Picture
- Small face cam in corner
- Main focus on screen
- More personal connection
- Requires good lighting

### Option 3: Introduction Only
- Face cam for intro (0:00-0:10)
- Switch to screencast for demo
- Face cam for closing (1:20-1:30)
- Professional feel

---

## 🎯 VISUAL CHECKLIST

**Before Recording Each Shot:**
```
□ Correct window/app in focus
□ Clean desktop (no clutter)
□ Font size large enough
□ Cursor visible
□ No notifications
□ Good lighting (if face cam)
□ Recording indicator on
```

**Visual Quality:**
```
□ 1080p resolution minimum
□ 60fps for smooth motion
□ High contrast
□ Readable text
□ No screen glare
□ Steady recording (no shaking)
```

---

## 💡 EDITING SUGGESTIONS

### Must-Have Edits
1. **Cut loading delays** (waiting for server)
2. **Speed up tests** (2x speed)
3. **Add overlay text** (key points)
4. **Fade in/out music**

### Nice-to-Have Edits
1. **Animated checkmarks** (on summary)
2. **Highlight cursor** (important clicks)
3. **Zoom effects** (emphasize details)
4. **Color corrections** (if needed)
5. **Sound effects** (subtle, for checkmarks)

### Text Overlays to Add
```
Shot 3:  "3 Technical + 2 Workflow"
Shot 4:  "Automated Development"
Shot 8:  "Complete CRUD Operations"
Shot 12: "Neon PostgreSQL + SQLModel"
Shot 14: "✓ 36 PASSED | 99% COVERAGE"
```

---

## 📹 EXPORT SETTINGS

```
Format:       MP4 (H.264)
Resolution:   1920x1080
Frame Rate:   30fps or 60fps
Bitrate:      8-10 Mbps
Audio:        AAC, 192kbps
Duration:     Exactly 1:30
File Size:    50-100MB
```

---

## ✅ POST-PRODUCTION CHECKLIST

```
□ Video plays smoothly
□ Audio is clear
□ All text is readable
□ Timing is correct (90s)
□ No awkward pauses
□ Transitions are smooth
□ Music at right volume
□ Exported in correct format
□ File size is acceptable
□ Tested on different devices
```

---

## 🎬 FINAL NOTES

**Remember:**
- Less is more - show results, not process
- Keep energy high throughout
- Visual > verbal (show don't just tell)
- Practice makes perfect
- Have fun! Your enthusiasm shows

**You've built something amazing - now showcase it! 🚀**
