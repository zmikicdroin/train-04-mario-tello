import os

# Paths to images and labels directories
images_dir = "images"
labels_dir = "labels"

# Collect all image filenames (without extension)
image_files = [f for f in os.listdir(images_dir) if f.endswith(".png")]
image_basenames = set(os.path.splitext(f)[0] for f in image_files)

# Collect all label filenames (without extension)
label_files = [f for f in os.listdir(labels_dir) if f.endswith(".txt")]
label_basenames = set(os.path.splitext(f)[0] for f in label_files)

# For each image that doesn't have a corresponding label, create an empty .txt file
unpaired_images = image_basenames - label_basenames
for base in unpaired_images:
    label_path = os.path.join(labels_dir, f"{base}.txt")
    open(label_path, "a").close()  # creates an empty file if it doesn't exist

print(f"Created {len(unpaired_images)} empty label files in '{labels_dir}'.")
