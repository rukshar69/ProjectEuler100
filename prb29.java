package Euler;

public class prb29 {

	static void solution(int a, int b) {
		int upperLim =(int) Math.pow(a, b);
		System.out.println(upperLim);
		boolean visited[] = new boolean[upperLim+1];
		for(int i =2;i<=a;i++) {
			for(int j =2;j<=b;j++) {
				visited[(int)Math.pow(i, j)] = true;
			}
		}
		
		int count = 0;
		for(int i =4;i<=upperLim;i++) {
			if(visited[i])count++;
		}
		
		System.out.println(count);
	}
	public static void main(String[] args) {
		solution(100,100);
	}
}
