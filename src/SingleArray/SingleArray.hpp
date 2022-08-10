#ifndef ARRAYS__SINGLEARRAY_HPP_
#define ARRAYS__SINGLEARRAY_HPP_
#include <cstdio>
class SingleArray {
  int *arr;
  int size;
 public:
  explicit SingleArray();
  void add(int item, int index);
  int remove(int index);
  void print();
};

#endif //ARRAYS__SINGLEARRAY_HPP_
