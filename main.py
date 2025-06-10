import os
import sys

def configure_enchant_paths():
    if getattr(sys, 'frozen', False):  # Running in bundled EXE (MSIX or PyInstaller)
        base_dir = os.path.dirname(sys.executable)
        print("Running from bundled EXE.")
    else:  # Running from source
        base_dir = os.path.dirname(os.path.abspath(__file__))
        print("Running from source/development.")

    # Enchant directory structure
    
    enchant_config_dir = os.path.join(os.path.dirname(sys.executable), "_internal", "enchant")


    # Set environment variables
    os.environ["ENCHANT_CONFIG_DIR"] = enchant_config_dir


try:
    configure_enchant_paths()

    import enchant
    d = enchant.Dict("en_US")

    word = "hello"
    print(f"Checking '{word}':", d.check(word))
    print("Suggestions for 'helllo':", d.suggest("helllo"))
except Exception as e:
    print("❌ Error loading enchant or dictionary:", e)

input("Press Enter to exit...")
