import os
import subprocess
import glob

def clean_name(filename):
    # Remove extension, replace underscores/hyphens with spaces
    base = os.path.splitext(filename)[0]
    cleaned = base.replace('_', ' ').replace('-', ' ')
    # Capitalize words
    return ' '.join(word.capitalize() for word in cleaned.split())

def commit_file_by_file(base_dir):
    valid_exts = ['.py', '.html', '.css', '.js', '.sql']
    
    # 1. Reset everything first just in case
    subprocess.run(["git", "reset"])
    
    # We will traverse the directory and find all source files
    for root, dirs, files in os.walk(base_dir):
        if 'output' in root.lower() or 'node_modules' in root.lower() or '.git' in root.lower():
            continue
            
        for filename in files:
            ext = os.path.splitext(filename)[1].lower()
            if ext in valid_exts:
                file_path = os.path.join(root, filename)
                
                # Get the relative path for git
                rel_path = os.path.relpath(file_path)
                
                # Determine Module/Task details for commit message
                parts = rel_path.split(os.sep)
                # Parts might look like: ['Deep_upskilling', 'Module-1', 'Design_Pattern_exercise', '1_SingletonPatternExample.py']
                # or ['Deep_upskilling', 'Module2_FrontendDev', 'handson_01', 'index.html']
                
                module_name = "General"
                for part in parts:
                    if "module" in part.lower() or "upskilling" in part.lower() or "basics" in part.lower() or "frameworks" in part.lower():
                        module_name = part
                        break
                
                cleaned_task = clean_name(filename)
                commit_message = f"[{module_name}] Add {cleaned_task} exercise implementation"
                
                print(f"Staging source: {rel_path}")
                subprocess.run(["git", "add", rel_path])
                
                # Check for corresponding output image in parallel output directory
                # E.g. root/output/filename.png (python filenames replace .py with .png)
                # or html filenames replace .html with .html.png
                possible_output_names = [
                    filename + ".png",
                    filename.replace(ext, ".png")
                ]
                
                # Look for 'output' folder in the current directory or parent directories
                output_dir = os.path.join(root, "output")
                if os.path.exists(output_dir):
                    for out_name in possible_output_names:
                        out_path = os.path.join(output_dir, out_name)
                        if os.path.exists(out_path):
                            rel_out_path = os.path.relpath(out_path)
                            print(f"Staging screenshot: {rel_out_path}")
                            subprocess.run(["git", "add", rel_out_path])
                            break
                            
                # Execute Commit
                print(f"Committing: {commit_message}")
                subprocess.run(["git", "commit", "-m", commit_message])

# Run it
commit_file_by_file(".")

# Commit any remaining files (README, gitignore, helper scripts)
remaining_files = [".gitignore", "README.md", "run_all.ps1"]
for f in remaining_files:
    if os.path.exists(f):
        subprocess.run(["git", "add", f])
        
subprocess.run(["git", "commit", "-m", "[General] Add project documentation and scripts"])
print("All tasks committed individually!")
