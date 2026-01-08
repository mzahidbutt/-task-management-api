#!/usr/bin/env python3
"""
Initialize a new FastAPI project from template.

Usage:
    python init_project.py <project_name> [--path <output_directory>]

Example:
    python init_project.py my-api --path ./projects
"""

import argparse
import shutil
import sys
from pathlib import Path


def init_project(project_name: str, output_path: Path) -> None:
    """
    Initialize a new FastAPI project from template.

    Args:
        project_name: Name of the project
        output_path: Directory where the project will be created
    """
    # Get the template directory
    script_dir = Path(__file__).parent
    skill_dir = script_dir.parent
    template_dir = skill_dir / "assets" / "project-template"

    if not template_dir.exists():
        print(f"Error: Template directory not found at {template_dir}")
        sys.exit(1)

    # Create output directory
    project_dir = output_path / project_name

    if project_dir.exists():
        print(f"Error: Directory {project_dir} already exists!")
        sys.exit(1)

    # Copy template to output directory
    print(f"Creating FastAPI project: {project_name}")
    print(f"Location: {project_dir}")

    shutil.copytree(template_dir, project_dir)

    # Update .env file with project name
    env_file = project_dir / ".env.example"
    if env_file.exists():
        content = env_file.read_text()
        content = content.replace("FastAPI Project", project_name)
        env_file.write_text(content)

    print("\nProject created successfully!")
    print("\nNext steps:")
    print(f"1. cd {project_name}")
    print("2. python -m venv venv")
    print("3. source venv/bin/activate  # On Windows: venv\\Scripts\\activate")
    print("4. pip install -r requirements.txt")
    print("5. cp .env.example .env")
    print("6. fastapi dev main.py")
    print("\nYour API will be available at: http://localhost:8000")
    print("Interactive docs at: http://localhost:8000/docs")


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a new FastAPI project from template"
    )
    parser.add_argument(
        "project_name",
        help="Name of the project (e.g., my-api)",
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=Path.cwd(),
        help="Output directory (default: current directory)",
    )

    args = parser.parse_args()

    # Validate project name
    if not args.project_name.replace("-", "").replace("_", "").isalnum():
        print("Error: Project name can only contain letters, numbers, hyphens, and underscores")
        sys.exit(1)

    init_project(args.project_name, args.path)


if __name__ == "__main__":
    main()
