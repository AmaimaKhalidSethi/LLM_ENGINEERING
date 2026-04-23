
#include <iostream>
#include <chrono>

using namespace std;
using namespace chrono;

double calculate(long long iterations, double param1, double param2) {
    double result = 1.0;
    for (long long i = 1; i <= iterations; ++i) {
        double j = i * param1 - param2;
        result -= (1.0 / j);
        j = i * param1 + param2;
        result += (1.0 / j);
    }
    return result;
}

int main() {
    auto start_time = high_resolution_clock::now();
    double result = calculate(200000000LL, 4.0, 1.0) * 4.0;
    auto end_time = high_resolution_clock::now();
    
    auto duration = duration_cast<microseconds>(end_time - start_time);
    
    printf("Result: %.12f\n", result);
    printf("Execution Time: %.6f seconds\n", duration.count() / 1000000.0);
    
    return 0;
}
