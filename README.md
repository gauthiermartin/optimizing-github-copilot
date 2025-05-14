# Optimizing Github Copilot

A comprehensive guide to maximizing productivity with GitHub Copilot in VS Code. This project collects best practices, commands, and techniques to help developers leverage the full power of AI pair programming through Copilot.

## Table of Contents

- [Getting Started](#getting-started)
  - [Project-Level Configuration](#project-level-configuration)
  - [User-Level Configuration](#user-level-configuration)
- [Instruction Files](#instruction-files)
  - [Types of Instruction Files](#types-of-instruction-files)
  - [How to Use Instruction Files](#how-to-use-instruction-files)
  - [Best Practices](#best-practices)
- [Chat Variables](#chat-variables)
- [Universal Commands](#universal-commands-available-in-ask-edit-and-agent-modes)
  - [Ask Mode Commands](#ask-mode-commands)
  - [Terminal Integration Commands](#terminal-integration-commands)
  - [VS Code Integration Commands](#vs-code-integration-commands)
  - [GitHub Integration Commands](#github-integration-commands)
  - [Agent Mode Commands](#agent-mode-commands-experimental)
- [Resources](#resources)

## Getting Started

This repository includes optimized configuration settings for GitHub Copilot in VS Code. These settings can be applied in two ways:

### Project-Level Configuration

For project-specific settings, copy the contents from this repository's `.vscode/settings.json` into your own project's `.vscode/settings.json` file. This will apply Copilot optimizations only for that specific project.

```jsonc
// .vscode/settings.json
{
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "text": "Generate Python code that adheres to the Ruff style guide..."
    }
  ],
  // Other Copilot settings...
}
```

### User-Level Configuration

To apply these settings globally across all your projects:

1. Open VS Code Settings (File > Preferences > Settings or Cmd/Ctrl+,)
2. Click on the "Open Settings (JSON)" icon in the top-right corner
3. Copy the GitHub Copilot related settings from this repository into your `settings.json`

This approach ensures consistent Copilot behavior across all your development work.


## Instruction Files

Instruction files allow you to customize GitHub Copilot's responses to match your specific coding practices and project requirements. These files contain natural language instructions in Markdown format that are automatically included in every chat request.

### Types of Instruction Files

1. **`.github/copilot-instructions.md`**: 
   - A single instruction file that applies workspace-wide
   - Contains all instructions for your workspace
   - Automatically included in every chat request
   - Requires setting `github.copilot.chat.codeGeneration.useInstructionFiles` to `true`

2. **`.instructions.md` files**:
   - Multiple specialized instruction files for specific tasks
   - Can be stored in two locations:
     - Workspace instructions: `.github/instructions` folder (project-specific)
     - User instructions: Stored in your VS Code profile (available across workspaces)

### How to Use Instruction Files

To create a `.github/copilot-instructions.md` file:

1. Set `github.copilot.chat.codeGeneration.useInstructionFiles` to `true` in your settings
2. Create a `.github/copilot-instructions.md` file at your workspace root
3. Add your coding guidelines, preferred technologies, and project requirements using Markdown

For `.instructions.md` files:

1. Run the "Chat: New Instruction File" command from the Command Palette
2. Choose where to store the instruction file (workspace or user profile)
3. Add a metadata header with an optional `applyTo` property to specify file patterns
4. Write your instructions in the body using Markdown

### Best Practices

- Keep instructions concise and focused
- Split instructions into multiple files organized by topic
- Use the `applyTo` property to automatically apply instructions to specific files
- Store instructions in version control to share with your team

Instruction files are particularly useful for:
- Enforcing coding standards across your team
- Specifying technology preferences and architecture guidelines
- Ensuring consistent code style and patterns
- Customizing Copilot's behavior for different parts of your project

## Chat Variables

Chat variables help provide relevant context to your GitHub Copilot prompts, making responses more accurate and tailored to your specific needs.

| Variable | Description |
|----------|-------------|
| `#changes` | Adds the list of source control changes as context |
| `#codebase` | Adds relevant workspace content as context to your prompt |
| `#extensions` | Tool to find and ask questions about VS Code extensions (e.g., "how to get started with Python #extensions?") |
| `#fetch` | Fetches content from a web page by providing the URL |
| `#<file or folder name>` | Type #, followed by a file or folder name to add it as chat context |
| `#githubRepo` | Performs code search for a GitHub repo (e.g., "what is a global snippet #githubRepo microsoft/vscode") |
| `#new` | Tool to scaffold a new VS Code workspace |
| `#newJupyterNotebook` | Tool to scaffold a new Jupyter notebook |
| `#openSimpleBrowser` | Opens the built-in Simple Browser to preview locally-deployed web apps |
| `#problems` | Adds workspace issues from the Problems panel as context |
| `#searchResults` | Adds results from the Search view as context |
| `#selection` | Adds the current editor selection as context |
| `#<symbol>` | Type #, followed by a symbol name to get symbol suggestions for workspace files |
| `#terminalSelection` | Adds the current terminal selection as context |
| `#terminalLastCommand` | Adds the last run terminal command as context |
| `#testFailure` | Adds test failure information as context |
| `#usages` | Combination of "Find All References", "Find Implementation", and "Go to Definition" |
| `#VSCodeAPI` | Adds the VS Code API as context for questions related to VS Code extension development |

## Universal Commands (Available in Ask, Edit, and Agent modes)

| Command | Description |
|---------|-------------|
| `/explain` | Ask Copilot to explain a block of code or a programming concept |
| `/fix` | Ask Copilot for suggestions on how to fix a block of code or resolve compiler/linting errors |
| `/fixTestFailure` | Get suggestions on how to fix failing tests |
| `/docs` | Generate documentation comments for methods and functions in the editor |
| `/tests` | Generate tests for methods and functions in the editor |

### Ask Mode Commands

| Command | Description |
|---------|-------------|
| `/setupTests` | Get help setting up a testing framework for your code |
| `/new` | Scaffold a new project or file based on your requirements |
| `/newNotebook` | Generate a new Jupyter notebook based on your requirements |

### Terminal Integration Commands

| Command | Description |
|---------|-------------|
| `@terminal` | Ask questions about the integrated terminal or shell commands |
| `@terminal /explain` | Explain something from the terminal |
| `copilot-debug` | Terminal command to help debug programs (prefix a run command) |

### VS Code Integration Commands

| Command | Description |
|---------|-------------|
| `@vscode` | Ask questions about VS Code features and settings |
| `@vscode /runCommand` | Run a VS Code command |
| `@vscode /search` | Generate a VS Code search |

### GitHub Integration Commands

| Command | Description |
|---------|-------------|
| `@github` | Ask about issues, pull requests, and more across your repositories |

### Agent Mode Commands (Experimental)

| Command | Description |
|---------|-------------|
| `/startDebugging` | Generate a launch.json debug configuration and start a debugging session |



## Model Context Protocol (MCP)
TODO
 



## Resources
- [Github Copilot VSCode Features](https://code.visualstudio.com/docs/copilot/reference/copilot-vscode-features)
- [Github Copilot Customization](https://code.visualstudio.com/docs/copilot/copilot-customization)
- [VS Code Agent Mode Just Changed Everything](https://youtu.be/dutyOc_cAEU?si=nD676VSQ25nPVO-g)
- [Smaller prompts, better answers with GitHub Copilot Custom Instructions](https://www.youtube.com/watch?v=zwIlqbTHjac)