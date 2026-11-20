Practical examples of **Conventional Commits**, tailored specifically to the `standard-version` tool you are using. 

The format is: `<type>(<optional scope>): <description>`

### 1. Features
Since you are adding , you will mostly use `feat`.
```bash
# Adding a new lab
git commit -m "feat(lab06): add report and presentation"

# Adding a new section to an existing lab
git commit -m "feat(lab05): add conclusion section"

# Updating the main template
git commit -m "feat: add new course catalog template structure"
```

### 2. Fixing mistakes (Bug Fixes)
When you fix a typo in your Markdown, a broken link, or a rendering error.
```bash
# Fixing a typo or broken link
git commit -m "fix(lab06): correct broken image link"

# Fixing a Quarto rendering issue
git commit -m "fix: resolve PDF rendering error in header"

# Fixing a typo in the README
git commit -m "fix(readme): correct spelling of scientific writing"
```

### 3. Documentation (Docs)
When you only change documentation, instructions, or the changelog.
```bash
# Updating instructions
git commit -m "docs: update installation steps for Quarto"

# The commit you made for the release
git commit -m "docs: add changelog for v6.0.0" 
```

### 4. Maintenance (Chores)
When you update tools, dependencies, or config files, but don't change the actual course content.
```bash
# Updating Node.js packages (like standard-version)
git commit -m "chore: update standard-version to latest version"

# Changing a config file
git commit -m "chore: add .gitignore for build folders"
```

### 5. Refactoring (Refactor)
When you change the code or structure but *don't* add a feature or fix a bug (e.g., moving files around).
```bash
# Moving files to a new folder
git commit -m "refactor: move lab06 images to assets folder"
```

---

### Pro-Tips for your specific setup:

1. **The Scope (the parentheses):** `(lab06)` or `(readme)` is optional but highly recommended. It tells the reader *exactly* which part of the project you changed.
2. **Imperative Mood:** Always write the description as if you are giving a command. Use **"add"**, **"fix"**, **"update"**, **"change"**—not "added", "fixes", or "updating".
   * *Good:* `feat(lab06): add presentation`
   * *Bad:* `feat(lab06): added presentation`

3. **The Magic of `standard-version`:** When you run `npx standard-version` for your release, it will look at these prefixes:
   * `feat:` will bump the **MINOR** version (e.g., 5.1.0 → 5.2.0)
   * `fix:` will bump the **PATCH** version (e.g., 5.1.0 → 5.1.1)
   * `feat!:` or `BREAKING CHANGE:` in the body will bump the **MAJOR** version (e.g., 5.1.0 → 6.0.0)
   * `chore:`, `docs:`, `refactor:` usually **do not** trigger a version bump, but they *will* be grouped nicely in the `CHANGELOG.md`.