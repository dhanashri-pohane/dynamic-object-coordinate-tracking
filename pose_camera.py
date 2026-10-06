import cv2
from ultralytics import YOLO

model = YOLO("yolo11n-pose.pt")

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

previous_points = {}

while True:
    ret, frame = camera.read()

    if not ret:
        print("Camera not working")
        break

    results = model.track(frame, persist=True)

    annotated_frame = results[0].plot()

    if results[0].keypoints is not None:

        keypoints = results[0].keypoints.xy

        for person_index, person_points in enumerate(keypoints):

            for point_index, point in enumerate(person_points):

                x = int(point[0])
                y = int(point[1])

                current_key = (person_index, point_index)

                if current_key in previous_points:

                    old_x, old_y = previous_points[current_key]

                    # Draw movement line
                    cv2.line(
                        annotated_frame,
                        (old_x, old_y),
                        (x, y),
                        (255, 255, 255),
                        2
                    )

                    # Print machine-readable coordinate
                    print(
                        f"Point_{point_index}: "
                        f"Xi={old_x}, Yi={old_y} -> "
                        f"Xf={x}, Yf={y}"
                    )

                previous_points[current_key] = (x, y)

    cv2.imshow("YOLO Coordinate Tracking", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()