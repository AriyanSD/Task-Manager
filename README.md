# 📝 Task Manager — Django + DRF + Django Template JS Frontend

A task management application built using **Django**, **Django REST Framework**, and **Bootstrap**, with a classic server-rendered UI that communicates with the backend via **JavaScript fetch()** calls.

- Django session-based authentication  
- REST API endpoints built with DRF  
- Frontend templates using JavaScript to call APIs  
- Proper permissions (IsAuthenticated + IsOwnerOrReadOnly)  
- CRUD operations both via API and UI  

---

## 📦 Features

### ✔ Task Features
- Create, edit, delete tasks  
- Task list with search + status filtering  
- Each task belongs to a user  
- Users can only edit/delete their own tasks  
- Task detail view  

### ✔ API Features
- `/api/tasks/`  
  - GET → List tasks  
  - POST → Create task  
- `/api/tasks/<id>/`  
  - GET → Retrieve  
  - PUT/PATCH → Update  
  - DELETE → Delete  

### ✔ Frontend Points
- `/tasks/`   
  - GET → All tasks list
- `/tasks/create/`   
  - GET → Create task form, then POST to API
- `/tasks/<int:pk>/`   
  - GET → Show task detail
- `/tasks/<int:pk>/edit/`   
  - GET → Edit task form, then PUT to API

**Note:** Deleting a task is managed via JavaScript in detail and list views with direct API calls (no separate view).

### ✔ Authentication
- Django session authentication  
- API protected using session cookies  
- No token required for frontend templates  

---

## 🛠 Technologies Used

- **Django 5(4 in deployment)**
- **Django REST Framework**
- **Bootstrap**
- **JavaScript (fetch API)**
- **SQLite**

---

## 🌐 Live Demo

The project is deployed on PythonAnywhere ,the debugg mode still is active:
**https://ariyansd.pythonanywhere.com/**

### Test Accounts
You can login with these accounts to test the application:

**Super User:**
- Username: `in txt file`
- Password: `in txt file`

**Test Users:**
- User 1: `user1` / `ariyan1383`
- User 2: `user2` / `ariyan1383`

Sample tasks have been added for testing purposes.

---

## 🚀 Setup

### Clone the repository
```bash
git clone https://github.com/AriyanSD/Task-Manager.git
```

## 🔐 API Authentication

This project uses **SessionAuthentication**:
- Users log in using Django's built-in login
- Browser stores the session cookie
- API calls include the cookie automatically
- DRF checks permissions using `IsAuthenticated`

---

## 🧩 API Endpoints

### 📘 List & Create
```
GET /api/tasks/
POST /api/tasks/
```

### 📙 Retrieve / Update / Delete
```
GET /api/tasks/<id>/
PUT /api/tasks/<id>/
DELETE /api/tasks/<id>/
```

### 👤 Permission Rules
`IsOwnerOrReadOnly` ensures:
- Anyone can read
- Only the owner can update/delete

---

## 🎨 Frontend Rendering

Templates rendered through Django:
- Task list loads via API using JS
- Task detail loads via API
- Create/Edit form sends POST/PUT to API
- Delete sends DELETE to API

---

## 🧪 Example API Response
```json
{
  "id": 4,
  "owner": 1,
  "owner_username": "ariyan",
  "title": "Complete README",
  "description": "Write full documentation",
  "status": "in_progress",
  "created_at": "2025-11-25T12:35:10Z",
  "updated_at": "2025-11-25T12:50:32Z"
}
```

---

## 🏗 Design and Implementation

### How It Works
The UI views work as just a frontend - they don't talk to the database directly. Everything goes through JavaScript calls to the API. I used Django's `TemplateView` to show these pages.

### API Setup
The requirements said:
- One API endpoint to handle list and create tasks
- One API endpoint to handle view, update, and delete tasks

So I used two DRF views:
- `ListCreateAPIView` for `/api/tasks/` (list and create)
- `RetrieveUpdateDestroyAPIView` for `/api/tasks/<id>/` (get, update, delete)

These views already have everything we need built-in.

### Why Session Authentication?
I went with session-based auth because:
- Works great with Django's login system
- No need to mess with tokens in the frontend
- Browser handles cookies automatically
- Much easier to set up than JWT
- Perfect for this type of project

I thought about using JWT at first, but session auth is simpler and does the job well for a Django template + API project.

### Permissions
I made a custom `IsOwnerOrReadOnly` permission so:
- Anyone logged in can see all tasks
- Only the task owner can edit or delete their own tasks
- No one can mess with other people's tasks

### Development Notes
- Used AI help mostly for UI part , example for debugging and Bootstrap styling in the templates
- Had to learn about session authentication with DRF - it's a bit different from token auth which is more common
- Used regular JavaScript with fetch() for all the API calls
- Kept it simple - no React, Vue, or other frameworks needed

