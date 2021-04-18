package renameFile;

import java.io.File;
import java.util.Scanner;

public class Rename {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		
		System.out.println("파일이름 변경을 원하는 경로 입력 : ");
		String fileUrl = sc.nextLine();
		System.out.println("변경할 이름 입력 : ");
		String fileName = sc.next();
		
		
		File file = new File(fileUrl);
		
		File[] fileList = file.listFiles();
		for (int i = 0; i < fileList.length; i++) {
			fileList[i].renameTo(new File(file.getPath()+ "\\" + fileName + (i+1) + ".png" ));
		}
		
			
		}		
	}
