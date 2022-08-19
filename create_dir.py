from genericpath import exists
import os 
    
# Leaf directory 


dir_names = ["list_tables"]
for i in dir_names:
# Parent Directories 
    try:
        parent_dir = "dir/SOURCE/"
            
        # Path 
        path = os.path.join(parent_dir, i) 
        
 
        os.makedirs(path) 
    except:
        print ("already exist")