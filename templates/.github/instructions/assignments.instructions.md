---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency and clarity for students."
applyTo: "assignments/**/*.md"
---

# Assignment Markdown Structure Guidelines

All assignment markdown files should follow these guidelines:

## 1. Template Usage

- Assignment markdown files must use the following structure:

   ```markdown
   # 📘 Assignment: [Assignment Title]

   ## 🎯 Objective

   [Describe what the student will learn or accomplish.]

   ## 📝 Tasks

   ### 🛠️ [Task Name]

   #### Description

   [Explain what the student must do.]

   #### Requirements

   Completed program should:

   - [Expected outcome or feature]
   ```

- The assignment must be created as a `README.md` file inside its assignment folder.
- Do not remove or skip required sections from the template.

## 2. Section Guidance

The section headers should reflect the structure in the template, including the exact icon usage.

- **Title**: Replace `[Assignment Title]` with a short, descriptive name (e.g., `Python Basics`, `Loops and Conditionals`, `Functions and Modules`). Keep the `📘 Assignment:` prefix.
- **Objective**: Write 1-2 sentences summarizing what the student will learn or accomplish. Focus on the main skills or concepts.
- **Tasks**: For each task:
   - Use a specific, action-oriented task name with the `🛠️` icon.
   - In the Description, clearly state what the student must do.
   - In Requirements, use bullet points to list the expected outcomes or features. Be specific and measurable.
   - Provide example input/output in code blocks if helpful.

## 3. Content Standards

- Keep the assignment learning-focused and appropriate for the intended skill level.
- Use clear, encouraging language that students can understand independently.
- Keep requirements consistent with the provided starter code and assignment materials.
- Do not add extra top-level sections unless explicitly specified.
