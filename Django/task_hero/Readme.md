
---

### 🔁 **Updated Project Roadmap (With Separate Auth App)**

---

### **PHASE 1: Project & App Setup**

1. **Create the Project & Apps**
   - `django-admin startproject taskhero_project`
   - `python manage.py startapp task_hero`
   - `python manage.py startapp users` (for authentication)

2. **Project Config**
   - Add `task_hero`, `users` to `INSTALLED_APPS`
   - Configure `AUTH_USER_MODEL` (if customizing user model)
   - Set up static files, templates folder structure

---

### **PHASE 2: Authentication App (accounts)**

1. **User Model & Forms**
   - Use Django's built-in `User` or create a `CustomUser` if needed.
   - Create custom **Sign Up Form** with:
     - First Name, Last Name, Email, Username, Password1, Password2

2. **Views & URLs**
   - `signup_view` → Registers users
   - `login_view` → Uses `LoginView`
   - `logout_view` → Uses `LogoutView`

3. **Templates**
   - `signup.html`, `login.html`, `base.html`
   - Use `extends` and `{% block %}` to reuse layout

4. **Redirect After Login**
   - Use `LOGIN_REDIRECT_URL = '/dashboard/'` in settings

---

### **PHASE 3: Task Management (tasks app)**

1. **Model**
   - Create `Task` model with:
     - Title, Description, Due Date, Status, Priority, Owner (ForeignKey to User)

2. **CRUD Views**
   - Create:
     - `TaskCreateView`
     - `TaskListView` (dashboard)
     - `TaskDetailView`
     - `TaskUpdateView`
     - `TaskDeleteView` (with confirmation)

3. **User Ownership**
   - Use `@login_required` decorators
   - In views, filter tasks by `request.user`
   - Add permissions logic to ensure only owners can edit/delete

---

### **PHASE 4: Dashboard & UI Design**

1. **Dashboard View**
   - Fetch tasks grouped by status:
     - `To Do`, `In Progress`, `Completed`
   - Use cards for each task:
     - Show: Title, Due Date, Priority (color-coded), Overdue Tag

2. **Task Detail View**
   - Show task information clearly
   - Include edit/delete buttons

3. **Styling**
   - Use Bootstrap or Tailwind CSS
   - Add colored priority tags and red "Overdue" tags

---

### **PHASE 5: Permissions & Security**

1. **Protect Views**
   - Use `LoginRequiredMixin` and `UserPassesTestMixin` where needed

2. **Access Control**
   - Tasks must belong to the current user
   - Redirect or show error message if not authorized

3. **Error Pages**
   - Custom 403/404 templates for better UX

---
