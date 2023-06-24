from PIL import Image
import torch
from transformers import OwlViTProcessor, OwlViTForObjectDetection

model_dir = "saved_model"

# processor = OwlViTProcessor.from_pretrained("google/owlvit-base-patch32")
# model = OwlViTForObjectDetection.from_pretrained("google/owlvit-base-patch32")

# Save model and processor to local files
# os.makedirs(model_dir, exist_ok=True)
# processor.save_pretrained(model_dir)
# model.save_pretrained(model_dir)

# Load model and processor from local files
processor = OwlViTProcessor.from_pretrained(model_dir)
model = OwlViTForObjectDetection.from_pretrained(model_dir)
texts = [["a photo of a person talking to phone", "phone", "mobile", "cellphone", "telephone"]]

def infere_phone(image):

    image = Image.fromarray(image)
    image = image.resize((384, 384))
    
    inputs = processor(text=texts, images=image, return_tensors="pt")
    outputs = model(**inputs)

    # Target image sizes (height, width) to rescale box predictions [batch_size, 2]
    target_sizes = torch.Tensor([image.size[::-1]])
    # Convert outputs (bounding boxes and class logits) to COCO API
    results = processor.post_process(outputs=outputs, target_sizes=target_sizes)

    i = 0  # Retrieve predictions for the first image for the corresponding text queries
    text = texts[i]
    boxes, scores, labels = results[i]["boxes"], results[i]["scores"], results[i]["labels"]

    # Print detected objects and rescaled box coordinates
    c = 0
    score_threshold = 0.15
    for box, score, label in zip(boxes, scores, labels):
        box = [round(i, 2) for i in box.tolist()]
        if score >= score_threshold:
            c += 1
            print(f"Detected {text[label]} with confidence {round(score.item(), 3)} at location {box}")
    if c > 0:
        return 1
    return 0
