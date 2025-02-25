import os
import shutil

def setup_standalone():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create assets directory
    assets_dir = os.path.join(current_dir, "assets")
    cards_dir = os.path.join(assets_dir, "cards")
    os.makedirs(assets_dir, exist_ok=True)
    os.makedirs(cards_dir, exist_ok=True)
    
    # Create saves directory
    saves_dir = os.path.join(current_dir, "saves")
    os.makedirs(saves_dir, exist_ok=True)
    
    # Source paths for assets
    source_paths = {
        "background": r"C:\Users\Iraishaadi\Desktop\PDFs\Program\BaccaratTable.jpg",
        "shoe": r"C:\Users\Iraishaadi\Desktop\PDFs\Program\SHOE-removebg-preview.png",
        "win_sound": r"C:\Users\Iraishaadi\Desktop\PDFs\Program\WIN sound effect no copyright.mp3",
        "music": r"C:\Users\Iraishaadi\Desktop\PDFs\Program\Las Vegas Casino Music Video_ For Night Game of Poker, Blackjack, Roulette Wheel & Slots.mp3",
        "red_chip": r"C:\Users\Iraishaadi\Desktop\PDFs\Program\pokerchip1.png",
        "blue_chip": r"C:\Users\Iraishaadi\Desktop\PDFs\Program\pokerchip3.png",
        "yellow_chip": r"C:\Users\Iraishaadi\Desktop\PDFs\Program\pokerchip4.png"
    }
    
    # Destination paths in assets directory
    dest_paths = {
        "background": os.path.join(assets_dir, "BaccaratTable.jpg"),
        "shoe": os.path.join(assets_dir, "SHOE-removebg-preview.png"),
        "win_sound": os.path.join(assets_dir, "WIN sound effect no copyright.mp3"),
        "music": os.path.join(assets_dir, "Las Vegas Casino Music.mp3"),
        "red_chip": os.path.join(assets_dir, "pokerchip1.png"),
        "blue_chip": os.path.join(assets_dir, "pokerchip3.png"),
        "yellow_chip": os.path.join(assets_dir, "pokerchip4.png")
    }
    
    # Copy assets
    for key, source in source_paths.items():
        dest = dest_paths[key]
        try:
            shutil.copy2(source, dest)
            print(f"Copied {key} to {dest}")
        except Exception as e:
            print(f"Error copying {key}: {e}")
    
    # Copy card images
    cards_source = r"\\IRAISHAADI\Users\Iraishaadi\Desktop\PDFs\Program\Playing Cards\PNG-cards-1.3"
    try:
        for file in os.listdir(cards_source):
            if file.endswith(".png"):
                source = os.path.join(cards_source, file)
                dest = os.path.join(cards_dir, file)
                shutil.copy2(source, dest)
                print(f"Copied card {file}")
    except Exception as e:
        print(f"Error copying cards: {e}")
    
    print("\nSetup complete!")
    print("Please verify that all assets were copied correctly.")

if __name__ == "__main__":
    setup_standalone()
