package resizeFile;

import java.awt.Graphics;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

import javax.imageio.ImageIO;

import org.apache.sanselan.ImageReadException;

import converter.cmykConverter;

public class Resize {

	String imgOriginPath;
	String imgTargetPath;
	String imgName;
	String imgFormat = "png";
	int width;
	int height;

	int originWidth;
	int originHeight;

	public static void main(String[] args) {

		new Resize().resizeImage();

	}

	public void cmykToRGB() {

	}

	Scanner sc = new Scanner(System.in);

	public void imageSet() {
		System.out.println("변경할 이미지 경로 입력 : ");
		imgOriginPath = sc.nextLine();

		System.out.println("저장할 이미지 경로 입력 : ");
		imgTargetPath = sc.nextLine();

		System.out.println("============================");

		System.out.print("저장할 이미지 이름 : ");
		imgName = sc.nextLine();

		System.out.print("넓이 : ");
		width = sc.nextInt();

		System.out.print("높이 : ");
		height = sc.nextInt();

	}

	public void resizeImage () {
		cmykConverter cc = new cmykConverter();
		imageSet();
		Image image = null;
		File originFiles = new File(imgOriginPath);
		File originFileName[] = originFiles.listFiles();	//originFiles 아래의 모든 파일
		try {
			for (int i = 0; i < originFileName.length; i++) {
				File file = originFileName[i];
				//System.out.println(file);
				try {
					image = ImageIO.read(file);
				}catch (Exception e) {
					try {
						image = cc.readImage(file);
					} catch (ImageReadException e1) {
						e1.printStackTrace();
					}
				}
				
			
			
				
				originWidth = image.getWidth(null);
				originHeight = image.getHeight(null);
				
				Image resizeImg = image.getScaledInstance(width, height, Image.SCALE_FAST);
				
				//흑백이미지로 변경	: TYPE_USHORT_GRAY
				BufferedImage newImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
				Graphics g = newImage.getGraphics();
				g.drawImage(resizeImg, 0, 0, null);	//x, y 좌표 설정
				g.dispose();//객체 삭제 처리(?)
				
				File resizedFile = new File(imgTargetPath + "\\" + imgName + i + ".png");
				ImageIO.write(newImage, imgFormat, resizedFile);
			}
		}catch(

	IOException e)
	{
		e.printStackTrace();
	}

}

}
