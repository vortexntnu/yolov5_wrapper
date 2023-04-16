import cv2
import torch



class YOLOv5Detector:
    def __init__(self, model_name='yolov5s'):
        # load model using Torch
        self.model = torch.hub.load("ultralytics/yolov5", model_name)
        self.conf_thres=0.5


        # # from a local directory
        # path = '/some/local/path/pytorch/vision'
        # # xdoctest: +SKIP
        # model = torch.hub.load(path, 'resnet50', weights='ResNet50_Weights.DEFAULT')
        
    def perform_inference(self, img):

        #results = self.model(img, conf_thres=self.conf_thres)
        results = self.model(img)
        return results
    
    def show_detections(self, img, results):

        # draw bounding box onto image
        for det in results.xyxy[0]:
            label = det[5]
            score = det[4]
            bbox = det[:4]

            # draw rectangle on image
            img = cv2.rectangle(img, (bbox[0].item(), bbox[1].item()), (bbox[2].item(), bbox[3].item()), (0, 0, 255), 2)
            # put label and score on image
            cv2.putText(img, f"{label} {score:.2f}", (bbox[0], bbox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        cv2.imshow("Detections", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



# # load image using OpenCV
# img = cv2.imread("/home/vortex/perception_ws/src/temp_yolov5_wrapper/yolov5_wrapper/data/images.jpeg")

# # load model using Torch
# model = torch.hub.load("ultralytics/yolov5", "yolov5s")

# # perform inference
# results = model(img)

# # print label, score, and bounding box coordinates of each detection
# for det in results.xyxy[0]:
#     label = det[5]
#     score = det[4]
#     bbox = det[:4]
#     bbox = bbox.int()  # convert to integers
#     print("Label: ", label)
#     print("Score: ", score)
#     print("Bounding Box: ", bbox)

#     # draw bounding box onto image
#     x1, y1, x2, y2 = bbox
#     print('x1', x1.item())
#     img = cv2.rectangle(img, (x1.item(), y1.item()), (x2.item(), y2.item()), (0, 255, 0), 2)

# # display image
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
