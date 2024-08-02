import os
import subprocess
import sys
import venv

def create_virtual_environment(env_dir, python_executable):
    """Create a virtual environment using the specified Python executable."""
    if not os.path.exists(env_dir):
        print("Creating a virtual environment with Python 3.10...")
        subprocess.check_call([python_executable, '-m', 'venv', env_dir])
    else:
        print("Virtual environment already exists. Skipping creation.")

def activate_virtual_environment(env_dir):
    """Activate the virtual environment."""
    if os.name == 'nt':
        activate_script = os.path.join(env_dir, 'Scripts', 'activate')
    else:
        activate_script = os.path.join(env_dir, 'bin', 'activate')
    print(f"Activating the virtual environment using {activate_script}...")
    subprocess.call([activate_script], shell=True)

def get_site_packages_dir(env_dir):
    """Get the site-packages directory of the virtual environment."""
    python_executable = os.path.join(env_dir, 'bin' if os.name != 'nt' else 'Scripts', 'python')
    site_packages_dir = subprocess.check_output([python_executable, '-c', 'import site; print(site.getsitepackages()[0])'])
    return site_packages_dir.decode().strip()

def add_project_root_to_site_packages(env_dir):
    """Add the project root directory to the site-packages."""
    site_packages_dir = get_site_packages_dir(env_dir)
    project_root_dir = os.getcwd()
    pth_file_path = os.path.join(site_packages_dir, 'myproject.pth')
    
    with open(pth_file_path, 'w') as pth_file:
        pth_file.write(project_root_dir)
    
    print(f"Added {project_root_dir} to {pth_file_path}")
    print("Project root directory added to site-packages.")

def install_dependencies(env_dir):
    """Install dependencies from requirements.txt."""
    print("Installing dependencies from requirements.txt...")
    pip_executable = os.path.join(env_dir, 'bin' if os.name != 'nt' else 'Scripts', 'pip')
    subprocess.check_call([pip_executable, 'install', '-r', 'requirements.txt'])
    print("Dependencies installed.")

def run_script(env_dir, script_path):
    """Run a Python script."""
    python_executable = os.path.join(env_dir, 'bin' if os.name != 'nt' else 'Scripts', 'python')
    subprocess.check_call([python_executable, script_path])

def run_tests(env_dir):
    """Run pytest."""
    python_executable = os.path.join(env_dir, 'bin' if os.name != 'nt' else 'Scripts', 'python')
    subprocess.check_call([python_executable, '-m', 'pytest'])

def deactivate_virtual_environment():
    """Deactivate the virtual environment."""
    print("Deactivating the virtual environment...")
    # On Unix-like systems, this can be done by running 'deactivate' command in the shell
    # On Windows, this would be `venv\Scripts\deactivate.bat`
    # But it is usually enough to exit the current shell
    if os.name == 'nt':
        subprocess.call(['venv\\Scripts\\deactivate.bat'], shell=True)
    else:
        subprocess.call(['deactivate'], shell=True)

def main():
    env_dir = os.path.join(os.getcwd(), 'venv')

    # Check for Python 3.10
    python_executable = 'python3.10'
    try:
        subprocess.check_call([python_executable, '--version'])
    except subprocess.CalledProcessError:
        print("Error: This script requires Python 3.10.")
        sys.exit(1)

    create_virtual_environment(env_dir, python_executable)
    activate_virtual_environment(env_dir)
    add_project_root_to_site_packages(env_dir)
    
    print("Step 1: Starting to install dependencies...\n")
    install_dependencies(env_dir)
    print("Step 1: Dependencies installed.\n\n")
    
    print("Step 2: Starting data cleaning...\n")
    run_script(env_dir, 'scripts/clean_data.py')
    print("Step 2: Data cleaned.\n\n")
    
    print("Step 3: Starting data analysis...\n")
    run_script(env_dir, 'scripts/analyze_data.py')
    print("Step 3: Data analysis completed.\n\n")
    
    print("Step 4: Starting regression analysis...\n")
    run_script(env_dir, 'scripts/linear_regression.py')
    print("Step 4: Regression analysis completed.\n\n")
    
    print("Step 5: Starting tests...\n")
    run_tests(env_dir)
    print("Step 5: Tests completed.\n\n")

    deactivate_virtual_environment()
    print("All tasks completed!")

if __name__ == "__main__":
    main()
