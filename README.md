# Dynamic Object Coordinate Tracking

This module focuses on detecting and representing dynamic objects from a live camera feed using YOLO Pose and OpenCV.

## Current Pipeline

```text
Live Camera
     ↓
OpenCV Frame
     ↓
YOLO Pose Detection
     ↓
17 Body Keypoints
     ↓
(x, y) Coordinates
     ↓
Previous → Current Coordinates
     ↓
Movement / Trajectory Representation
```

## What the System Currently Does

* Captures live frames using OpenCV
* Detects a person using YOLO Pose
* Extracts 17 body keypoints
* Converts each keypoint into `(x, y)` coordinates
* Compares coordinates between consecutive frames
* Draws movement lines between previous and current coordinates
* Produces machine-readable coordinate information

## Coordinate System

The current YOLO frame is:

```text
Width  = 640 pixels
Height = 480 pixels
```

The coordinate origin is at the top-left:

```text
(0,0) ───────────────→ X
  |
  |
  |
  ↓
  Y
```

For a keypoint:

```text
Previous: (Xi, Yi)
Current:  (Xf, Yf)
```

Movement can be represented as:

```text
(Xi, Yi) → (Xf, Yf)
```

And calculated as:

```text
Δx = Xf - Xi
Δy = Yf - Yi
```

## Example

```text
Point_0:
Xi = 422
Yi = 473

Xf = 419
Yf = 474
```

Therefore:

```text
Movement:
(-3, +1)
```

This allows the system to represent movement using coordinates rather than storing the complete visual information from every frame.

## Example YOLO Pose Output

A single detected person produces 17 keypoints:

```text
(422.65, 473.74)
(474.58, 433.69)
(373.05, 427.75)
(528.22, 448.17)
...
```

These points can be connected according to the human pose skeleton to create a compact representation of the detected person.

## Current Goal

The next stages are:

```text
17 Keypoints
     ↓
Stable Object / Person ID
     ↓
Coordinate History
     ↓
Movement Direction
     ↓
State Comparison
     ↓
Changed Region / Object Information
```

## Technologies

* Python
* OpenCV
* YOLO Pose
* Ultralytics

## Project Context

This module is part of a larger environment-understanding system that aims to convert visual information into compact, machine-readable representations before higher-level reasoning is performed.
