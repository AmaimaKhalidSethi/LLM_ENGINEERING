#include <iostream>
#include <chrono>

double calculate(int iterations, double param1, double param2) {
    double result = 1.0;
    for (int i = 1; i <= iterations; ++i) {
        double j = i * param1 - param2;
        result -= (1.0 / j);
        j = i * param1 + param2;
        result += (1.0 / j);
    }
    return result;
}

int main() {
    auto start_time = std::chrono::high_resolution_clock::now();
    double result = calculate(200000000, 4.0, 1.0) * 4.0;
    auto end_time = std::chrono::high_resolution_clock::now();

    std::printf("Result: %.12f\n", result);
    auto execution_time = std::chrono::duration_cast<std::chrono::duration<double>>(end_time - start_time);
    std::printf("Execution Time: %.6f seconds\n", execution_time.count());

    return 0;
}