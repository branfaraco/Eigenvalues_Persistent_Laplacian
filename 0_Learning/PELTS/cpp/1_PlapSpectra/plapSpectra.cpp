#include "Complex.hpp"
#include <Eigen/Dense>
#include <vector>
#include <tuple>
#include <iostream>

int main() {
    // d1 = [[-1,0,-1],
    //       [ 1,-1,0],
    //       [ 0, 1,1]]
    Eigen::MatrixXi d1(3, 3);
    d1 << -1,  0, -1,
           1, -1,  0,
           0,  1,  1;

    // d2 = [[ 1],
    //       [ 1],
    //       [-1]]
    Eigen::MatrixXi d2(3, 1);
    d2 <<  1,
          1,
         -1;

    std::vector<Eigen::MatrixXi> boundaries = {d1, d2};

    // filtrations = [
    //   [0,1,2],  // dim 0
    //   [3,4,5],  // dim 1
    //   [5]       // dim 2
    // ]
    std::vector<std::vector<double>> filtrations = {
        {0, 1, 2},
        {3, 4, 5},
        {5}
    };

    petls::Complex complex(boundaries, filtrations);

    // spectra() typically returns: vector of (dim, a, b, eigenvalues)
    auto s = complex.spectra();

    // Print in a similar style to your earlier code
    for (const auto& spectrum : s) {
        int dim = std::get<0>(spectrum);
        double a = std::get<1>(spectrum);
        double b = std::get<2>(spectrum);
        const std::vector<float>& eigs = std::get<3>(spectrum);

        std::cout << "Eigenvalues of L_{" << dim << "}^{" << a << "," << b << "} = [";
        for (int i = 0; i < (int)eigs.size(); ++i) {
            std::cout << eigs[i];
            if (i + 1 < (int)eigs.size()) std::cout << ", ";
        }
        std::cout << "]\n";
    }

    return 0;
}
