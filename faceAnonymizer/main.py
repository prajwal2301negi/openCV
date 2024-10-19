import cv2
import os

import mediapipe as mp

output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# read Images
img = cv2.imread(os.path.join('.', 'data', 'humanFace.webp'))

H, W, _ = img.shape

# detect Faces
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection = 0, min_detection_confidence = 0.5) as face_detection:
    # 0 is use when image is near and 1 is use when image is far away
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)
    
    print(out.detections)
#     [label_id: 0
# score: 0.905619621
# location_data {
#   format: RELATIVE_BOUNDING_BOX
#   relative_bounding_box {
#     xmin: 0.220698819
#     ymin: 0.273925185
#     width: 0.56406337
#     height: 0.424806893
#   }
#   relative_keypoints {
#     x: 0.37256515
#     y: 0.393028408
#   }
#   relative_keypoints {
#     x: 0.601374626
#     y: 0.393263549
#   }
#   relative_keypoints {
#     x: 0.474316776
#     y: 0.501546383
#   }
#   relative_keypoints {
#     x: 0.480501473
#     y: 0.584580541
#   }
#   relative_keypoints {
#     x: 0.269065917
#     y: 0.428689182
#   }
#   relative_keypoints {
#     x: 0.742702067
#     y: 0.429675043
#   }
# }
# ]



    for detection in out.detections:
        location_data = detection.location_data
        bbox = location_data.relative_bounding_box
        # from data

        x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

        x1 = int(x1 * W)
        y1 = int(y1 * H)
        w = int(w* W)
        h = int(h * H)

        cv2.rectangle(img, (x1, y1), (x1+w, y1+h), (0, 255, 0), 10)

        cv2.imshow('img', img)
        cv2.waitKey(0)


# blur Faces
img[y1:y1+h, x1:x1+w, :] = cv2.blur(img[y1:y1+h, x1:x1+w, :], (10,10))

cv2.imshow('img',img)
cv2.waitKey(0)

# save Images
cv2.imwrite(os.path.join(output_dir, 'output.webp'), img)