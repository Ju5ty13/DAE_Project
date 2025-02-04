// See https://aka.ms/new-console-template for more information
using System;
using System.Diagnostics;

class Player
{
    // Public variable (accessible from outside the class)
    public int playerHealth;

    // Private variable (only accessible inside this class)
    private string secretPower;

    // Constructor to initialize the player
    public Player(int health, string power)
    {
        playerHealth = health;
        secretPower = power;
    }

    // Public method to access the private variable
    public void RevealSecretPower()
    {
        Console.WriteLine($"Psst... my secret power is: {secretPower}");
    }
}

class Program
{
    static void Main()
    {
        Console.WriteLine("What is my name?");
        string myname = "Justin";
        Console.WriteLine(myname);

        Console.WriteLine("What is my age?");
        int myage = 17;
        Console.WriteLine(myage);

        Console.WriteLine("What's a more accurate representation of my age?");
        float accurateAge = 17.2f;
        Console.WriteLine(accurateAge);

        Console.WriteLine("Hmm... I'm wondering what the weather is right now.");

        bool isThundering = true;
        bool isRaining = false;
        bool isCloudy = false;

        if (isThundering)
        {
            Console.WriteLine("AHHHH NOO GET BACK INSIDE ITS THUNDERING!!");
        }
        else if (isRaining)
        {
            Console.WriteLine("I like this hehehe");
        }
        else if (isCloudy)
        {
            Console.WriteLine("Hmm, this is okay");
        }

        Console.WriteLine("OH NO! I think I just got struck by lightning!");

        // Create a player object after getting struck by lightning
        Player me = new Player(100, "Top secret superpowers from lightning!");

        Console.WriteLine($"Am I okay? Checking health... {me.playerHealth} HP");
        
        Console.WriteLine("Wait... do I feel different?");
        me.RevealSecretPower(); // Reveal the secret power

        int meowsMade = 0;
        while (meowsMade < 10)
        {
            Console.WriteLine("THUNDER!");
            meowsMade++;
        }

        for (int click = 0; click < 20; click++)
        {
            Console.WriteLine("AAAA ARE WE SAFE!?" + (click + 1));
        }

        int Add(int a, int b)
        {
            return a + b;
        }
        int result = Add(10, 10);

        Console.WriteLine(result);
        Console.WriteLine("Okay, I think we're safe... thankfully.");

        Console.WriteLine("I think I need a break from the outside. Let's go get a drink at a vending machine.");

        int[] numbers = { 5, 10, 15, 20 };
        Console.WriteLine(numbers[0]);
    }
}
