import os
import re

def get_pdf_dimensions(directory):
    pdf_dims = {}
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'rb') as f:
                    # Read the first 10KB, usually MediaBox is in the beginning or in pages object
                    # For a more robust check we might need to look further, but let's try 20KB
                    content = f.read(20480) 
                    
                    # Regex for MediaBox [llx lly urx ury]
                    match = re.search(rb'/MediaBox\s*\[\s*(-?[\d.]+)\s+(-?[\d.]+)\s+(-?[\d.]+)\s+(-?[\d.]+)\s*\]', content)
                    if match:
                        nums = [float(x) for x in match.groups()]
                        width_pts = abs(nums[2] - nums[0])
                        height_pts = abs(nums[3] - nums[1])
                        
                        # Convert points to inches (1 inch = 72 points)
                        w_in = width_pts / 72.0
                        h_in = height_pts / 72.0
                        
                        pdf_dims[filename] = f"{w_in:.2f} x {h_in:.2f} inches ({width_pts:.1f} x {height_pts:.1f} pts)"
                    else:
                        pdf_dims[filename] = "Dimension not found in header"
            except Exception as e:
                pdf_dims[filename] = f"Error: {str(e)}"
    return pdf_dims

target_dir = r"c:\Users\nihil\coding\novel\novel-assist-agent\library\references\D&D"
dims = get_pdf_dimensions(target_dir)

print("PDF Dimensions Report:")
for name in sorted(dims.keys()):
    print(f"{name}: {dims[name]}")
