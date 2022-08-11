#include <iostream>
#include <gtest/gtest.h>
#include "SingleArray/SingleArray.hpp"
#include "VectorArray/VectorArray.hpp"

using namespace std;
// Demonstrate some basic assertions.

TEST(SingleArrayTest, BaseTestAdd) {
  auto single_array = SingleArray();
  single_array.add(1, 3);
  EXPECT_EQ(single_array.Getstr(), "0 0 0 1");
  EXPECT_EQ(single_array.size, 4);
  printf("%d", single_array.arr[5]);

  single_array.add(2, 3);
  EXPECT_EQ(single_array.Getstr(), "0 0 0 2 1");
  EXPECT_EQ(single_array.size, 5);

  single_array.add(-5, 0);
  EXPECT_EQ(single_array.Getstr(), "-5 0 0 0 2 1");
  EXPECT_EQ(single_array.size, 6);

  single_array.add(120, 9);
  EXPECT_EQ(single_array.Getstr(), "-5 0 0 0 2 1 0 0 0 120");
  EXPECT_EQ(single_array.size, 10);
}

TEST(SingleArrayTest, BaseTestRemove) {
  auto single_array = SingleArray();
  single_array.add(1, 3);
  EXPECT_EQ(single_array.Getstr(), "0 0 0 1");
  EXPECT_EQ(single_array.size, 4);

  single_array.remove(2);
  EXPECT_EQ(single_array.Getstr(), "0 0 1");
  EXPECT_EQ(single_array.size, 3);

  single_array.add(2, 0);
  EXPECT_EQ(single_array.Getstr(), "2 0 0 1");
  EXPECT_EQ(single_array.size, 4);

  single_array.remove(0);
  EXPECT_EQ(single_array.Getstr(), "0 0 1");
  EXPECT_EQ(single_array.size, 3);
}

TEST(VectorArrayTest, BaseTestAdd) {
  auto vector_array = VectorArray(20);
  EXPECT_EQ(3, 3);
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}