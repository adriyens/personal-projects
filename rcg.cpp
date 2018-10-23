/*
Random Curse Generator: for those times you're so done you need a program to express your frustration

Concepts practiced:
  - vectors
  - rand() function

Future plans:
  - change it so that I use dictionaries instead of vectors
  - have a working menu system that allows user to generate multiple curses (commented out bc it's buggy)

 */

#include <iostream>
#include <cstdlib>
#include <time.h>
#include <string>
#include <vector>
using namespace std;

//generates random number between 1 - 100
int randNum(int num);

//adds -ing to the end of verb words
string ing(string verb);

//generates curse expressions
void curse();

/* ------VARIABLES------ */
vector <string> adj, verbs, noun, suffix; //vectors of various curse words
int ra, rv, rn, rs, pre, suf; //ints used to randomly generate nums
int input, amnt;
int count = 0;
bool inf = true;

int main() {
  srand(time(NULL));
  //need to figure out a way to create functions that'll do all this shit
  //but i keep getting out_of_range errors so ??? tbd
  //create a multilayered map!?!?!? idk how to do this so.. future!adrianne if ur out there....

  //adjectives
  adj.push_back("DAMN");
  adj.push_back("GODDAMN");
  adj.push_back("JESUS");
  adj.push_back("TITTY");

  //verbs
  verbs.push_back("BITCH");
  verbs.push_back("FUCK");
  verbs.push_back("MOTHERFUCK");
  verbs.push_back("SHITT");
  verbs.push_back("PISS");

  //nouns
  noun.push_back("ASS");
  noun.push_back("ASSHOLE");
  noun.push_back("BASTARD");
  noun.push_back("CUNT");
  noun.push_back("HELL");
  noun.push_back("BITCH");
  noun.push_back("FUCK");
  noun.push_back("SHIT");
  noun.push_back("CHRIST");
  noun.push_back("MOTHERFUCKER");
  noun.push_back("TITS");
  noun.push_back("FUCKER");
  noun.push_back("COCK");
  noun.push_back("DICK");
  noun.push_back("PENIS");
  noun.push_back("PIECE OF SHIT");
  noun.push_back("BALLS");
  noun.push_back("CUNTFLAPS");
  noun.push_back("CUNTFLAP");
  noun.push_back("PISS");
  noun.push_back("NIPPLE");
  noun.push_back("NIPPLES");

  //on a {whatever}
  suffix.push_back("STICK");
  suffix.push_back("BIKE");
  suffix.push_back("CRACKER");
  suffix.push_back("SCOOTER");
  suffix.push_back("POGO STICK");

  //casts size of vectors to an int to be used in randNum()
  ra = int(adj.size());
  rv = int(verbs.size());
  rn = int(noun.size());
  rs = int(suffix.size());

  cout << "Welcome to the Random Curse Generator\n" << endl;

  cout << "Hit ENTER to generate a curse: ";

  while (cin.get() == '\n') {
    cout << endl;
    curse();
    cout << endl;
    cout << "Hit ENTER to generate a curse: ";
  }

  /*
  cout << "How many curses you want?\n"
    << "1. Just one\n"
    << "2. A certain amount\n"
    << "3. Just fuck me up\n"
    << "4. Actually, I'm good now\n"
    << endl;

  do {
    cout << "Choose an option: "; cin >> input;
  switch(input){
    case 1:
      cout << endl;
      curse();
      cout << endl;
      break;
    case 2:
      cout << "How many do you want? "; cin >> amnt;
      cout << endl;
      while (count < amnt){
        curse();
        count++;
      }
      cout << endl;
      break;
    case 3:
      cout << endl;
      while (inf == true)
        curse();
      break;
    case 4:
      exit(1);
      break;
    default:
      cout << "Bitch what the fuck" << endl;
      break;
  }
  } while (input > 0 or input < 4);
  */

  return 0;
}

int randNum(int num){return rand() % num;}
string ing(string verb){return verb + "ING";}

void curse(){
  bool addon = false;
  bool before = true;
  suf = rand() % 100 + 1;
  pre = rand() % 100 + 1;

  //50% chance the curse will have "on a {whatever}" at the end
  if (suf >= 50)
    addon = true;

  //25% chance curse won't have an adjective
  if (pre <= 25)
    before = false;

  //adds an adjective to the beginning of curse
  if (before == true)
    cout << "\t" << adj.at(randNum(ra)) << " ";
  else
    cout << "\t";

  cout << ing(verbs.at(randNum(rv))) << " " << noun.at(randNum(rn));

  //adds "on a <whatever>" to the end
  if (addon == true)
    cout << " ON A " << suffix.at(randNum(rs)) << endl;
  else
    cout << endl;
}
