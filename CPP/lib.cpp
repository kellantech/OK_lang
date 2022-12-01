#include <pybind11/pybind11.h>
#include <cctype>
#include <string>


namespace py = pybind11;

std::string remove_chars(std::string in) {
  bool rm = true;
  std::string out = in;
  for (int iter = 0; iter < in.length(); ++iter) {
    char c = in[iter];
    if (c == '"' || c == '\'') {
      rm = !rm;
    } else if (rm) {
      if (isalpha(c) != 0) {
        out.erase(out.find(in[iter]), 1);
      }
    }
  }
  return out;
}

PYBIND11_MODULE(lib,m){
	m.doc() = "OKLANG module";
	m.def("remove_chr",&remove_chars);
}

