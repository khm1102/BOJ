use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let left: i32 = input.trim().parse().expect("Invalid left value");

    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let right: i32 = input.trim().parse().expect("Invalid right value");

    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let k: i32 = input.trim().parse().expect("Invalid k value");

    let count = match k {
        2 => std::cmp::max(right - std::cmp::max(left, 3) + 1, 0),
        3 => (std::cmp::max(left, 6)..=right).filter(|&x| x % 3 == 0).count() as i32,
        4 => (std::cmp::max(left, 10)..=right)
            .filter(|&x| x % 2 == 0 && x != 12)
            .count() as i32,
        5 => (std::cmp::max(left, 15)..=right).filter(|&x| x % 5 == 0).count() as i32,
        _ => panic!(),
    };

    println!("{}", count);
}
