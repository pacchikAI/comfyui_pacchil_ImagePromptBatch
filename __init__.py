import os
import csv 

class LoadImageandPrompt:

    def __init__(self):
        pass
 

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "FolderLocation": ("STRING",),
                "PromptFileName": ("STRING", ),
                "index": ("INT",),
            },
        }

    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("Image Name", "Prompt")


    FUNCTION = "LoadImageandPrompt"

    CATEGORY = "LoadImageandPrompt"

    def LoadImageandPrompt(self, index, FolderLocation, PromptFileName):
        PromptFileName = FolderLocation + PromptFileName
        with open(PromptFileName, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            header = next(reader, None)
            
            for row in reader:
                if len(row) >= 3:  # Ensure row has at least 3 columns
                    if str(index) == row[0]:
                        return FolderLocation+row[1], row[2]  # Return image_name and prompt
            

            print(f"No entry found with index {index}")
            return None, None

NODE_CLASS_MAPPINGS = {
    "LoadImageandPrompt": LoadImageandPrompt

}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadImageandPrompt": "Load Image and Prompt",
    
}
