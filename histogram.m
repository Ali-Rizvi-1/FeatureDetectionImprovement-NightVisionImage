clc; clear; close all;

lion = imread('LionImage.jpg');
lionNV = imread('LionImageNightVision.jpg');

B = imresize(lion,[589 943]) 
imwrite(B, "LionImage2.jpg", "Quality", 100) 

equal_img = imadjust(im2gray(lionNV));

subplot 321
imshow(lion); xlabel('Original Image');
subplot 322
imhist(lion); ylim('auto')
subplot 323
imshow(lionNV); xlabel('Night Vision Image');
subplot 324
imhist(lionNV); ylim('auto')
subplot 325
imshow(equal_img); xlabel('Equalized Histogram Image')
subplot 326
imhist(equal_img); ylim('auto')

figure;
imshow(equal_img)

imwrite(equal_img, "AdjustedLionImage.jpg", "Quality", 100) 
