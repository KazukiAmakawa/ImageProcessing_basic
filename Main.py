#=================================================================
#
#		Image Processing - Main
#		Copyright(c) KazukiAmakawa, all right reserved.
#
#=================================================================
#This is the main function of the program, all program will begin from this program
#May cannot compile under the Windows System.

#import head
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path
import math
import matplotlib.patches as patches
from scipy import misc
from collections import deque
from PIL import ImageFilter
import cv2
import random 


#import files
import GradFig
import Init
import Proj1
import Proj2
import Proj3
import Proj4
import Proj5
import ProjTest
import TimeCal
import Algorithm
import Convolution
import Trans
import ImgEnp


#return img array: the array of the figure
#return -1 : exit or no figure
def FigureInput():
	Figure = []
	Name = []
	root0 = ""
	for root, dirs, files in os.walk(os.getcwd()):
		if root0 == "":
			root0 = root
			root0 += "/Output"
		if root0 == root:
			continue

		for i in range(0, len(files)):
			LocStr = root + "/" + files[i]
			
			Hajimari = 0
			Last = ""

			for j0 in range(0, len(files[i])):
				j = len(files[i]) - j0 -1
				if files[i][j] == ".":
					break
				else:
					Last = files[i][j] + Last

			if Last == "bmp" or Last == "jpg" or Last == "png":
				Figure.append(LocStr)
				Name.append(files[i])

	if len(Figure) == 0:
		print("No Figure")
		return -1

	for i in range(0, len(Figure)):
		print(str(i+1) + "\t" + Name[i])
	print("0\tEXIT")

	InpInt = 0
	while 1:
		InpStr = input("Choose a figure with code:  ")
		try:
			InpInt = int(InpStr)
		except ValueError:
			print("Input Error")
			continue
		else:
			if InpInt < 0 or InpInt > len(Figure):
				print("input Error")
				continue
			else:
				break

	if InpInt == 0:
		return -1
	else:
		NameStr = Figure[InpInt-1]

	Init.LogWrite("Figure input succeed", "0")
	return np.array(Image.open(NameStr).convert("L"))


def Output(img):
	plt.imshow(img, cmap="gray")
	plt.axis("off")
	plt.show()
	Init.LogWrite("Figure output succeed", "0")
	InpStr = input("Save the figure?[Y/ n]")
	if InpStr == "Y" or InpStr == "y":
		Name = "Figure_"
		Name += str(TimeCal.GetTime())
		Name += ".png"
		os.system("cp null " + Name)
		misc.imsave(Name, img)
		if not os.path.exists("Output"):
			os.system("mkdir Output")
		os.system("mv " + Name + " Output/" + Name)
	return


def MET(img):
	METi = 0
	METSum = -99999.00
	Sum = [0 for n in range(260)]
	Pro = [0.000 for n in range(260)]
	ProSum = [0.000 for n in range(260)]
	TTL = len(img) * len(img[0])

	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			Sum[int(img[i][j])] += 1

	for i in range(0, len(Sum)):
		Pro[i] = Sum[i] / TTL
		if i != 0:
			ProSum[i] = ProSum[i-1] + Pro[i]
		else:
			ProSum[i] = Pro[i]

	for i in range(0, len(ProSum)):
		Ent = 0
		for j in range(0, len(Pro)):
			if Pro[j] == 0:
				continue
			if j <= i:
				Ent -= (Pro[j]/ProSum[i] * math.log(Pro[j]/ProSum[i]+0.001))
			else:
				Ent -= (Pro[j]/(1-ProSum[i]) * math.log(Pro[j]/(1-ProSum[i])+0.001))

		if Ent > METSum:
			METi = i
			METSum = Ent
	print("argmax = " + str(METi))
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			if img[i][j] <= METi:
				img[i][j] = 0
			else:
				img[i][j] = 255
	Init.LogWrite("MET calculation succeed", "0")
	Output(img)


def MainFunction(kind, Remimg):
	os.system("clear")
	if kind == 0:
		img = FigureInput()
		try:
			Remimg = img.copy()
		except:
			return

		try:
			if img == -1:
				return
		except:
			pass

		InpStr = input("Lock the figure?[Y/ n]  ")
		if InpStr == "N" or InpStr == "n":
			kind = 0
		else:
			kind = 1
	else:
		img = Remimg.copy()

	os.system("clear")
	print("-1) Another Figure")
	print("1)  Gray level linear transformation.")
	print("2)  Gamma(power) transformation.")
	print("3)  Contrast-Stretching Transformations.")
	print("4)  Histogram Equalization")
	print("5)  Maximum entropy for thresholding")
	print("6)  Get Gradient of figure")
	print("7)  Thresholding with Gradient")
	print("8)  Statistic the figure")
	print("9)  Auto algorithm!")
	print("10) Monte Carlo Average Constrast")
	print("11) Convolution")
	print("12) Histogram Equalization with Monte Carlo")
	print("13) Gradient transformation Algorithm (GTA!)")
	print("14) 2 Side Gradient Treasholding with DFS")
	print("15) Median Filtering")
	print("16) Sobel 3 * 3 cross edge detection operator")
	print("17) Roberts cross edge detection operator")
	print("18) Gradient Treasholding with Convolution")
	print("19) The smallest variance smoothing filter")
	print("20) Canny edge detector")
	print("21) Random Walk Algorithm")
	print("22) Unsharp masking")
	print("23) Block Algorithm")
	print("24) Toboggan Algorithm")
	print("25) Linear PDE method")
	print("26) Non-linear PDE method")
	print("27) Bilateral Filter Smoothing")
	print("28) Least square estimation")
	print("29) Iterative solution")
	print("30) Fourier Transform")
	print("31) Histogram Fourier Transform")
	print("32) Entropy Analysis")
	print("33) Wavelet Algorithm")
	print("34) Gauss Random")
	print("35) ADMM Algorithm")
	print("0)　EXIT")
	InpInt = 0
	while 1:
		InpStr = input("Input the algorithm you need:  ")
		try:
			InpInt = int(InpStr)
		except ValueError:
			print("Input Error")
			continue
		else:
			if InpInt < -1 or InpInt > 50:
				print("Input Error")
				continue
			else:
				break

	if InpInt == -1:
		MainFunction(0, [])
		return
	if InpInt == 0:
		return 
	if InpInt == 1:
		img = Proj1.GLLT(img)
	if InpInt == 2:
		img = Proj1.GPT(img)
	if InpInt == 3:
		img = Proj1.CST(img)
	if InpInt == 4:
		img = Proj1.HE(img)
	if InpInt == 5:
		MET(img)
		MainFunction(kind, Remimg)
		return
	if InpInt == 6:
		GradFig.GetGradient(img)
		MainFunction(kind, Remimg)
		return
	if InpInt == 7:
		img = GradFig.GT(img)
	if InpInt == 8:
		GradFig.FigSta(img, 0)
		MainFunction(kind, Remimg)
		return
	if InpInt == 9:
		img = Algorithm.Algorithm(img)
	if InpInt == 10:
		img = Algorithm.MCAC(img)
	if InpInt == 11:
		img = Convolution.Convolution(img)
		Output(img)
		return
	if InpInt == 12:
		img = Algorithm.MCHE(img)
	if InpInt == 13:
		img = GradFig.GTA(img)
	if InpInt == 14:
		img = GradFig.TGT(img)
	if InpInt == 15:
		img = Proj2.MF(img)
	if InpInt == 16:
		img = Proj2.SO(img)
	if InpInt == 17:
		img = Proj2.RO(img)
	if InpInt == 18:
		img = Proj2.GOC(img)
	if InpInt == 19:
		img = Proj2.SVSF(img)
	if InpInt == 20:
		img = Algorithm.CED(img)
	if InpInt == 21:
		img = Algorithm.RWPI(img)
	if InpInt == 22:
		img = Proj3.UM(img)
	if InpInt == 23:
		img = Proj3.BlockAlg(img)
	if InpInt == 24:
		img = Algorithm.TobAlgo(img)
	if InpInt == 25:
		img = Proj4.PDEMethod(img, 1)
	if InpInt == 26:
		img = Proj4.PDEMethod(img, 2)
	if InpInt == 27:
		img = cv2.bilateralFilter(img, 9, 35, 35)
	if InpInt == 28:
		img = Proj5.LSE(img)
	if InpInt == 29:
		img = Proj5.IS(img)
	if InpInt == 30:
		img = Trans.FT(img)
	if InpInt == 31:
		Trans.HFT(img)
		MainFunction(kind, Remimg)
		return
	if InpInt == 32:
		img = ImgEnp.Main(img)
	if InpInt == 33:
		img = ProjTest.Wavelet(img)
	if InpInt == 34:
		img = ProjTest.Gauss(img)
	if InpInt == 35:
		img = ProjTest.ADMM(img)
	Output(img)
	InpStr = input("Use the new figure?[Y/n]  ")
	if InpStr == "Y" or InpStr == "y":
		Remimg = img.copy()

	MainFunction(kind, Remimg)
	return


MainFunction(0, [])






