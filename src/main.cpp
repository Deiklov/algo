#include <iostream>
#include <gtest/gtest.h>
#include "SingleArray/SingleArray.hpp"
using namespace std;
// Demonstrate some basic assertions.
TEST(HelloTest, BasicAssertions) {
  // Expect two strings not to be equal.
  auto kekmda = SingleArray();
  kekmda.add(1, 3);
  cout << kekmda.size << endl;
  kekmda.print();
  EXPECT_EQ(kekmda.arr[3], 1);
  kekmda.add(2, 3);
  EXPECT_EQ(kekmda.arr[3], 2);
  kekmda.print();
  EXPECT_EQ(kekmda.arr[4], 1);
  kekmda.print();
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}