public class FinalAverage
{
	private int[] grades;
	private boolean isHonors, isAP;
	
	public FinalAverage(int[] g, boolean h, boolean ap)
	{
		grades = new int[g.length];
		for (int i = 0; i < g.length; i++)
		{
			grades[i] = g[i];
		}
		isHonors = h;
		isAP = ap;
	}
	
	public double getAverage()
	{
		double sum = 0.0;
		for (int i = 0; i < grades.length; i++)
		{
			sum += grades[i];
		}
		return sum / grades.length;
	}
	
	public int dropLowest()
	{
		int min = grades[0];
		int indexMin = 0;
		for (int i = 0; i < grades.length; i++)
		{
			if (grades[i] < min)
			{
				min = grades[i];
				indexMin = i;
			}
		}
		
		int[] temp = new int[grades.length-1];
		for (int i = 0; i < grades.length; i++)
		{
			if (i < indexMin)
			{
				temp[i] = grades[i];
			}
			if (i > indexMin)
			{
				temp[i-1] = grades[i];
			}
		}
		grades = temp;
	}
}