    x1, y1, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)