# **Car & Pedestrian Tracker With Python**

컴퓨터 비전을 이용한 **자동차&보행자 추적** 어플리케이션입니다. <br>
**`Haar-Like Feature`** 알고리즘을 사용합니다. <br>
**[OpenCV](https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html?highlight=detectmultiscale)** 라이브러리를 사용합니다.


<br><br>

## **`Haar-Like Feature`**
얼굴, 이미지 혹은 실시간 영상을 인식하기 위해 사용되는 사물 인식 알고리즘입니다.

<br>

![논문에 있던 샘플사진 by Viola and Jones](https://miro.medium.com/max/1400/1*fQBZTdPk_YzaR7If7Sjzxg.png)
위와 같이 하얗고 검은 부분이 있는 네모난 박스를 픽셀에 대입해보면서 목표물과 같은 부분과 다른 부분을 찾습니다.
<br>

<br>

**[Haar 알고리즘을 시각화 한 영상](https://youtu.be/hPCTwxF0qf4)**

<br><br>

## **과정**
- 사진들 혹은 영상을 준비합니다.
- 준비한 것을 흑백으로 처리합니다. 필요하다면 영상 화질도 낮춥니다.
    - 알고리즘을 빠르게 인식시키기 위해서 컬러를 배제하고 영상 화질을 낮춥니다. 
        - 컬러를 배제하고 화질을 낮춰도 `Haar-Like Feature` 알고리즘은 자동차의 모양을 인식할 수 있습니다.(그늘진 곳과 덜 그늘진 곳을 인식하기 때문.)
- 목표물을 인식하기 위해 `Haar-Like Feature` 알고리즘을 학습시킵니다. 
    - 여기서는 미리 학습된 `xml` 파일을 가져다 사용하였습니다.
        - [자동차](https://raw.githubusercontent.com/andrewssobral/vehicle_detection_haarcascades/master/cars.xml)
        - [보행자](https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_fullbody.xml)
- 학습된 것을 이용하여 이미지나 영상에서 자동차와 보행자를 찾아 각각 자동차에게는 빨간색 네모를, 보행자에게는 노란색 네모를 씌웁니다.

<br><br>

## **실습**

```
pip install opencv-python
```

- `fork` 한 뒤 로컬에 내려받아 openCV를 설치합니다.
    - openCV 설치는 python 가상환경을 만들고 하길 권장드립니다.

```
video = cv2.VideoCapture('영상제목.mp4')
```
- 사용하고 싶은 영상을 폴더에 넣고 해당 영상 제목을 `video = cv2.VideoCapture()` 함수에 str변수로 넣어주세요.
- **`Car_and_Pedestrian_Tracking.py`** 를 실행해주세요. <br>

<br><br>


* * *
[참고자료]

<br>

[Face Detection with Haar Cascade](https://towardsdatascience.com/face-detection-with-haar-cascade-727f68dafd08)
<br>
[Build AI Car & Pedestrian Tracking with Python for Beginners (Tutorial)](https://www.youtube.com/watch?v=zg9X6ASj3Q0&ab_channel=CleverProgrammer)