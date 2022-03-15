import java.util.*;

public class BrickaBrack
{
   public static void main(String args[])
   {
      Scanner scan = new Scanner(System.in);
      int points = 0;
      int power = 1;
      int cost = 10;
      String userText = "";
      
      System.out.println("Do you wanna play a ga-a-ame?");
      System.out.print("Type Y to play and Q to quit : ");
      userText = scan.next();
      
      while (!userText.equals("Q"))
      {
         System.out.println("Press enter to brack bricks");
         System.out.println("To power up, type upgrade.");
         for (int i = 0; i < 50; i++)
         {
            userText = scan.nextLine();
            if (userText.equals("upgrade"))
            {
               if (points >= cost)
               {
                  power++;
                  points -= cost;
                  cost = 2*cost + 3;
               }
               else
               {
                  System.out.println("You need " + cost + " points");
               }
            }
            points += (Math.random() * (power + 1));
            System.out.println("Points : " + points);
         }
         
         System.out.println("Do you wanna play a ga-a-ame?");
         System.out.print("Type Y to play and Q to quit : ");
         userText = scan.next();
      }
   }
}