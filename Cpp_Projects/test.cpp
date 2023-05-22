#include <iostream> // basic libhary for cout & cin
#include <string> // to enable use of string variable assignment
#include <typeinfo>
#include <vector> // creating dynamic arrays
using namespace std; // OPTIONAL short-hand coding (i.e. std::cout --> cout)


int main(){ // the entry point of EVERY SINGLE C++ program

    // vector <int> vector1{2};
    // vector <int> vector2(2);

    // std::cout<<"vector 1 size is " << vector1.size() << ", and the first value is " << vector1[0] << std::endl; // vector 1 size is 1, and the first value is 2
    // std::cout << "vector 2 size is " << vector2.size() << ", and the first value is " << vector2[0] << std::endl; // vector 2 size is 2, and the first value is 0

    // vector1.push_back(10); // .push_back will add the argument to the end of the vector
    // vector1.push_back(20);

    // cout << vector1[0] << ' ' << vector1[1] << ' ' << sizeof(vector1); // sizeof() operator will return the bit/byte size of the argument


//     vector2.push_back(100); 
//     vector2.push_back(200);

//     cout << vector2[0] << vector2[1]
//     << sizeof(vector2) << endl;

    
//     vector <vector<int>> vector_2d;

//     vector_2d.push_back(vector1);
//     vector_2d.push_back(vector2);

//     cout << vector_2d.at(0)[0] << " " << vector_2d.at(1)[0] << endl;

//     vector1.at(0) = 1000;

//     cout << vector_2d.at(0)[0] << " " << vector_2d.at(1)[0] << endl;

//     return 0;
// }



/**************************************************
SWITCH -- a "case" study...
**************************************************/

// char a = 's';

// switch (a)
// {
// case 4: std::cout<<"the int 4 was chosen" << std::endl;
// case '0':
// case '1': std::cout<<"0 or 1 was chosen" << std::endl;
// default: std::cout<< "this is where we break";break;
// }

// std::vector<int> pipe_fix(const std::vector<int>& nums) {



/**************************************************
VECTORS -- the better kind of arrays!
**************************************************/

// std::vector<int> nums{1,2,3,4,5};
// std::vector<int> newNums(nums.size());
  
// std::cout<< "the size of nums vector is " << nums.size() << std::endl;
// for(int i = 0; i < nums.size(); i++){
//     std::cout<<"current iteration is " << nums[i] << std::endl;

//     newNums[i] = i+1;

// }

// std::cout << "ok so something happened here..." << std::endl;
// std::cout << newNums[0] << std::endl;



/**************************************************
POINTERS -- separating the boys from the men
**************************************************/


return 0; // LEAVE THIS LINE ALONE!!
}
