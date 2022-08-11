#include <iostream>
#include <gtest/gtest.h>
#include "SingleArray/SingleArray.hpp"
using namespace std;
// Demonstrate some basic assertions.
TEST(SingleArrayTest, BaseTest) {
  // Expect two strings not to be equal.
  auto kekmda = SingleArray();
  kekmda.add(1, 3);
  EXPECT_EQ(kekmda.Getstr(), "0 0 0 1");
  EXPECT_EQ(kekmda.size, 4);

  kekmda.add(2, 3);
  EXPECT_EQ(kekmda.Getstr(), "0 0 0 2 1");
  EXPECT_EQ(kekmda.size, 5);

  kekmda.add(-5, 0);
  EXPECT_EQ(kekmda.Getstr(), "-5 0 0 0 2 1");
  EXPECT_EQ(kekmda.size, 6);

  kekmda.add(120, 9);
  EXPECT_EQ(kekmda.Getstr(), "-5 0 0 0 2 1 0 0 0 120");
  EXPECT_EQ(kekmda.size, 10);
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}