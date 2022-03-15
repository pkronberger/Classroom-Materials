public class Circle
{
	private int radius;
	
	public Circle()
	{
		radius = 1;
	}
	
	public Circle(int rad)
	{
		this.radius = rad;
	}
	
	public int getRadius()
	{
		return radius;
	}
	
	public void setRadius(int newRadius)
	{
		radius = newRadius;
	}
	
	public int getArea()
	{
		return (int) (Math.PI * radius * radius);
	}
	
	public int getCircumference()
	{
		return (int) (2 * Math.PI * radius);
	}
	
	public String toString()
	{
		return "Circle Radius - " + radius;
	}
}