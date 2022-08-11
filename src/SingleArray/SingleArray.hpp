#ifndef ARRAYS__SINGLEARRAY_HPP_
#define ARRAYS__SINGLEARRAY_HPP_
#include <cstdio>
class SingleArray {
 public:
  int *arr;
  int size;
  explicit SingleArray();
  void add(int item, u_int64_t index);
  int remove(u_int64_t index);
  void print();
};

#endif //ARRAYS__SINGLEARRAY_HPP_
