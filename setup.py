from cx_Freeze import setup, Executable

setup(
    name = "Space ships",
    version = "0.1",
    description = "Space ships",
    executables = [Executable("menu.py")]
)