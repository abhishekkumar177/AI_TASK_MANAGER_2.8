# 🤝 Contributing to AI Task Manager 2.8

Welcome! 👋 Whether you’re a beginner, student, or experienced developer, your contributions are truly valued. We are building an AI-driven future for task management and media, and we’re excited to have you on board!

---

## 🛠 Development Standards

To maintain code quality and project integrity, please adhere to the following technical requirements:

* **Framework:** Built using **React 19** and **Streamlit**.
* **Styling:** Use **Tailwind CSS** for all new React components.
* **Naming Conventions:**
* `PascalCase` for React components (e.g., `PostCard.jsx`).
* `camelCase` for variables and functions.


* **Linting:** You **must** run `npm run lint` and fix all warnings before committing.
* **Code Quality:** Follow Python (PEP8) for backend scripts. Write clean, modular, and documented code.

---

## 🚀 Getting Started

### 1️⃣ Fork the Repository

Click the **Fork** button at the top-right corner of this page to create your copy of the repo.

### 2️⃣ Clone Your Fork

```bash
git clone https://github.com/your-username/AI_TASK_MANAGER_2.8.git
cd AI_TASK_MANAGER_2.8

```

### 3️⃣ Create a New Branch

```bash
git checkout -b feature/your-feature-name

```

### 4️⃣ Make Your Changes

* **Environment:** Copy `.env.example` to `.env` before starting.
* Write clean, modular, and documented code.
* Add docstrings and comments where necessary.
* Keep your code consistent with the existing structure.

### 5️⃣ Test Your Changes

* **For Streamlit:** Run `streamlit run app.py` locally.
* **For React:** Run `npm run dev` and `npm run lint`.
* Verify that your changes don’t break existing functionality.

### 6️⃣ Commit and Push

We follow the `type(scope): subject` format for commit messages:

* `feat:` A new feature
* `fix:` A bug fix
* `docs:` Documentation changes

```bash
git add .
git commit -m "feat: added intelligent task sorting"
git push origin feature/your-feature-name

```

### 7️⃣ Submit a Pull Request

* Go to your forked repo and click **"Compare & pull request"**.
* **Mandatory:** You **MUST** provide screenshots or GIFs of the new changes in your PR description.
* Wait for review and feedback from maintainers.

---

## 🚦 Workflow & Rules

* **Respect Assignments:** Wait for an issue to be **officially assigned** to you before starting work. Unsolicited PRs for unassigned issues will be closed.
* **Issue Limit:** Maximum of **3 issues** assigned at one time.
* **Visual Requirements:** You **MUST** provide screenshots of the "Area to be Changed" when opening a new Issue.

---

## ⏱️ Time Constraints & Disqualification

* **Deadline:** Tasks should ideally be completed within **30 minutes to 48 hours**.
* **Grace Period:** If no progress is shown after **72 hours**, the issue will be unassigned.
* **Stale PRs:** Failure to respond to requested changes within **24 hours** may result in the PR being closed.
* **Immediate Disqualification:** Submitting a PR that fails the build, ignores linting rules, lacks mandatory screenshots, or duplicates someone else's work.

---

## 🚫 Community Guidelines & Morale

* **Positive Environment:** No negative comments that decrease morale or discourage other contributors.
* **Code of Conduct:** Please be respectful and inclusive. Harassment or discrimination of any kind will not be tolerated.

---

## 📬 Need Help?

If you get stuck or have questions:

* Open a **GitHub Issue** describing your problem.
* Tag a **maintainer** for assistance.
* **Tips:** Start with issues labeled `good first issue`. Don’t worry about perfection—maintainers will guide you!

**Thank you for helping us improve! Together, we’re building a smarter future. 🚀**
