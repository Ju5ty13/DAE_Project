// See https://aka.ms/new-console-template for more information
using System.Diagnostics;

Console.WriteLine("What is my name?");
string myname = "Justin";
Console.WriteLine(myname);
Console.WriteLine("What is my age?");
int myage = 17;
Console.WriteLine(myage);
Console.WriteLine("whats a more accurate representation of my age?");
float accurateage = 17.2f;
Console.WriteLine(accurateage);
Console.WriteLine("hmm im wondering what the weather is right now");

bool isthundering = true;
bool israining = false;
bool iscloudy = false;

if (isthundering)
{Console.WriteLine("AHHHH NOO GET BACK INSIDE ITS THUNDERING1!!");}
else if (israining)
{Console.WriteLine("i like this hehehe");}
else if (iscloudy)
{Console.WriteLine("hmm this is okay");}

int meowsmade = 0; 
while (meowsmade < 10) 
{
    Console.WriteLine ("THUNDER!");
meowsmade++;}
for (int click = 0; click < 20; click++)
{
Console.WriteLine ("AAAA ARE WE SAFE!?" + (click + 1));}

int Add(int a, int b)
{
    return a + b;
}
int result = Add(10,10);

Console.WriteLine(result);

Console.WriteLine("okay i think we're safe.. thankfully");


// just tests, they dont work yet
//public int playerHealth = 100;
//private string secretpower = "Top secret super powers from lightning!";
Console.WriteLine("i think i need a break from the outside, lets go get a drink at a vending machine");


int[] numbers = { 5, 10, 15, 20 };

Console. WriteLine (numbers[0]);

List<string> friends = new List<string>(); // empty list

friends. Add ("Charlie");
