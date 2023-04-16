import cv2
import torch


class YOLOv5Detector:
    def __init__(self, model_name="yolov5s"):

        # default model
        self.model = torch.hub.load("ultralytics/yolov5", model_name)
        self.model.conf = 0.5

    def perform_inference(self, img):
        results = self.model(img)
        return results


    def show_detections(self, img, results):
        for det in results.xyxy[0]:
            label = det[5]
            score = det[4]
            bbox = det[:4]

            img = cv2.rectangle(
                img,
                (bbox[0].item(), bbox[1].item()),
                (bbox[2].item(), bbox[3].item()),
                (0, 0, 255),
                2,
            )

            cv2.putText(
                img,
                f"{label} {score:.2f}",
                (bbox[0], bbox[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                1,
            )

        cv2.imshow("Detections", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

