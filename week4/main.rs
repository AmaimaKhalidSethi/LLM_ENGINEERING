fn lcg(seed: u32, a: u32, c: u32, m: u32) -> impl Iterator<Item = u32> {
    std::iter::successors(Some(seed), move |value| Some((a.wrapping_mul(*value).wrapping_add(c)) % m))
}

fn max_subarray_sum(n: usize, seed: u32, min_val: i32, max_val: i32) -> i64 {
    let mut lcg_gen = lcg(seed, 1664525, 1013904223, 2u32.pow(32));
    let random_numbers: Vec<i32> = (0..n)
        .map(|_| (lcg_gen.next().unwrap() as i32) % (max_val - min_val + 1) + min_val)
        .collect();
    let mut max_sum = std::i64::MIN;
    for i in 0..n {
        let mut current_sum: i64 = 0;
        for j in i..n {
            current_sum += random_numbers[j] as i64;
            if current_sum > max_sum {
                max_sum = current_sum;
            }
        }
    }
    max_sum
}

fn total_max_subarray_sum(n: usize, initial_seed: u32, min_val: i32, max_val: i32) -> i64 {
    let mut lcg_gen = lcg(initial_seed, 1664525, 1013904223, 2u32.pow(32));
    let mut total_sum: i64 = 0;
    for _ in 0..20 {
        let seed = lcg_gen.next().unwrap();
        total_sum += max_subarray_sum(n, seed, min_val, max_val);
    }
    total_sum
}

fn main() {
    let n = 10000;
    let initial_seed = 42;
    let min_val = -10;
    let max_val = 10;
    let start_time = std::time::Instant::now();
    let result = total_max_subarray_sum(n, initial_seed, min_val, max_val);
    let end_time = start_time.elapsed().as_secs_f64();
    println!("Total Maximum Subarray Sum (20 runs): {}", result);
    println!("Execution Time: {:.6} seconds", end_time);
}