import cv2
import numpy as np
from PIL import Image, ImageEnhance

def ghibli_effect(image_path, output_path):
    # Load image
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Apply bilateral filter for soft edges
    filtered = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
    
    # Convert to PIL for additional enhancements
    pil_img = Image.fromarray(filtered)
    
    # Enhance color
    enhancer = ImageEnhance.Color(pil_img)
    pil_img = enhancer.enhance(1.5)
    
    # Enhance contrast
    enhancer = ImageEnhance.Contrast(pil_img)
    pil_img = enhancer.enhance(1.2)
    
    # Convert back to OpenCV format
    final_img = np.array(pil_img)
    final_img = cv2.cvtColor(final_img, cv2.COLOR_RGB2BGR)
    
    # Save output image
    cv2.imwrite(output_path, final_img)
    
    print(f"Ghibli effect applied. Saved as {output_path}")

# Example usage
ghibli_effect("input.jpg", "output.jpg")
