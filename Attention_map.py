from PIL import Image
import torch
from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np


# Path to the input image
image_path = '/content/1038.jpg'  # Replace with your actual image path

# Load and preprocess the image
def load_and_preprocess_image(image_path):
    # Define DINO-specific preprocessing transformations
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),               # Resize to model's input size
        transforms.ToTensor(),                       # Convert to tensor
        transforms.Normalize(mean=[0.485, 0.456, 0.406],  # Normalize with ImageNet mean
                             std=[0.229, 0.224, 0.225])
    ])
    
    # Load image and apply transformations
    image = Image.open(image_path).convert("RGB")   # Ensure it's RGB
    image_tensor = preprocess(image).unsqueeze(0)   # Add batch dimension
    return image_tensor

# Get preprocessed image tensor
input_image = load_and_preprocess_image(image_path)

# Register hooks to capture attention maps from self-attention layers
def get_attention_maps(model, input_image):
    attention_maps = []

    def hook(module, input, output):
        # Add the attention map to the list
        attention_maps.append(output.detach().cpu())
    
    # Loop through model's transformer layers and register the hook to the self-attention
    hooks = []
    for layer in model.transformer.layers:
        hook_handle = layer.self_attn.register_forward_hook(hook)
        hooks.append(hook_handle)
    
    # Forward pass to get attention maps
    _ = model(input_image)
    
    # Remove hooks after extraction
    for hook in hooks:
        hook.remove()
    
    return attention_maps

# Visualization function
def visualize_attention_map(attention_map, image, layer_idx=0, head_idx=0):
    # Get specific layer and head attention map
    attention = attention_map[layer_idx][0, head_idx].numpy()
    
    # Resize attention map to match image dimensions
    attention_resized = np.array(Image.fromarray(attention).resize(image.shape[1:3], resample=Image.BILINEAR))

    # Display image with attention overlay
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    ax.imshow(image.permute(1, 2, 0))  # Convert tensor to image format
    ax.imshow(attention_resized, cmap='jet', alpha=0.5)
    plt.axis('off')
    plt.show()

# Assuming 'model' is your DINO model and 'input_image' is a preprocessed tensor image
input_image = ...  # Add code to preprocess and load your image
attention_maps = get_attention_maps(model, input_image)

# Visualize the attention for a specific layer and head
visualize_attention_map(attention_maps, input_image, layer_idx=11, head_idx=0)  # Choose appropriate layer and head
