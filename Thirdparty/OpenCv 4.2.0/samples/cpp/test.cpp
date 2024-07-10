#include <iostream>
#include <opencv2/opencv.hpp>
using namespace std;
using namespace cv;
int main()
{
   Mat img=imread("test.jpg");//
   imshow("test",img);
   waitKey(5000);
   return 0;
}