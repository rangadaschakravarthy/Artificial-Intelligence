import numpy as np

def compute_iou(boxA, boxB):
    # box format: [x1, y1, x2, y2]
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    
    interArea = max(0, xB - xA) * max(0, yB - yA)
    
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
    
    unionArea = boxAArea + boxBArea - interArea
    iou = interArea / float(unionArea) if unionArea > 0 else 0.0
    return iou, interArea, unionArea

def main():
    print("--- Day 45: Sample Spaces and Events ---")
    
    # 1. Set Operations on Events
    Omega = set(range(1, 11)) # {1, 2, ..., 10}
    Event_A = {2, 4, 6, 8, 10} # Evens
    Event_B = {6, 7, 8, 9, 10} # Greater than 5
    
    print("
1. Set Operations:")
    print(f"  Sample Space Omega: {Omega}")
    print(f"  Event A (Evens):    {Event_A}")
    print(f"  Event B (> 5):      {Event_B}")
    print(f"  A Intersection B:   {Event_A.intersection(Event_B)}")
    print(f"  A Union B:          {Event_A.union(Event_B)}")
    print(f"  A Difference B:     {Event_A.difference(Event_B)}")
    
    # 2. Object Detection IoU Calculation
    gt_box = [50, 50, 150, 150]    # Ground truth box
    pred_box = [70, 70, 170, 170]  # Prediction box
    
    iou, inter, union = compute_iou(gt_box, pred_box)
    print("
2. Computer Vision Intersection over Union (IoU):")
    print(f"  Ground Truth Box: {gt_box}")
    print(f"  Predicted Box:    {pred_box}")
    print(f"  Intersection Area: {inter} sq px")
    print(f"  Union Area:        {union} sq px")
    print(f"  IoU Score:         {iou:.4f}")

if __name__ == "__main__":
    main()
