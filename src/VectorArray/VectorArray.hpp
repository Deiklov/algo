#ifndef ARRAYS__VECTORARRAY_HPP_
#define ARRAYS__VECTORARRAY_HPP_
#include <cstdio>
#include <string>
using namespace std;
class VectorArray {
 public:
  int *arr;
  int size;
  explicit VectorArray(uint64_t scale_size);
  void add(int item, u_int64_t index);
  int remove(u_int64_t index);
  string Getstr();
};

#endif //ARRAYS__VECTORARRAY_HPP_
