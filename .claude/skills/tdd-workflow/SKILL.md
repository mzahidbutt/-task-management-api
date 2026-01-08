---
name: tdd-workflow
description: Test-Driven Development (TDD) workflow using the Red-Green-Refactor cycle. Use this skill when you want to build features with high quality and test coverage. Guides through writing tests first, then implementing code to pass those tests, and finally refactoring. Uses pytest, SQLModel, and FastAPI skills to ensure robust, well-tested code.
---

# Test-Driven Development (TDD) Workflow

Professional development workflow that writes tests before code. This ensures high quality, prevents bugs, and creates maintainable code through the Red-Green-Refactor cycle.

## What is TDD?

Test-Driven Development is a methodology where you:
1. **Write a failing test first** (Red)
2. **Write minimal code to pass the test** (Green)
3. **Refactor and improve the code** (Refactor)
4. **Repeat** for each feature

**Benefits:**
- Catch bugs before they exist
- Better code design
- Built-in documentation
- Confidence to refactor
- Higher test coverage

## When to Use TDD Workflow

Use this workflow when:
- Building critical features that must work correctly
- You want high test coverage
- Working on complex business logic
- Need confidence that code works
- Want to prevent regression bugs
- Building features that will be maintained long-term

**When to skip TDD:**
- Quick prototypes or experiments
- UI/design exploration
- Very simple CRUD with no logic
- One-off scripts

---

## The TDD Cycle: Red-Green-Refactor

```
🔴 RED → 🟢 GREEN → 🔵 REFACTOR → 🔴 RED → ...
```

### 🔴 RED Phase: Write Failing Test

Write a test for functionality that doesn't exist yet.

**Goal:** Define what "done" looks like before coding.

**Actions:**
1. Think about what the feature should do
2. Write a test that describes the behavior
3. Run the test → It should FAIL
4. Confirm it fails for the right reason

**Invoke pytest skill:**
```
"Write a test for [feature] that:
- Tests [specific behavior]
- Expects [specific outcome]
- Handles [specific scenario]"
```

**Red Phase Checklist:**
- [ ] Test clearly describes desired behavior
- [ ] Test fails when run
- [ ] Test fails for the right reason (not syntax error)
- [ ] Test is focused and tests one thing

---

### 🟢 GREEN Phase: Make Test Pass

Write the minimum code needed to make the test pass.

**Goal:** Get to working code as quickly as possible.

**Actions:**
1. Write the simplest code that passes the test
2. Use SQLModel skill for database code
3. Use FastAPI skill for API endpoint code
4. Run the test → It should PASS
5. Don't worry about perfection yet

**Invoke SQLModel skill (if needed):**
```
"Create/update [Model] with [fields] to support [feature]"
```

**Invoke FastAPI skill (if needed):**
```
"Create/update endpoint [URL] that [does what the test expects]"
```

**Green Phase Checklist:**
- [ ] Test passes
- [ ] Code is simple (not over-engineered)
- [ ] No extra features beyond what test requires
- [ ] Other tests still pass

---

### 🔵 REFACTOR Phase: Improve Code

Clean up and improve the code while keeping tests passing.

**Goal:** Make code better without changing behavior.

**Actions:**
1. Look for code smells (duplication, long functions, etc.)
2. Improve naming, structure, readability
3. Extract reusable code
4. Run tests after each change → Must stay GREEN
5. Stop when code is clean

**What to refactor:**
- Extract repeated code into functions
- Improve variable/function names
- Simplify complex logic
- Remove dead code
- Add type hints
- Improve error messages

**Refactor Phase Checklist:**
- [ ] Code is more readable
- [ ] No duplication
- [ ] Functions do one thing
- [ ] Names are clear
- [ ] All tests still pass

---

## Complete TDD Workflow Steps

### Step 1: Identify Next Small Feature

Break the feature into the smallest testable piece.

**Example:** Instead of "Add comments feature", start with:
- "Create a comment on a task"
- Then: "List comments for a task"
- Then: "Delete a comment"

**Good small features:**
- Create a resource
- Read a single resource
- List resources with filter
- Update a resource field
- Delete a resource
- Validate input
- Handle specific error

**Tip:** Each feature should take 5-15 minutes to implement.

---

### Step 2: 🔴 RED - Write Failing Test

**Actions:**

1. **Invoke pytest skill** to write the test:
```
"Write a test called test_[feature_name] that:
- [Setup: what needs to exist first]
- [Action: what the test does]
- [Assert: what should be true after]"
```

2. **Run the test:**
```bash
uv run pytest tests/test_[file].py::test_[feature_name] -v
```

3. **Verify it fails:**
- Should see: `FAILED` in red
- Error should make sense (e.g., "404 Not Found" because endpoint doesn't exist)

**Example Test:**
```python
def test_create_task_with_priority():
    """Test creating a task with priority field"""
    response = client.post("/tasks", json={
        "complain_no": "TASK001",
        "priority": "high",  # This field doesn't exist yet!
        "created_by": "john"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["priority"] == "high"
```

**Run:** ❌ Test fails (priority field doesn't exist)

---

### Step 3: 🟢 GREEN - Make Test Pass

**Actions:**

1. **Determine what's needed:**
   - Database change? → Use SQLModel skill
   - API change? → Use FastAPI skill
   - Both? → Use both skills

2. **Invoke SQLModel skill** (if database change needed):
```
"Add [field_name] field to [Model]:
- Type: [datatype]
- Default: [default_value]
- Nullable: [yes/no]"
```

3. **Invoke FastAPI skill** (if API change needed):
```
"Update [endpoint] to:
- Accept [new_field] in request
- Return [new_field] in response
- [Any validation/logic needed]"
```

4. **Run the test again:**
```bash
uv run pytest tests/test_[file].py::test_[feature_name] -v
```

5. **Verify it passes:**
- Should see: `PASSED` in green ✅

**Example Implementation:**

**SQLModel change:**
```python
class Task(SQLModel, table=True):
    # ... existing fields ...
    priority: str = Field(default="medium")  # ✅ Added
```

**FastAPI change:**
```python
class TaskCreate(SQLModel):
    complain_no: str
    priority: str = "medium"  # ✅ Added
    created_by: str

class TaskResponse(SQLModel):
    id: int
    complain_no: str
    priority: str  # ✅ Added
    created_by: str
```

**Run:** ✅ Test passes!

---

### Step 4: 🔵 REFACTOR - Improve Code

**Actions:**

1. **Review the code you just wrote:**
   - Is it clear?
   - Any duplication?
   - Good names?
   - Type safety?

2. **Make improvements:**
   - Extract magic strings to constants
   - Add enums for type safety
   - Improve error messages
   - Add docstrings

3. **Run tests after each change:**
```bash
uv run pytest -v
```

4. **Ensure all tests still pass:** ✅

**Example Refactoring:**

**Before (works but not great):**
```python
priority: str = Field(default="medium")
```

**After (better - type-safe):**
```python
from enum import Enum

class PriorityLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Task(SQLModel, table=True):
    priority: PriorityLevel = Field(default=PriorityLevel.MEDIUM)
```

**Run tests:** ✅ Still passing!

---

### Step 5: Repeat Cycle

Go back to Step 1 and pick the next small feature.

**Example progression:**
1. ✅ Create task with priority
2. 🔴 Filter tasks by priority (write test)
3. 🟢 Implement filter (make test pass)
4. 🔵 Refactor query logic
5. 🔴 Validate priority values (write test)
6. 🟢 Add validation (make test pass)
7. 🔵 Refactor validation

---

## Complete Example: Adding Task Assignment

### Feature: "Assign tasks to users"

**Break down into small pieces:**
1. Add assigned_to field
2. Create assignment endpoint
3. List assigned tasks
4. Validate assignee exists

---

### Iteration 1: Add assigned_to field

**🔴 RED - Write test:**
```python
def test_assign_task_to_user():
    # Create task
    response = client.post("/tasks", json={
        "complain_no": "T001",
        "created_by": "alice"
    })
    task_id = response.json()["id"]

    # Assign to user
    response = client.post(f"/tasks/{task_id}/assign", json={
        "assigned_to": "bob"
    })

    assert response.status_code == 200
    assert response.json()["assigned_to"] == "bob"
```

**Run:** ❌ Fails (endpoint doesn't exist)

**🟢 GREEN - Implement:**

*SQLModel:*
```python
class Task(SQLModel, table=True):
    # ... existing fields ...
    assigned_to: Optional[str] = None
    assigned_at: Optional[datetime] = None
```

*FastAPI:*
```python
@app.post("/tasks/{task_id}/assign")
def assign_task(task_id: int, assignment: dict, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(404, "Task not found")

    task.assigned_to = assignment["assigned_to"]
    task.assigned_at = datetime.now()
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
```

**Run:** ✅ Passes!

**🔵 REFACTOR - Improve:**
```python
# Add Pydantic model for type safety
class TaskAssignment(SQLModel):
    assigned_to: str

@app.post("/tasks/{task_id}/assign")
def assign_task(
    task_id: int,
    assignment: TaskAssignment,  # Better: type-safe
    session: Session = Depends(get_session)
):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(404, f"Task {task_id} not found")

    task.assigned_to = assignment.assigned_to
    task.assigned_at = datetime.now()
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
```

**Run:** ✅ Still passes!

---

### Iteration 2: List my assigned tasks

**🔴 RED - Write test:**
```python
def test_list_my_assigned_tasks():
    # Create and assign tasks
    task1 = client.post("/tasks", json={"complain_no": "T1", "created_by": "alice"})
    task2 = client.post("/tasks", json={"complain_no": "T2", "created_by": "alice"})

    client.post(f"/tasks/{task1.json()['id']}/assign", json={"assigned_to": "bob"})
    client.post(f"/tasks/{task2.json()['id']}/assign", json={"assigned_to": "charlie"})

    # Get Bob's tasks
    response = client.get("/tasks?assigned_to=bob")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["assigned_to"] == "bob"
```

**Run:** ❌ Fails (filtering not implemented)

**🟢 GREEN - Implement:**
```python
@app.get("/tasks")
def list_tasks(
    assigned_to: Optional[str] = None,
    session: Session = Depends(get_session)
):
    statement = select(Task)

    if assigned_to:
        statement = statement.where(Task.assigned_to == assigned_to)

    tasks = session.exec(statement).all()
    return tasks
```

**Run:** ✅ Passes!

**🔵 REFACTOR:** Already clean, no changes needed.

---

## TDD Best Practices

### Write Good Tests

**Good test characteristics:**
- Tests one thing
- Has clear name
- Follows Arrange-Act-Assert pattern
- Independent (doesn't depend on other tests)
- Fast to run

**Test naming:**
- `test_[feature]_[scenario]_[expected_result]`
- Examples:
  - `test_create_task_returns_201`
  - `test_get_nonexistent_task_returns_404`
  - `test_update_task_changes_database`

### Keep Tests Fast

- Use test database (separate from development)
- Clean up after tests
- Mock external services
- Don't test framework features (FastAPI/SQLModel already tested)

### Test the Right Things

**DO test:**
- Your business logic
- API behavior
- Database interactions
- Validation rules
- Error handling

**DON'T test:**
- Framework internals
- Third-party libraries
- Trivial getters/setters

### Commit Frequently

Commit after each RED-GREEN-REFACTOR cycle:
```bash
git add .
git commit -m "Add task assignment feature (TDD)"
```

---

## Troubleshooting TDD

### Test won't fail (stays green)
- Test might not be testing what you think
- Feature might already exist
- Test might be too loose (always passes)
- Check assertions are correct

### Test fails for wrong reason
- Syntax error in test
- Test setup issue
- Wrong test data
- Fix test before implementing feature

### Can't make test pass
- Test might be too ambitious (break it down)
- May need prerequisite features first
- Check error message for clues
- Start with even simpler implementation

### Refactoring breaks tests
- Make smaller changes
- Run tests after each tiny change
- Revert and try different approach
- Tests might be too brittle (coupled to implementation)

---

## TDD vs. API Feature Development Workflow

### When to use TDD Workflow:
- Critical features
- Complex logic
- Need high confidence
- Learning new technology

### When to use API Feature Development:
- Straightforward CRUD
- Tight deadlines
- Simple features
- Prototyping

### Use both together:
- API Feature Development = overall structure
- TDD Workflow = how you implement each endpoint

Example:
```
API Feature Development Workflow: "Add comments feature"
  ├─ Step 2: Database design
  ├─ Step 3: API implementation
  │   ├─ Use TDD for POST /comments endpoint
  │   │   └─ RED → GREEN → REFACTOR
  │   ├─ Use TDD for GET /comments endpoint
  │   │   └─ RED → GREEN → REFACTOR
  │   └─ Use TDD for DELETE /comments endpoint
  │       └─ RED → GREEN → REFACTOR
  └─ Step 4: Verify everything works
```

---

## Success Metrics

You're doing TDD right when:
- ✅ Writing tests before code feels natural
- ✅ Tests fail first, then pass
- ✅ Refactoring is confident and safe
- ✅ Test coverage is high (>80%)
- ✅ Bugs are caught early
- ✅ Code is cleaner and simpler
- ✅ You understand what you're building

---

## Quick Reference

### TDD Cycle Summary

```
1. 🔴 RED: Write failing test
   └─ pytest skill: "Write test for [feature]"

2. 🟢 GREEN: Make it pass
   ├─ SQLModel skill: "Add [field/model]"
   └─ FastAPI skill: "Create [endpoint]"

3. 🔵 REFACTOR: Clean up
   └─ Improve while keeping tests green

4. REPEAT: Next feature
```

### Key Commands

```bash
# Run specific test
uv run pytest tests/test_file.py::test_name -v

# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov

# Run tests on file save (watch mode)
uv run pytest-watch

# Run failed tests only
uv run pytest --lf
```

---

## Learning Resources

As you practice TDD, you'll develop:
- **Better design skills** - Tests force good architecture
- **Faster debugging** - Tests pinpoint problems
- **Confidence** - Tests prove code works
- **Documentation** - Tests show how to use code

Start with simple features and work up to complex ones. TDD is a skill that improves with practice!
