# 🎯 DEMO VIDEO PRACTICE GUIDE
## Step-by-Step Preparation & Rehearsal

---

## 📋 PREPARATION PHASE (30 minutes)

### Step 1: Environment Setup (10 min)

#### Desktop Cleanup
```
□ Close all unnecessary applications
□ Close extra browser tabs
□ Hide desktop icons (optional)
□ Set wallpaper to solid color (optional)
□ Disable notifications (Windows: Focus Assist, Mac: Do Not Disturb)
□ Put phone on silent
```

#### Terminal Setup
```
□ Open 3 terminal tabs/windows:
   Tab 1: For showing skills
   Tab 2: For running server
   Tab 3: For running tests
□ Set font size to 18-20pt
□ Use high-contrast theme
□ Clear history: type `clear` or `cls`
□ Navigate to project folder
```

#### Browser Setup
```
□ Open Chrome/Firefox
□ Close all tabs except one
□ Navigate to http://localhost:8000/docs
   (Server not running yet - will show error, that's OK)
□ Zoom to 100% or 125% for readability
□ Hide bookmarks bar (Ctrl+Shift+B)
□ Enter fullscreen or clean window mode
```

#### IDE/Editor Setup (Optional)
```
□ Open VS Code with project
□ Close right sidebar/panels
□ Set readable zoom level
□ Have project explorer visible
```

---

### Step 2: Test All Commands (10 min)

#### Test Terminal Commands

**Terminal 1: Skills**
```bash
cd "E:\Panaversity\Pana-400\Pana_project\.claude\skills"
ls -la *.skill

# Expected: 5 .skill files listed
```

**Terminal 2: Server**
```bash
cd "E:\Panaversity\Pana-400\Pana_project\task-api"
uv run uvicorn main:app --reload

# Expected: Server starts, no errors
# Keep running for browser test
```

**Terminal 3: Tests**
```bash
cd "E:\Panaversity\Pana-400\Pana_project\task-api"
uv run pytest tests/ -v --tb=no

# Expected: 36 passed
# Stop server before running tests
```

#### Test Browser Interaction

```
1. Go to http://localhost:8000/docs
2. Find POST /tasks
3. Click "Try it out"
4. Paste demo data:
   {
     "complain_no": "DEMO001",
     "complain_remarks": "Video demo task",
     "complain_status": "pending",
     "created_by": "demo_user"
   }
5. Click "Execute"
6. Verify 201 response with ID
7. Find GET /tasks/{task_id}
8. Enter ID from previous response
9. Click "Execute"
10. Verify 200 response

✓ Everything works? Move to next step!
✗ Errors? Fix them before recording!
```

---

### Step 3: Prepare Recording Materials (10 min)

#### Create Title Slide (Optional)
```
Use PowerPoint, Keynote, or Canva:

Title: Task Management API Project
Subtitle: Panaversity Quarter 4
By: [Your Name]

Save as image or have ready to screen record
```

#### Create Summary Slide
```
PROJECT SUMMARY

✓ 5 Reusable Skills
  (3 technical + 2 workflow)

✓ Complete CRUD API
  (FastAPI + SQLModel)

✓ Cloud Database
  (Neon PostgreSQL)

✓ 36 Tests | 99% Coverage

✓ Production-Ready Code

Save as image or have ready
```

#### Print Reference Materials
```
□ Print DEMO_QUICK_REFERENCE.md
□ Have script visible on second monitor
   OR memorize key talking points
□ Have timer/stopwatch ready
```

---

## 🎭 REHEARSAL PHASE (45 minutes)

### Rehearsal 1: Script Reading (10 min)

**Goal:** Familiarize with script

```
□ Read script out loud 3 times
□ Note difficult words/phrases
□ Practice pronunciation
□ Find natural pace
□ Mark breathing points
```

**Tips:**
- Read slower than you think
- Emphasize key words: "5 skills", "99% coverage"
- Smile while reading (sounds better!)
- Record yourself and listen back

---

### Rehearsal 2: Actions Only (10 min)

**Goal:** Practice all technical steps

**Run through without speaking:**

```
□ Show skills files
□ Show workflow file/diagram
□ Start server
□ Open browser to /docs
□ Create task (data pre-copied)
□ Get task by ID
□ Stop server
□ Run tests
□ Show test results
□ Switch to summary slide
```

**Time yourself:**
- Technical actions should take: ~60 seconds
- Leaves 30 seconds for talking
- Too slow? Practice faster transitions
- Too fast? Add more pauses/explanations

---

### Rehearsal 3: Combined Dry Run (15 min)

**Goal:** Full rehearsal without recording

**Do complete run-through with:**
- Speaking
- Actions
- Timing
- Transitions

**Use stopwatch to time each section:**

| Section | Target | Your Time | Status |
|---------|--------|-----------|--------|
| Intro | 10s | ___s | □ |
| Skills | 15s | ___s | □ |
| Workflow | 15s | ___s | □ |
| API Demo | 30s | ___s | □ |
| Tests | 10s | ___s | □ |
| Closing | 10s | ___s | □ |
| **TOTAL** | **90s** | **___s** | □ |

**Troubleshooting:**
- Too long? Speak faster, cut pauses
- Too short? Add more explanation, slow down
- Awkward spots? Practice transitions more

---

### Rehearsal 4: Mock Recording (10 min)

**Goal:** Practice like it's real

**Setup:**
1. Start recording software
2. Do NOT hit record yet
3. Pretend you're recording
4. Go through entire demo
5. Stop

**This helps:**
- Reduce nervousness
- Find technical issues
- Build confidence
- Smooth transitions

---

## 🎬 RECORDING PHASE (30 minutes)

### Pre-Recording Final Check (5 min)

```
□ All apps/tabs ready
□ Terminal history cleared
□ Server NOT running yet
□ Browser at /docs (will show error, OK)
□ Demo data copied to clipboard
□ Script visible
□ Timer ready
□ Mic tested (record 10 seconds, play back)
□ Camera tested (if using)
□ Good lighting (if showing face)
□ Notifications OFF
□ Phone silent/away
□ Recording software open
□ Output folder selected
□ Breath deeply and smile!
```

---

### Recording Attempt 1 (10 min)

**Just Do It!**

1. Start recording
2. Do complete 90-second demo
3. Stop recording
4. **DO NOT** delete or re-do yet
5. Save as "take1.mp4"

**Then:**
- Watch back immediately
- Take notes on what went wrong
- Note timestamp of mistakes
- Don't be too critical - it's your first take!

---

### Review & Notes (5 min)

**Watch your recording and check:**

| Aspect | Good? | Notes |
|--------|-------|-------|
| Audio clear | □ | |
| Voice energy | □ | |
| Timing (90s) | □ | |
| All visuals shown | □ | |
| Commands worked | □ | |
| Smooth transitions | □ | |
| No long pauses | □ | |

**Common issues:**
- Speaking too fast → Slow down
- Speaking too quiet → Closer to mic, more energy
- Clicking wrong things → Practice more
- Going over time → Cut explanations, speak faster
- Awkward pauses → Edit these out later OR re-record

---

### Recording Attempt 2 (10 min)

**Apply lessons learned**

1. Fix issues from Attempt 1
2. Reset environment (clear terminals)
3. Take deep breath
4. Start recording
5. Complete demo
6. Stop recording
7. Save as "take2.mp4"

**This take usually better!**

---

## ✂️ EDITING PHASE (30 minutes)

### Basic Editing (Minimum)

**Must-do edits:**

```
□ Trim beginning (start on first word)
□ Trim end (end after last word)
□ Cut out long server startup delay
□ Speed up test execution (2x)
□ Add title card (if created)
□ Add summary slide at end
□ Adjust audio levels (normalize)
□ Export as MP4
```

**Tools:**
- DaVinci Resolve (free, powerful)
- iMovie (Mac, simple)
- OpenShot (free, cross-platform)

---

### Advanced Editing (Optional)

**Nice additions:**

```
□ Add background music (low volume)
□ Add text overlays for key points
□ Add animated checkmarks
□ Add smooth transitions
□ Color correction (if needed)
□ Add zoom effects on important parts
□ Add your name/contact at end
```

**Text Overlays to Add:**
```
Shot 3:  "3 Technical + 2 Workflow"
Shot 8:  "Complete CRUD Operations"
Shot 14: "✓ 36 PASSED | 99% COVERAGE"
```

---

## 📤 EXPORT & SUBMISSION (15 minutes)

### Export Settings

```
Format:       MP4 (H.264)
Resolution:   1920x1080
Frame Rate:   30fps
Bitrate:      8 Mbps
Audio:        AAC, 192kbps
Duration:     1:30 (exactly)
```

### Quality Check

**Watch exported video:**

```
□ Video plays smoothly
□ Audio is clear throughout
□ No pixelation or artifacts
□ Text is readable (if added)
□ Duration is 90 seconds (±2s OK)
□ File size reasonable (<100MB)
□ Format is correct (MP4)
```

### Final Testing

**Test on different devices:**

```
□ Play on your computer
□ Play on phone (if possible)
□ Test with headphones
□ Test with speakers
□ Check in different media players
```

### Submission

```
□ Rename file: "YourName_TaskAPI_Demo.mp4"
□ Upload to submission platform
□ OR upload to YouTube (unlisted)
□ Verify upload completed
□ Test viewing the uploaded version
□ Submit link/file as required
```

---

## 🎯 TROUBLESHOOTING GUIDE

### Problem: Going Over Time

**Solutions:**
- Speak 10% faster
- Cut workflow explanation to 10s
- Skip showing workflow file, just explain
- Show only Create task, skip Get task
- Cut intro to 7-8 seconds

---

### Problem: Audio Too Quiet

**Solutions:**
- Get closer to mic
- Speak louder (more energy!)
- Edit audio: normalize volume
- Adjust mic gain before recording
- Use external microphone

---

### Problem: Server Takes Too Long to Start

**Solutions:**
- Start server before recording, then restart
- Edit out waiting time
- Switch to pre-started server
- Fast-forward in editing (2x speed)

---

### Problem: Made Mistake While Recording

**Solutions:**
- Pause, wait 2 seconds, continue
  (Edit out pause later)
- Finish take anyway, review after
- Note timestamp, decide if re-record needed
- Most mistakes can be edited out!

---

### Problem: Nervous or Stumbling

**Solutions:**
- Practice 2 more times
- Remember: You can re-record!
- Take deep breaths between sections
- Smile (reduces tension)
- Remember: Reviewers want you to succeed!

---

### Problem: Commands Not Working

**Solutions:**
- Test ALL commands before recording
- Have backup plan (screenshots)
- Keep old working version
- Don't update packages right before recording

---

## ✅ FINAL CHECKLIST

### Day Before Recording
```
□ Test all commands work
□ Prepare demo data
□ Create title/summary slides
□ Read through script 3-5 times
□ Get good night's sleep!
```

### Morning of Recording
```
□ Pick quiet time (no background noise)
□ Good lighting (if showing face)
□ Comfortable clothes
□ Glass of water nearby
□ Clear calendar (30-60 min block)
```

### Right Before Recording
```
□ Use bathroom!
□ Deep breaths
□ Smile and relax
□ Remember: It's just a demo
□ You've got this! 🚀
```

### After Recording
```
□ Save all takes (don't delete)
□ Watch and take notes
□ Edit as needed
□ Export and test
□ Submit on time
□ Celebrate! 🎉
```

---

## 💪 CONFIDENCE BOOSTERS

**Remember:**

1. **You built something amazing** - Show it with pride!
2. **Nobody expects perfection** - Natural delivery is better
3. **You can re-record** - First take is practice
4. **Reviewers are supportive** - They want to see you succeed
5. **Your work speaks for itself** - The API works, tests pass!

**Positive Affirmations:**

> "I built a production-ready API with 99% test coverage."

> "My skills automate complex development workflows."

> "I followed professional best practices throughout."

> "This demo showcases my technical abilities clearly."

> "I am prepared and confident."

---

## 🎓 SUCCESS CRITERIA

Your demo is successful if it shows:

✓ **5 Skills** - Clearly identified
✓ **Automation** - Workflows orchestrate technical skills
✓ **API Works** - Can create and retrieve tasks
✓ **Quality** - Tests pass, high coverage
✓ **Professional** - Clear, confident delivery

**Even if not perfect, showing these 5 things = SUCCESS!**

---

## 📞 NEED HELP?

**If stuck:**
1. Re-read the DEMO_VIDEO_SCRIPT.md
2. Watch your practice recordings
3. Take a break and try again
4. Remember: Done is better than perfect!

**Timeline:**
- Day 1: Preparation (30 min)
- Day 2: Rehearsal (45 min)
- Day 3: Recording (30 min)
- Day 4: Editing (30 min)
- Day 5: Review & Submit

**Total time investment: ~2.5 hours spread over a few days**

---

## 🌟 FINAL THOUGHTS

You've put in weeks of work building this project.
The demo video is your chance to showcase that effort.

**Take your time.**
**Practice thoroughly.**
**Record confidently.**
**Submit proudly.**

**You've got this!** 🚀🎉

---

**Good luck with your demo video!**

Remember: Your API works, your tests pass, your skills are real.
Now just show the world what you've built!
