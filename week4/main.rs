use std::time::Instant;

const MOD: u64 = 1 << 32;
const A: u64 = 1664525;
const C: u64 = 1013904223;

#[inline]
fn lcg(seed: u64) -> impl Iterator<Item = u64> {
    std::iter::successors(Some(seed), move |&value| {
        Some((A.wrapping_mul(value).wrapping_add(C)) % MOD)
    })
}

#[inline]
fn max_subarray_sum(n: usize, seed: u64, min_val: i32, max_val: i32) -> i32 {
    let mut max_sum = i32::MIN;
    let mut random_numbers = vec![0i32; n];
    
    // Generate random numbers using LCG
    let mut lcg_iter = lcg(seed);
    for i in 0..n {
        random_numbers[i] = (lcg_iter.next().unwrap() % (max_val - min_val + 1) as u64 + min_val as u64) as i32;
    }
    
    // Kadane's algorithm for maximum subarray sum
    for i in 0..n {
        let mut current_sum = 0;
        for j in i..n {
            current_sum += random_numbers[j];
            if current_sum > max_sum {
                max_sum = current_sum;
            }
        }
    }
    
    max_sum
}

fn total_max_subarray_sum(n: usize, initial_seed: u64, min_val: i32, max_val: i32) -> i64 {
    let mut total_sum: i64 = 0;
    let mut lcg_iter = lcg(initial_seed);
    
    for _ in 0..20 {
        let seed = lcg_iter.next().unwrap();
        total_sum += max_subarray_sum(n, seed, min_val, max_val) as i64;
    }
    
    total_sum
}

fn main() {
    let n = 10000;
    let initial_seed = 42;
    let min_val = -10;
    let max_val = 10;
    
    let start_time = Instant::now();
    let result = total_max_subarray_sum(n, initial_seed, min_val, max_val);
    let end_time = Instant::now();
    
    let duration = end_time.duration_since(start_time);
    let seconds = duration.as_secs_f64();
    
    println!("Total Maximum Subarray Sum (20 runs): {}", result);
    println!("Execution Time: {:.6f} seconds", seconds);
}