---
name: api-feature-workflow
description: End-to-end workflow for adding a new feature to a FastAPI application. Use this skill when building complete API endpoints from requirements to deployment. Guides through database design, API implementation, testing, and verification using SQLModel, FastAPI, and pytest skills. Perfect for adding CRUD endpoints, new features, or extending existing APIs.
---

# API Feature Development Workflow

Systematic workflow for building complete API features from scratch. This skill orchestrates your SQLModel, FastAPI, and pytest skills to deliver production-ready features.

## When to Use This Skill

Use this workflow when:
- Adding a new API endpoint or feature
- Building CRUD operations for a new resource
- Extending existing API functionality
- Need to implement a complete user story
- Want to ensure all aspects (database, API, tests) are covered

## Workflow Steps

### Step 1: Understand Requirements

Before writing any code, clarify the feature requirements.

**Questions to ask:**
1. What is the feature trying to accomplish?
2. What data needs to be stored?
3. What endpoints are needed (GET, POST, PUT, DELETE)?
4. What are the validation rules?
5. Who can access this feature (permissions)?
6. What should happen on errors?

**Output:** Clear understanding of what to build

---

### Step 2: Design Database Schema

Use the SQLModel skill to design or modify the database schema.

**Actions:**
1. Identify what tables/models are needed
2. Define fields with proper data types
3. Set up relationships (foreign keys) if needed
4. Add indexes for query performance
5. Define constraints (nullable, unique, defaults)

**Invoke SQLModel skill:**
```
"Create a [ModelName] table with fields: [list fields with types].
Add relationship to [OtherModel] via [foreign_key].
Include indexes on [frequently queried fields]."
```

**Checklist:**
- [ ] Model class created with proper fields
- [ ] Relationships defined if needed
- [ ] Defaults set for optional fields
- [ ] Database table will be created on startup

---

### Step 3: Create API Endpoints

Use the FastAPI skill to build the API routes.

**Actions:**
1. Design the endpoint URLs (RESTful patterns)
2. Create Pydantic request/response models
3. Implement route handlers with proper HTTP methods
4. Add request validation
5. Implement error handling
6. Add endpoint documentation

**Invoke FastAPI skill:**
```
"Create CRUD endpoints for [Resource]:
- POST /[resource] - Create new [resource]
- GET /[resource] - List all [resources] with filtering
- GET /[resource]/{id} - Get single [resource]
- PUT /[resource]/{id} - Update [resource]
- DELETE /[resource]/{id} - Delete [resource]

Include validation for [specific rules].
Add error handling for [specific cases]."
```

**RESTful URL Patterns:**
- Collection: `/tasks`, `/comments`, `/users`
- Single resource: `/tasks/{id}`, `/users/{user_id}`
- Nested resources: `/tasks/{task_id}/comments`
- Actions: `/tasks/{id}/assign`, `/users/{id}/activate`

**Checklist:**
- [ ] Pydantic models created (Create, Update, Response)
- [ ] Route handlers implemented
- [ ] HTTP status codes correct (200, 201, 404, etc.)
- [ ] Error handling added
- [ ] Docstrings added to endpoints

---

### Step 4: Write Tests

Use the pytest skill to create comprehensive tests.

**Actions:**
1. Test each endpoint (happy path)
2. Test validation errors
3. Test edge cases (not found, duplicates, etc.)
4. Test filtering and pagination
5. Test database state changes

**Invoke pytest skill:**
```
"Write tests for [Resource] endpoints covering:
- Creating [resource] with valid data
- Creating [resource] with invalid data (validation errors)
- Listing [resources] with filters
- Getting single [resource] by ID
- Getting non-existent [resource] (404)
- Updating [resource]
- Deleting [resource]
- [Any specific business logic tests]"
```

**Test Coverage Goals:**
- Happy path (everything works)
- Validation errors (bad input)
- Not found errors (invalid IDs)
- Business logic edge cases

**Checklist:**
- [ ] Tests created for all endpoints
- [ ] Happy path tests passing
- [ ] Error case tests passing
- [ ] Database cleanup in tests working
- [ ] All tests pass: `uv run pytest`

---

### Step 5: Manual Verification

Test the feature manually to ensure it works end-to-end.

**Actions:**
1. Start the development server
2. Open the interactive API docs
3. Test each endpoint manually
4. Verify database state
5. Test with realistic data

**Commands:**
```bash
# Start server
uv run uvicorn main:app --reload

# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov

# Check specific endpoint
curl -X POST http://localhost:8000/[endpoint] \
  -H "Content-Type: application/json" \
  -d '{"field": "value"}'
```

**Interactive Testing:**
1. Go to `http://localhost:8000/docs`
2. Try the "Try it out" button on each endpoint
3. Test with valid data
4. Test with invalid data
5. Verify responses match expectations

**Database Verification:**
- Check that records are created/updated/deleted correctly
- Verify relationships are working
- Check that constraints are enforced

**Checklist:**
- [ ] Server starts without errors
- [ ] All endpoints visible in `/docs`
- [ ] Can create resource successfully
- [ ] Can read resource successfully
- [ ] Can update resource successfully
- [ ] Can delete resource successfully
- [ ] Error messages are clear and helpful

---

### Step 6: Final Review

Review everything before considering the feature complete.

**Code Review Checklist:**
- [ ] Database model follows naming conventions
- [ ] API endpoints follow RESTful patterns
- [ ] All tests passing
- [ ] No hardcoded values (use environment variables)
- [ ] Error handling is comprehensive
- [ ] API documentation is clear
- [ ] No sensitive data in responses
- [ ] Database queries are efficient (no N+1 problems)
- [ ] Code is clean and readable

**Documentation Checklist:**
- [ ] Endpoint docstrings are descriptive
- [ ] Request/response models have examples
- [ ] Error responses documented
- [ ] Any business rules documented

---

## Example Usage

### Example 1: Add Comments Feature

**Requirement:** "Users should be able to comment on tasks"

**Step 1: Requirements**
- Comments belong to tasks
- Each comment has: text, author, timestamp
- Users can list, create, delete their own comments

**Step 2: Database (SQLModel skill)**
```
Create Comment model:
- id (primary key)
- task_id (foreign key to tasks)
- comment_text (required)
- author_name (required)
- created_at (auto timestamp)
```

**Step 3: API (FastAPI skill)**
```
Endpoints:
- POST /tasks/{task_id}/comments
- GET /tasks/{task_id}/comments
- DELETE /comments/{comment_id}
```

**Step 4: Tests (pytest skill)**
```
Tests:
- test_create_comment_on_task()
- test_list_comments_for_task()
- test_delete_comment()
- test_comment_on_nonexistent_task()
```

**Step 5: Manual Testing**
- Create task via API
- Add comments to task
- List comments
- Delete comment
- Verify in database

**Result:** Complete comments feature with tests ✅

---

### Example 2: Add Task Priority

**Requirement:** "Tasks should have priority levels"

**Step 1: Requirements**
- Priority: low, medium, high
- Default: medium
- Filter tasks by priority

**Step 2: Database (SQLModel skill)**
```
Add to Task model:
- priority (enum: low/medium/high, default: medium)
```

**Step 3: API (FastAPI skill)**
```
Update:
- TaskCreate to accept priority
- GET /tasks to filter by priority
- Add priority validation (enum)
```

**Step 4: Tests (pytest skill)**
```
Tests:
- test_create_task_with_priority()
- test_filter_by_priority()
- test_invalid_priority_rejected()
```

**Step 5: Manual Testing**
- Create tasks with different priorities
- Filter by priority
- Try invalid priority

**Result:** Priority feature added ✅

---

## Common Patterns

### Adding a New Resource (CRUD)

For a new resource like "Projects", "Categories", "Tags":

1. **Database:** Create model with SQLModel skill
2. **API:** Create 5 CRUD endpoints with FastAPI skill
3. **Tests:** Write tests for all operations with pytest skill
4. **Verify:** Test manually and check database

### Adding a Field to Existing Resource

For adding a field like "due_date" to tasks:

1. **Database:** Add field to existing model
2. **API:** Update Create/Update/Response models
3. **Tests:** Update existing tests, add new field tests
4. **Verify:** Test that field is saved/retrieved

### Adding a Relationship

For relating two resources like Tasks and Categories:

1. **Database:** Add foreign key, define relationship
2. **API:** Update endpoints to include related data
3. **Tests:** Test that relationships work correctly
4. **Verify:** Check that related data loads properly

---

## Tips for Success

1. **Start small:** Build one endpoint at a time
2. **Test early:** Don't wait until everything is built
3. **Use examples:** Copy patterns from existing endpoints
4. **Read errors:** Error messages tell you what's wrong
5. **Check database:** Verify data is actually being saved
6. **Use types:** Type hints catch errors before runtime
7. **Think REST:** Follow RESTful conventions for URLs
8. **Handle errors:** Always think about what can go wrong

---

## Troubleshooting

### Server won't start
- Check DATABASE_URL in .env file
- Verify database is running
- Check for syntax errors in models

### Tests failing
- Check test database is clean
- Verify test data is valid
- Read test error messages carefully

### Endpoint not working
- Check URL path is correct
- Verify HTTP method (GET/POST/PUT/DELETE)
- Check request body format
- Look at server logs for errors

### Database errors
- Check field types match
- Verify foreign keys exist
- Ensure required fields provided
- Check for constraint violations

---

## Success Criteria

Feature is complete when:
- ✅ All tests passing
- ✅ Manual testing successful
- ✅ Database state correct
- ✅ Error handling works
- ✅ Documentation clear
- ✅ Code reviewed and clean
