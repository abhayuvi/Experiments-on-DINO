import re
import matplotlib.pyplot as plt
from subprocess import Popen, PIPE

# Initialize lists to store different losses for plotting
epochs, loss_values = [], []
loss_ce_values, loss_bbox_values, loss_giou_values = [], [], []

# Execute the training script and capture the output
process = Popen(['bash', 'scripts/DINO_train.sh', '/content/DATASET'], stdout=PIPE, stderr=PIPE, text=True)

# Regular expressions to capture loss values from the output
epoch_pattern = re.compile(r"Epoch: \[(\d+)\]")
loss_pattern = re.compile(r"loss: ([\d.]+)")
loss_ce_pattern = re.compile(r"loss_ce: ([\d.]+)")
loss_bbox_pattern = re.compile(r"loss_bbox: ([\d.]+)")
loss_giou_pattern = re.compile(r"loss_giou: ([\d.]+)")

for line in process.stdout:
    print(line, end='')  # Print training log
    # Extract epoch
    epoch_match = epoch_pattern.search(line)
    if epoch_match:
        epochs.append(int(epoch_match.group(1)))
    # Extract main loss
    loss_match = loss_pattern.search(line)
    if loss_match:
        loss_values.append(float(loss_match.group(1)))
    # Extract classification, bounding box, and giou losses
    loss_ce_match = loss_ce_pattern.search(line)
    if loss_ce_match:
        loss_ce_values.append(float(loss_ce_match.group(1)))
    loss_bbox_match = loss_bbox_pattern.search(line)
    if loss_bbox_match:
        loss_bbox_values.append(float(loss_bbox_match.group(1)))
    loss_giou_match = loss_giou_pattern.search(line)
    if loss_giou_match:
        loss_giou_values.append(float(loss_giou_match.group(1)))

process.wait()

# Plot the loss values
plt.figure(figsize=(10, 6))
plt.plot(epochs, loss_values, label="Total Loss")
plt.plot(epochs, loss_ce_values, label="Classification Loss (loss_ce)")
plt.plot(epochs, loss_bbox_values, label="Bounding Box Loss (loss_bbox)")
plt.plot(epochs, loss_giou_values, label="GIoU Loss (loss_giou)")

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss Curves")
plt.legend()
plt.grid()
plt.show()
