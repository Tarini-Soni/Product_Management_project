#  Project Management Tool (Trello-like Full Stack App)

##  Overview
The Project Management Tool is a full-stack web application designed to help users manage projects, tasks, and collaboration efficiently.  
It is inspired by tools like Trello and Asana, providing a structured workflow for task tracking and team coordination.

---

##  Features

-  User Authentication (JWT Login & Registration)
-  Create and manage multiple projects
-  Task creation under each project
-  Assign tasks to users
-  Comment system for task discussions
-  Secure user-based data isolation
-  REST API architecture (Django REST Framework)

---

##  Tech Stack

### Frontend
- React.js
- Axios
- React Router

### Backend
- Django
- Django REST Framework
- Simple JWT Authentication

### Database
- SQLite (Development)

---

##  Project Structure


Project_Management_Tool/
│
├── backend (Django)
│ ├── users/
│ ├── projects/
│ ├── tasks/
│ ├── comments/
│ └── core/
│
├── frontend (React)
│ ├── src/
│ ├── pages/
│ └── api.js




---

##  Authentication Flow

1. User registers or logs in
2. Backend returns JWT token
3. Token is stored in frontend (localStorage)
4. Token is sent with every API request
5. Backend verifies token before allowing access

---

## 📡 API Endpoints

- `/api/auth/register/` → Register user
- `/api/auth/login/` → Login user
- `/api/projects/` → Manage projects
- `/api/tasks/` → Manage tasks
- `/api/comments/` → Manage comments

---

##  Objective

To build a real-world full-stack project demonstrating:
- Authentication system
- REST API development
- Frontend-backend integration
- Scalable project structure

---

##  Future Improvements

- Drag & Drop Kanban Board UI
- Real-time updates using WebSockets
- Notifications system
- Team collaboration features
- Cloud deployment (Render / Vercel / AWS)

---

##  Author

Developed as a Full Stack Internship Project
