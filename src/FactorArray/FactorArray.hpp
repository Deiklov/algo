#ifndef ARRAYS__FACTORARRAY_HPP_
#define ARRAYS__FACTORARRAY_HPP_
#include <cstdio>
#include <string>
using namespace std;
class FactorArray {
 public:
  int *arr;
  int size;
  int cap;
  int scale_koef;
  explicit FactorArray();
  void add(int item, u_int64_t index);
  int remove(u_int64_t index);
  void grow();
  void compress();
  string Getstr();
};

#endif //ARRAYS__FACTORARRAY_HPP_
