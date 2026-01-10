import json
import os

def cleanup_other_json():
    file_path = r"c:\Users\nihil\coding\novel\novel-assist-agent\data\word_list\_archive\other.json"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        keys_to_remove = ["날씨", "도구"]
        removed_keys = []
        
        for key in keys_to_remove:
            if key in data:
                del data[key]
                removed_keys.append(key)
        
        if not removed_keys:
            print("No extracted keys found to remove.")
            return

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print(f"Successfully removed keys: {', '.join(removed_keys)} from {file_path}")
        
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON file: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    cleanup_other_json()
