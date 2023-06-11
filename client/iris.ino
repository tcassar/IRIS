#include "ESP8266.h"
#include "Camera.h"

#define SSID "Tom's iPhone (2)"
#define PASSWORD "hotspot1234"
#define HOST_NAME   "172.20.10.8"
#define HOST_PORT   (5000)

ESP8266 wifi;

void setupWifi() {
  Serial.print("setup Wi-Fi");
  Serial1.begin(115200);

  // initialise the wi-fi library
  wifi.begin(Serial2, 115200);

  // check wi-fi firmware version
  Serial.print("Wi-Fi FW Version: ");
  Serial.println(wifi.getVersion().c_str());

  // set operation mode to station
  if (wifi.setOprToStation()) {
    Serial.print("to station ok\r\n");
  } else {
    Serial.print("to station err\r\n");
  }

  // join access point
  if (wifi.joinAP(SSID, PASSWORD)) {
    Serial.print("Join AP success\r\n");
    Serial.print("IP: ");
    Serial.println(wifi.getLocalIP().c_str());
  } else {
    Serial.print("Join AP failure\r\n");
  }

  // activate single connection mode - required to create a TCP connection
  if (wifi.disableMUX()) {
    Serial.print("single ok\r\n");
  } else {
    Serial.print("single err\r\n");
  }

  Serial.print("Wi-Fi setup complete\r\n");
}

void printCameraError(enum CamErr err) {
  Serial.print("Error: ");
  switch (err) {
    case CAM_ERR_NO_DEVICE:
      Serial.println("No Device");
      break;
    case CAM_ERR_ILLEGAL_DEVERR:
      Serial.println("Illegal device error");
      break;
    case CAM_ERR_ALREADY_INITIALIZED:
      Serial.println("Already initialized");
      break;
    case CAM_ERR_NOT_INITIALIZED:
      Serial.println("Not initialized");
      break;
    case CAM_ERR_NOT_STILL_INITIALIZED:
      Serial.println("Still picture not initialized");
      break;
    case CAM_ERR_CANT_CREATE_THREAD:
      Serial.println("Failed to create thread");
      break;
    case CAM_ERR_INVALID_PARAM:
      Serial.println("Invalid parameter");
      break;
    case CAM_ERR_NO_MEMORY:
      Serial.println("No memory");
      break;
    case CAM_ERR_USR_INUSED:
      Serial.println("Buffer already in use");
      break;
    case CAM_ERR_NOT_PERMITTED:
      Serial.println("Operation not permitted");
      break;
    default:
      break;
  }
}

void setupCamera() {
  CamErr err;

  // open serial communications
  Serial.begin(115200);

  // wait for the serial port to open - needed for native USB port
  while (!Serial) {}

  Serial.println("Prepare camera");
  // prepare the camera
  // default parameters: number of buffers = 1, 30FPS, QVGA, YUV 4:2:2 format
  err = theCamera.begin();
  if (err != CAM_ERR_SUCCESS) {
    printCameraError(err);
  }

  // Auto white balance configuration
  Serial.println("Set Auto white balance parameter");
  err = theCamera.setAutoWhiteBalanceMode(CAM_WHITE_BALANCE_DAYLIGHT);
  if (err != CAM_ERR_SUCCESS) {
    printCameraError(err);
  }

  Serial.println("Set still picture format");
  // set the still picture resolution to QUADVGA (1280x960) and the format to JPEG
  err = theCamera.setStillPictureImageFormat(
    CAM_IMGSIZE_QUADVGA_H,
    CAM_IMGSIZE_QUADVGA_V,
    CAM_IMAGE_PIX_FMT_JPG);
  if (err != CAM_ERR_SUCCESS) {
    printCameraError(err);
  }
}

void connectToServer() {
  // create a TCP connection to the server
  if (wifi.createTCP(HOST_NAME, HOST_PORT)) {
      Serial.print("create tcp ok\r\n");
  } else {
      Serial.print("create tcp err\r\n");
  }
}

void disconnectFromServer() {
  // release the TCP connection
  if (wifi.releaseTCP()) {
      Serial.print("release tcp ok\r\n");
  } else {
      Serial.print("release tcp err\r\n");
  }
}

void sendPhoto(CamImage image) {
  Serial.println("Send photo");

  // create a TCP connection to the server
  connectToServer();

  // pre-allocate 100 bytes for the request
  // TODO: is this enough?
  char request[100];

  // format the request
  sprintf(request, "POST / HTTP/1.1\r\nContent-Type: image/jpeg\r\nContent-Length: %i\r\n\r\n%s ", image.getImgBuffSize());

  // concat the raw image bytes to the end of the request
  strncat(request, image.getImgBuff(), image.getImgBuffSize());

  Serial.println(request);
  // send the request over TCP
  wifi.send(request, strlen(request));

  // release the TCP connection when we're done
  disconnectFromServer();
}

void takePhoto() {
  Serial.println("Take photo");

  // take the photo
  CamImage image = theCamera.takePicture();
  if (!image.isAvailable()) {
    Serial.println("CAMERA error");
    return;
  }

  // send the photo
  sendPhoto(image);
}

void setup(void) {
  Serial.begin(9600);
  Serial.println("Begin Setup");
  setupWifi();
  setupCamera();
  Serial.println("Setup Complete");

  // take a photo immediately after setup is complete
  // TODO: this should be done when the wake word is heard
  takePhoto();
}

void loop(void) {
}